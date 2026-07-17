Welcome to core-pdfminer.six's documentation!
*********************************************

.. image:: https://github.com/core-experiments/core-pdfminer.six/actions/workflows/actions.yml/badge.svg
    :target: https://github.com/core-experiments/core-pdfminer.six/actions/workflows/actions.yml
    :alt: Continuous integration status

We fathom PDF.

Core-pdfminer.six is a performance-focused Python package for extracting information from PDF documents.

Check out the source on `GitHub <https://github.com/core-experiments/core-pdfminer.six>`_.

Content
=======

This documentation is organized into four sections (according to the `Diátaxis
documentation framework <https://diataxis.fr>`_). The
:ref:`tutorial` section helps you setup and use core-pdfminer.six for the first
time. Read this section if this is your first time working with core-pdfminer.six.
The :ref:`howto` offers specific recipes for solving common problems.
Take a look at the :ref:`topic` if you want more background information on
how core-pdfminer.six works internally. The :ref:`reference` provides
detailed api documentation for all the common classes and functions in
core-pdfminer.six.

.. toctree::
    :maxdepth: 2

    tutorial/index
    howto/index
    topic/index
    reference/index
    faq


Features
========

* Parse all objects from a PDF document into Python objects.
* Analyze and group text in a human-readable way.
* Extract text, images (JPG, JBIG2 and Bitmaps), table-of-contents, tagged
  contents and more.
* Support for (almost all) features from the PDF-1.7 specification
* Support for Chinese, Japanese and Korean CJK) languages as well as vertical writing.
* Support for various font types (Type1, TrueType, Type3, and CID).
* Support for RC4 and AES encryption.
* Support for AcroForm interactive form extraction.


Installation instructions
=========================

* Install Python 3.10 or newer.
* Install core-pdfminer.six.

::
    $ pip install core-pdfminer.six

* (Optionally) install extra dependencies for extracting images.

::
    $ pip install 'core-pdfminer.six[image]'

* Use the command-line interface to extract text from pdf.

::
    $ pdf2txt.py example.pdf

* Or use it with Python.

.. code-block:: python

    from core_pdfminer_six.high_level import extract_text

    text = extract_text("example.pdf")
    print(text)



Contributing
============

We welcome any contributors to core-pdfminer.six! But, before doing anything, take
a look at the `contribution guide
<https://github.com/core-experiments/core-pdfminer.six/blob/main/CONTRIBUTING.md>`_.
