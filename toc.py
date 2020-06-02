from pdfWriter import pdf


class TOC:    
    def __init__(self):
        self.entry = dict()
    def addEntry(self, name: str):
        if name not in self.entry.keys():
            self.entry[name] = []

    def addSubEntry(self, entry: str, subName: str):
        if entry not in self.entry.keys():
            pass
        self.entry[entry].append(subName)
    def createPage(self, pdffile: pdf) -> int:
        for it in self.entry.keys():
            for jt in self.entry[it]:
                pass


                
