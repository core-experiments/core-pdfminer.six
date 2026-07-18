.. _tutorial_composable:

Extract text from a PDF using Python - part 2
*********************************************

The command line tools and the high-level API are just shortcuts for often
used combinations of core-pdfminer.six components. You can use these components to
modify core-pdfminer.six to your own needs.

For example, to extract the text from a PDF file and save it in a python
variable::

    from io import StringIO

    from core_pdfminer_six.converter import TextConverter
    from core_pdfminer_six.layout import LAParams
    from core_pdfminer_six.pdfdocument import PDFDocument
    from core_pdfminer_six.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from core_pdfminer_six.pdfpage import PDFPage
    from core_pdfminer_six.pdfparser import PDFParser

    output_string = StringIO()
    with open('tests/fixtures/samples/simple1.pdf', 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    print(output_string.getvalue())
