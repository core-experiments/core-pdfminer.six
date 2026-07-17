from __future__ import annotations

from typing import ClassVar, cast

from core_pdfminer_six.layout import LAParams, LTChar, LTComponent, LTPage
from core_pdfminer_six.pdfcolor import PREDEFINED_COLORSPACE
from core_pdfminer_six.pdffont import PDFFont
from core_pdfminer_six.pdfinterp import PDFGraphicState
from core_pdfminer_six.utils import Plane


class BenchmarkFont:
    fontname = "Helvetica"

    def is_vertical(self) -> bool:
        return False

    def get_descent(self) -> float:
        return -0.207


FONT = BenchmarkFont()
COLOR_SPACE = PREDEFINED_COLORSPACE["DeviceGray"]


def make_char(index: int, columns: int = 80) -> LTChar:
    column = index % columns
    row = index // columns
    return LTChar(
        matrix=(1, 0, 0, 1, column * 6, 760 - row * 12),
        font=cast(PDFFont, FONT),
        fontsize=10,
        scaling=1,
        rise=0,
        text=chr(65 + index % 26),
        textwidth=0.5,
        textdisp=0,
        ncs=COLOR_SPACE,
        graphicstate=PDFGraphicState(),
    )


class CharacterGeometry:
    params: ClassVar = [100, 1000, 10000]
    param_names: ClassVar = ["characters"]

    def time_construct_characters(self, characters: int) -> list[LTChar]:
        return [make_char(index) for index in range(characters)]


class SpatialPlane:
    params: ClassVar = [100, 1000, 10000]
    param_names: ClassVar = ["components"]

    def setup(self, components: int) -> None:
        self.components = [
            LTComponent(((index % 100) * 10, (index // 100) * 10, (index % 100) * 10 + 8, (index // 100) * 10 + 8))
            for index in range(components)
        ]
        self.bbox = (0, 0, 1000, max(10, ((components + 99) // 100) * 10))
        self.plane = Plane[LTComponent](self.bbox, gridsize=50)
        self.plane.extend(self.components)

    def time_build(self, components: int) -> Plane[LTComponent]:
        plane = Plane[LTComponent](self.bbox, gridsize=50)
        plane.extend(self.components)
        return plane

    def time_full_query(self, components: int) -> list[LTComponent]:
        return list(self.plane.find(self.bbox))

    def time_window_queries(self, components: int) -> int:
        return sum(len(list(self.plane.find((x, y, x + 100, y + 100)))) for x, y in self.queries)

    @property
    def queries(self) -> list[tuple[int, int]]:
        return [(x, y) for y in range(0, int(self.bbox[3]), 50) for x in range(0, 1000, 100)]


class LayoutAnalysis:
    params: ClassVar = [100, 500, 2000]
    param_names: ClassVar = ["characters"]
    timeout = 20.0

    def setup(self, characters: int) -> None:
        self.characters = characters
        self.laparams = LAParams()
        self.chars = [make_char(index) for index in range(characters)]

    def time_group_objects(self, characters: int) -> list[object]:
        page = LTPage(1, (0, 0, 612, 792))
        return list(page.group_objects(self.laparams, self.chars))

    def time_page_analysis(self, characters: int) -> LTPage:
        page = LTPage(1, (0, 0, 612, 792))
        for char in self.chars:
            page.add(char)
        page.analyze(self.laparams)
        return page
