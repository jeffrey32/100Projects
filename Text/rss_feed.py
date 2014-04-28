#!/usr/bin/env python

import requests
import re
from lxml import etree
import StringIO
import chardet

def get_feed(url):
    source = requests.get(url).text
    root = etree.fromstring(source)
    parser = etree.XMLParser()
    tree = etree.parse(StringIO.StringIO(source),parser)

#    parser = etree.HTMLParser()
#    tree = etree.fromstring(source, parser)
#    tree = etree.parse(StringIO.StringIO(source), parser)




    xpath_link = tree.xpath("//channel/item/link/text()")
    xpath_title = tree.xpath("//channel/item/title/text()")
    xpath_desc = tree.xpath("//channel/item/description/text()")

    print xpath_link
    print xpath_title
    print xpath_desc


#    for i in xpath_link:
#        print i,
#    print "\n"

#    for i in xpath_title:
#        print i





if __name__ == '__main__':
    get_feed("http://krebsonsecurity.com/feed/")

