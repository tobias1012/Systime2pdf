#!/usr/bin/env python3

from bs4 import BeautifulSoup, element #html parser
import requests
import codecs

from toc import TOC
#from page import Page

class Page:
    def __init__(self):
        self.content = str()

    def makePage(self, pdf):
        pdf.set_font("DejaVu", size=12)
        pdf.write_html(self.content)

class WebScraper:
    def __init__(self, domain: str, userid: str, authtoken: str):
        self.cookies = {"ekeys-userid": userid, "myaccount-authtoken": authtoken}
        toc = requests.get(domain, cookies=self.cookies)
        self.sToc= BeautifulSoup(toc.content, "html.parser")
        self.sites = None

    def MakeToc(self):
        title = self.sToc.find("a", "navbar-brand text")
        print(title.text)
        retToc = TOC(title.text)
        levels = self.sToc.find("ul", "level-1")
        li = levels.find_all("li", recursive=False) #lets find every top level TOC entry

        for it in li: #iterate through top level entries
            span = it.find_all("span")
            link = it.find_all("a", href=True)
            retToc[span[0].text] = TOC(span[0].text, link[0]['href']) #Set first to top level because bs4 hacks
            for i in range(1,len(span)): #iterate through sub entries starting from 1
                name = span[i].text
                currentLink = link[i]['href']
                retToc[span[0].text].addEntry(name, currentLink)
                print(name)
            
        self.sites = retToc
        return retToc
    def _siteSubRoutine(self, arr, retArr):
        
        for it in arr:
            tempSite = Page()
            tempSite.content = self._getAndCleanSite(it.link)
            retArr.append(tempSite)

            self._siteSubRoutine(it.sections, retArr)

    def _findImg(self, content):
        if isinstance(content, str):
            return
        for tag in content.children:
            self._findImg(tag)
            if tag.name == "img":
                tag.decompose()
            if tag.name == "td" or tag.name == "tr" or tag.name == "th":
                tag['width'] = 100
            try:
                if tag.name == "div":
                    if "note-handle" == tag["class"][0] or tag["class"][0] == "note-ui":
                        tag.decompose()
            except KeyError:
                pass
            finally:
                pass
            

    def _getAndCleanSite(self, url):
        site = requests.get(url, cookies=self.cookies)
        parsedSite = BeautifulSoup(site.content, "html.parser")

        content = parsedSite.find("div", {"id" : "page-content"})

        self._findImg(content)

        return str(content).encode("latin-1", "replace").decode("latin-1")

    def MakeSites(self):
        if self.sites == None:
            return
        
        retArr = []
        self._siteSubRoutine(self.sites.sections , retArr)

        return retArr
        
    