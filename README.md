core-pdfminer.six
=================

[![Continuous integration](https://github.com/core-experiments/core-pdfminer.six/actions/workflows/actions.yml/badge.svg)](https://github.com/core-experiments/core-pdfminer.six/actions/workflows/actions.yml)

*We fathom PDF*

Core-pdfminer.six is a performance-focused fork of pdfminer.six. It extracts information from PDF documents, with a
focus on text data, while retaining the familiar pdfminer.six API design under the `core_pdfminer_six` namespace.

It is modular, so individual components can be replaced. You can implement your own interpreter or rendering device for
uses beyond text analysis.

Check out the full documentation on
[Read the Docs](https://pdfminersix.readthedocs.io).


Features
--------

* Written entirely in Python.
* Parse, analyze, and convert PDF documents.
* Extract content as text, images, html or [hOCR](https://en.wikipedia.org/wiki/HOCR).
* Support for PDF-1.7 specification (well, almost).
* Support for CJK languages and vertical writing.
* Support for various font types (Type1, TrueType, Type3, and CID) support.
* Support for extracting embedded images (JPG, PNG, TIFF, JBIG2, bitmaps).
* Support for decoding various compressions (ASCIIHexDecode, ASCII85Decode, LZWDecode, FlateDecode, RunLengthDecode,
  CCITTFaxDecode)
* Support for RC4 and AES encryption.
* Support for AcroForm interactive form extraction.
* Table of contents extraction.
* Tagged contents extraction.
* Automatic layout analysis.

How to use
----------

* Install Python 3.10 or newer.
* Install core-pdfminer.six.
  ```bash
  pip install core-pdfminer.six

* (Optionally) install extra dependencies for extracting images.

  ```bash
  pip install 'core-pdfminer.six[image]'

* Use the command-line interface to extract text from pdf.

  ```bash
  pdf2txt.py example.pdf

* Or use it with Python.
  ```python
  from core_pdfminer_six.high_level import extract_text

  text = extract_text("example.pdf")
  print(text)
  ```

Contributing
------------

We welcome contributions! Whether you want to fix a bug, add a feature, or improve documentation, your help is appreciated.

Please note that as a community-maintained project with limited maintainer availability, the best way to get an issue resolved is to submit a pull request yourself.

To get started:
1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions and coding standards
2. Check out the [open issues](https://github.com/core-experiments/core-pdfminer.six/issues) to find something to work on

Acknowledgement
---------------

This repository includes code from `pyHanko` ; the original license has been included [here](/docs/licenses/LICENSE.pyHanko).
