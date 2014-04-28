#!/usr/bin/env python

raw = str(raw_input("Enter a string: ")).split()


for i in raw:
    for each_letter in i:
        first = each_letter[0]
        break
    print i[1:] + "-" + first + "ay",
