#!/usr/bin/env python

#usage ./text2html textfile.txt > output.html
import sys
import re

with open(sys.argv[1], 'r') as f:
    for i in f:
        regex = re.findall(r'\w\W',i)
        if regex:
            print "<p>" + str(i) + "</p>"


        

