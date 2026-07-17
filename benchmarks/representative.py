from __future__ import annotations

from typing import ClassVar

from benchmarks.common import sample_path
from core_pdfminer_six.high_level import extract_pages, extract_text
from core_pdfminer_six.pdfpage import PDFPage

REPRESENTATIVE_PDFS = [
    "simple1.pdf",
    "contrib/issue-598-cmap-other-fonts.pdf",
    "contrib/matplotlib.pdf",
    "contrib/issue-1113-evil-xobjects.pdf",
    "nonfree/naacl06-shinyama.pdf",
]


class RepresentativeExtraction:
    params: ClassVar = REPRESENTATIVE_PDFS
    param_names: ClassVar = ["document"]
    timeout = 60.0

    def setup(self, document: str) -> None:
        self.path = sample_path(document)

    def time_extract_text(self, document: str) -> str:
        return extract_text(self.path)

    def time_extract_pages(self, document: str) -> list[object]:
        return list(extract_pages(self.path))

    def time_enumerate_pdf_pages(self, document: str) -> list[PDFPage]:
        with self.path.open("rb") as source:
            return list(PDFPage.get_pages(source))

    def peakmem_extract_text(self, document: str) -> str:
        return extract_text(self.path)

    def track_extracted_characters(self, document: str) -> int:
        return len(extract_text(self.path))


class EdgeCaseExtraction:
    params: ClassVar = [
        "contrib/issue-1061-colour-space-stack.pdf",
        "contrib/issue-1062-filters.pdf",
        "contrib/issue-886-xref-stream-widths.pdf",
        "contrib/issue-1249-evil-xrefs.pdf",
    ]
    param_names: ClassVar = ["document"]
    timeout = 60.0

    def setup(self, document: str) -> None:
        self.path = sample_path(document)

    def time_extract_text(self, document: str) -> str:
        return extract_text(self.path)


ENCRYPTED_PDFS = {
    "rc4-40": ("encryption/rc4-40.pdf", "foo"),
    "aes-128": ("encryption/aes-128.pdf", "foo"),
    "aes-256": ("encryption/aes-256.pdf", "foo"),
    "aes-256-r6": ("encryption/aes-256-r6.pdf", "usersecret"),
}


class EncryptedExtraction:
    params: ClassVar = list(ENCRYPTED_PDFS)
    param_names: ClassVar = ["encryption"]
    timeout = 30.0

    def setup(self, encryption: str) -> None:
        document, self.password = ENCRYPTED_PDFS[encryption]
        self.path = sample_path(document)

    def time_extract_text(self, encryption: str) -> str:
        return extract_text(self.path, password=self.password)
