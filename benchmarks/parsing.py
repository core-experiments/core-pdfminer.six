from __future__ import annotations

import sys
from io import BytesIO
from typing import ClassVar

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.psexceptions import PSEOF
from pdfminer.psparser import PSBaseParser, PSKeyword, PSStackParser


class BenchmarkStackParser(PSStackParser[PSKeyword]):
    def flush(self) -> None:
        self.add_results(*self.popall())

    def do_keyword(self, pos: int, token: PSKeyword) -> None:
        self.add_results((pos, token))


TOKEN_FRAGMENT = (
    b"123 -45 +.5 1.25 true false /Name /escaped#20name "
    b"(plain string) (nested (string) and \\ escape) <4142f> "
    b"[1 2 /Array] << /Key (value) /Count 3 >> keyword\n"
)


class Tokenization:
    params: ClassVar = [1, 32, 256]
    param_names: ClassVar = ["fragment_repetitions"]

    def setup(self, fragment_repetitions: int) -> None:
        self.data = TOKEN_FRAGMENT * fragment_repetitions

    def time_base_parser(self, fragment_repetitions: int) -> int:
        parser = PSBaseParser(BytesIO(self.data))
        count = 0
        try:
            while True:
                parser.nexttoken()
                count += 1
        except PSEOF:
            return count

    def time_stack_parser(self, fragment_repetitions: int) -> int:
        parser = BenchmarkStackParser(BytesIO(self.data))
        count = 0
        try:
            while True:
                parser.nextobject()
                count += 1
        except PSEOF:
            return count


def make_pdf_with_xref_chain(length: int) -> bytes:
    header = b"%PDF-1.4\n"
    catalog_offset = len(header)
    catalog = b"1 0 obj\n<< /Type /Catalog >>\nendobj\n"
    parts = [header, catalog]
    size = len(header) + len(catalog)
    previous_offset: int | None = None
    xref_offsets = []

    for _ in range(length):
        xref_offsets.append(size)
        previous = b"" if previous_offset is None else b" /Prev " + str(previous_offset).encode()
        section = (
            b"xref\n0 2\n0000000000 65535 f \n"
            + f"{catalog_offset:010d} 00000 n \n".encode()
            + b"trailer\n<< /Size 2 /Root 1 0 R"
            + previous
            + b" >>\n"
        )
        parts.append(section)
        size += len(section)
        previous_offset = xref_offsets[-1]

    parts.append(b"startxref\n" + str(xref_offsets[-1]).encode() + b"\n%%EOF\n")
    return b"".join(parts)


class CrossReferenceChains:
    params: ClassVar = [10, 250, sys.getrecursionlimit() + 100]
    param_names: ClassVar = ["xref_sections"]
    timeout = 20.0

    def setup(self, xref_sections: int) -> None:
        self.pdf = make_pdf_with_xref_chain(xref_sections)

    def time_document_construction(self, xref_sections: int) -> int:
        parser = PDFParser(BytesIO(self.pdf))
        document = PDFDocument(parser, fallback=False)
        return len(document.xrefs)
