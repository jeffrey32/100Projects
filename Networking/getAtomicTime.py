#!/usr/bin/env python

from lxml import etree
import requests
from StringIO import StringIO

source = requests.get("http://www.worldtimeserver.com/current_time_in_AU-VIC.aspx").text
parser = etree.HTMLParser()
tree = etree.parse(StringIO(source), parser)

xpath_time = tree.xpath("//*[@id='analog-digital']/span/text()")
for i in xpath_time:
    a = " ".join(i.split())
    print "Current Atomic AEST time: %s" % a
