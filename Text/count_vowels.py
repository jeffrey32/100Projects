#!/usr/bin/env python

raw = str(raw_input("Enter a string: ")).lower()

a,e,i,o,u = 0,0,0,0,0

for each_letter in raw:
    if "a" in each_letter:
        a += 1
    if "e" in each_letter:
        e += 1
    if "i" in each_letter:
        i += 1
    if "o" in each_letter:
        o += 1
    if "u" in each_letter:
        u += 1

print "Total vowels:", a+ e + i + o + u
print "A:",a
print "E:",e
print "I:",i
print "O:",o
print "U:",u
