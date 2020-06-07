#!/usr/bin/env python3

from fpdf import FPDF



class TOC:    
    def __init__(self, name, link = str()):
        self.line = 1
        self.name = name
        self.link = link
        self.sections = []
    def addEntry(self, name: str, link: str):
        if(name in self.sections):
            pass
        self.sections.append(TOC(name, link = link))

    def _createSection(self, size: float, arr, pdf):
        arr.append(self.name)

        #add to pdf
        pdf.set_font("DejaVu", size=size)
        pdf.cell(200, 10, txt=self.name, ln=self.line, align="C")
        self.line += 1
        for it in self.sections:
            arr.append(it._createSection(size -5, arr, pdf))
        return arr


    def createPage(self, pdf: FPDF): #create a pdf page
        size = 25
        arr = []
        pdf.add_page()
        text = self._createSection(size, arr, pdf)
        
    def __getitem__(self, id: str):
        ret = [item for item in self.sections if item.name == id] # Get list of all with the right name
        return ret[0]

    def __setitem__(self, index: str, obj):
        self.sections.append(obj)
    def __str__(self):
        return self.name

                
if __name__ == "__main__":
    print("This shoulnd't be run as main")
