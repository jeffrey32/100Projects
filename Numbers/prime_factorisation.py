#!/usr/bin/env python
import sys
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

raw = int(raw_input("Enter a number and I will find all prime factors:\n>"))

def factor_finder(n):
    if n%n == 0:
        print 'yes'
    else: print 'no'




factor_finder(raw)



