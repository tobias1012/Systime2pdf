#!/usr/bin/env python3

from fpdf import FPDF

from scraper import WebScraper
from toc import TOC

class BookWriter:
    def __init__(self, name: str):
        self.w = WebScraper("https://sprogdansk.systime.dk/index.php?id=frontpage&cmd=toc")
        self.tableOfContents = self.w.MakeToc()
        self.pages = []
    def saveBook(self):
        pdf = FPDF()
        pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
        self.tableOfContents.createPage(pdf)


        #Save pdf
        pdf.output("file.pdf")