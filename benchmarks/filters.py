from __future__ import annotations

import base64
import zlib
from typing import ClassVar

from pdfminer.ascii85 import ascii85decode, asciihexdecode
from pdfminer.lzw import lzwdecode
from pdfminer.pdftypes import PDFStream
from pdfminer.psparser import LIT
from pdfminer.runlength import rldecode
from pdfminer.utils import apply_png_predictor, decode_text

PAYLOAD = bytes(range(256)) * 256


def run_length_encode(data: bytes) -> bytes:
    encoded = bytearray()
    for offset in range(0, len(data), 128):
        block = data[offset : offset + 128]
        encoded.append(len(block) - 1)
        encoded.extend(block)
    encoded.append(128)
    return bytes(encoded)


class ASCII85Decoding:
    params: ClassVar = [64, 4096, 65536]
    param_names: ClassVar = ["decoded_bytes"]

    def setup(self, decoded_bytes: int) -> None:
        payload = PAYLOAD[:decoded_bytes]
        self.ascii85 = base64.a85encode(payload, adobe=True)
        self.asciihex = payload.hex().encode() + b">"

    def time_ascii85(self, decoded_bytes: int) -> bytes:
        return ascii85decode(self.ascii85)

    def time_asciihex(self, decoded_bytes: int) -> bytes:
        return asciihexdecode(self.asciihex)


class StreamDecoding:
    params: ClassVar = ["FlateDecode", "ASCII85Decode", "ASCIIHexDecode", "RunLengthDecode"]
    param_names: ClassVar = ["filter_name"]

    def setup(self, filter_name: str) -> None:
        if filter_name == "FlateDecode":
            self.encoded = zlib.compress(PAYLOAD)
        elif filter_name == "ASCII85Decode":
            self.encoded = base64.a85encode(PAYLOAD, adobe=True)
        elif filter_name == "ASCIIHexDecode":
            self.encoded = PAYLOAD.hex().encode() + b">"
        else:
            self.encoded = run_length_encode(PAYLOAD)
        self.filter = LIT(filter_name)

    def time_pdf_stream_decode(self, filter_name: str) -> bytes:
        return PDFStream({"Filter": self.filter}, self.encoded).get_data()


class Predictors:
    params: ClassVar = [64, 256, 1024]
    param_names: ClassVar = ["columns"]

    def setup(self, columns: int) -> None:
        row = bytes(index % 256 for index in range(columns * 3))
        self.encoded = (b"\x00" + row) * 64

    def time_png_predictor(self, columns: int) -> bytes:
        return apply_png_predictor(pred=12, colors=3, columns=columns, bitspercomponent=8, data=self.encoded)


class SmallDecoders:
    def time_lzw(self) -> bytes:
        return lzwdecode(b"\x80\x0b\x60\x50\x22\x0c\x0c\x85\x01")

    def time_run_length(self) -> bytes:
        return rldecode(b"\x05123456\xfa7\x04abcde\x80junk")


class PDFTextDecoding:
    params: ClassVar = ["ascii", "utf16", "pdfdoc"]
    param_names: ClassVar = ["encoding"]

    def setup(self, encoding: str) -> None:
        if encoding == "ascii":
            unit = b"plain ASCII text "
        elif encoding == "utf16":
            unit = b"\xfe\xff\x00H\x00e\x00l\x00l\x00o"
        else:
            unit = bytes((0x18, 0x1F, 0x80, 0x81, 0x8D, 0x95, 0xA0, 0xFF))
        self.value = unit * 256

    def time_decode_text(self, encoding: str) -> str:
        return decode_text(self.value)
