#!/usr/bin/env python

raw = str(raw_input("Enter a string: ")).lower()
ord_forward = ""
ord_backward = ""


for i in raw:
    ord_forward += str(ord(i))
    ord_backward += str(ord(i))[::-1]


if ord_forward == ord_backward[::-1]:
    print "Yes %s tis a palindrome" % raw
else:
    print "This no fucking palindrome!"

