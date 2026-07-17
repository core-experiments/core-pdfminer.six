.. _install:

Install core-pdfminer.six as a Python package
**********************************************

To use core-pdfminer.six for the first time, you need to install the Python
package in your Python environment.

This tutorial requires you to have a system with a working Python and pip
installation. If you don't have one and don't know how to install it, take a
look at `The Hitchhiker's Guide to Python! <https://docs.python-guide.org/>`_.

Install using pip
=================

Run the following command on the commandline to install core-pdfminer.six as a
Python package::

    pip install core-pdfminer.six


Test core-pdfminer.six installation
===================================

You can test the core-pdfminer.six installation by importing it in Python.

Open an interactive Python session and import ``core_pdfminer_six``::

    >>> import core_pdfminer_six
    >>> print(core_pdfminer_six.__version__)  # doctest: +IGNORE_RESULT
    '<installed version>'

Now you can use core-pdfminer.six as a Python package. But core-pdfminer.six also
comes with a couple of useful commandline tools. To test if these tools are
correctly installed, run the following on your commandline::

    $ pdf2txt.py --version
    core-pdfminer.six <installed version>
