.. _faq:

Frequently asked questions
**************************

Why is it called core-pdfminer.six?
===================================

Core-pdfminer.six is a performance-focused fork of pdfminer.six. The ``core``
prefix identifies this distribution and its ``core_pdfminer_six`` Python
namespace, while the rest of the name acknowledges its upstream foundation.

The upstream pdfminer.six project is itself a fork of the `original pdfminer
created by Euske <https://github.com/euske>`_. Its ``.six`` suffix originally
referred to the ``six`` compatibility package used to support both Python 2 and
Python 3.

The current punchline "We fathom PDF" is a `whimsical reference
<https://github.com/pdfminer/pdfminer.six/issues/197#issuecomment-655091942>`_
to the six. Fathom means both deeply understanding something, and a fathom is
also equal to six feet.

How does core-pdfminer.six compare to other forks of pdfminer?
==============================================================

Core-pdfminer.six keeps the familiar architecture of pdfminer.six but develops
its internals independently, with an emphasis on throughput, memory use, and
scalability. Its import namespace is ``core_pdfminer_six`` so it can coexist
with upstream pdfminer.six in the same environment.

Why are there `(cid:x)` values in the textual output?
=====================================================

One of the most common issues with core-pdfminer.six is that the textual output
contains raw character id's `(cid:x)`. This is often experienced as confusing
because the text is shown fine in a PDF viewer and other text from the same
PDF is extracted properly.

The underlying problem is that a PDF has two different representations
of each character. Each character is mapped to a glyph that determines
how the character is shown in a PDF viewer. And each character is also
mapped to its unicode value that is used when copy-pasting the character.
Some PDF's have incomplete unicode mappings and therefore it is impossible
to convert the character to unicode. In these cases core-pdfminer.six defaults
to showing the raw character id `(cid:x)`

A quick test to see if core-pdfminer.six should be able to do better is to
copy-paste the text from a PDF viewer to a text editor. If the result
is proper text, core-pdfminer.six should also be able to extract proper text.
If the result is gibberish, core-pdfminer.six will also not be able to convert
the characters to unicode.

References:

#. `Chapter 5: Text, PDF Reference 1.7 <https://opensource.adobe.com/dc-acrobat-sdk-docs/pdflsdk/index.html#pdf-reference>`_
#. `Text: PDF, Wikipedia <https://en.wikipedia.org/wiki/PDF#Text>`_
