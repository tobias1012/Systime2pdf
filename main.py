#!/usr/bin/env python3

from bookWriter import *
from scraper import WebScraper
from sys import argv

def main():
    book = BookWriter(argv[1], argv[2], argv[3], argv[4])
    book.saveBook()



if __name__ == "__main__":
    if len(argv) != 4:
        print("""Usage:
        main.py <out> <tocsite> <userId> <authtoken>
        """)
    main()
else:
    pass