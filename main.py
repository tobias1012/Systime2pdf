#!/usr/bin/env python3

from bookWriter import *
from scraper import WebScraper

def main():
    book = BookWriter("test")
    book.saveBook()



if __name__ == "__main__":
    main()
else:
    pass