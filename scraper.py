#!/usr/bin/env python3

from bs4 import BeautifulSoup #html parser
import requests
import codecs

from toc import TOC

class WebScraper:
    def __init__(self, domain):
        self.cookies = {}
        toc = requests.get(domain, cookies=self.cookies)
        self.sToc= BeautifulSoup(toc.content, "html.parser")

    def MakeToc(self):
        title = self.sToc.find("a", "navbar-brand text")
        print(title.text)
        retToc = TOC(title.text)
        levels = self.sToc.find("ul", "level-1")
        li = levels.find_all("li", recursive=False) #lets find every top level TOC entry

        for it in li: #iterate through top level entries
            span = it.find_all("span")
            retToc[span[0].text] = TOC(span[0].text) #Set first to top level because bs4 hacks
            for i in range(1,len(span)): #iterate through sub entries starting from 1
                name = span[i].text
                retToc[span[0].text].addEntry(name)
                print(name)
            

        return retToc