#!/usr/bin/env python3

from fpdf import FPDF, HTMLMixin

from scraper import WebScraper
from toc import TOC

class MyFPDF(FPDF, HTMLMixin):
    pass

class BookWriter:
    def __init__(self, fileName: str, domain: str, userid: str, authtoken: str ):
        self.w = WebScraper(domain, userid, authtoken)
        self.tableOfContents = self.w.MakeToc()
        self.pages = self.w.MakeSites()
        self._fileName = fileName
    def saveBook(self):
        pdf = MyFPDF()
        pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
        self.tableOfContents.createPage(pdf)
        pdf.add_page()
        for it in self.pages:
            it.makePage(pdf)

        #Save pdf
        pdf.output(self._fileName)