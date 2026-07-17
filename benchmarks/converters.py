from __future__ import annotations

from io import BytesIO
from typing import ClassVar

from benchmarks.common import sample_path
from pdfminer.high_level import extract_text_to_fp


class OutputFormats:
    params: ClassVar = ["text", "html", "xml", "hocr", "tag"]
    param_names: ClassVar = ["output_type"]
    timeout = 30.0

    def setup(self, output_type: str) -> None:
        self.path = sample_path("nonfree/naacl06-shinyama.pdf")

    def time_convert_document(self, output_type: str) -> bytes:
        output = BytesIO()
        with self.path.open("rb") as source:
            extract_text_to_fp(source, output, output_type=output_type, codec="utf-8")
        return output.getvalue()
