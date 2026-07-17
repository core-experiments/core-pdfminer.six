from __future__ import annotations

from typing import ClassVar

from pdfminer.cmapdb import CMap, CMapDB
from pdfminer.encodingdb import EncodingDB


class IdentityCMapDecoding:
    params: ClassVar = [64, 4096, 65536]
    param_names: ClassVar = ["encoded_bytes"]

    def setup(self, encoded_bytes: int) -> None:
        self.horizontal = CMapDB.get_cmap("Identity-H")
        self.vertical = CMapDB.get_cmap("Identity-V")
        self.data = bytes(range(256)) * (encoded_bytes // 256)

    def time_horizontal(self, encoded_bytes: int) -> tuple[int, ...]:
        return tuple(self.horizontal.decode(self.data))

    def time_vertical(self, encoded_bytes: int) -> tuple[int, ...]:
        return tuple(self.vertical.decode(self.data))


class NestedCMapDecoding:
    def setup(self) -> None:
        self.cmap = CMap(CMapName="Benchmark")
        self.cmap.code2cid = {index: {suffix: index * 256 + suffix for suffix in range(16)} for index in range(16)}
        self.data = bytes(value % 16 for value in range(65536))

    def time_decode(self) -> tuple[int, ...]:
        return tuple(self.cmap.decode(self.data))


class EncodingLookup:
    params: ClassVar = ["StandardEncoding", "MacRomanEncoding", "WinAnsiEncoding", "PDFDocEncoding"]
    param_names: ClassVar = ["encoding"]

    def time_get_encoding(self, encoding: str) -> dict[int, str]:
        return EncodingDB.get_encoding(encoding)
