#!/usr/bin/env python

print "For binary to decial enter 1 \nFor decimal to binary enter 2"
choice = int(raw_input(">"))

if choice == 1:
    print "Binary to Decimal converter."
    binary_number = raw_input("Enter a binary number to convert> ")
    print int(binary_number,2)



if choice == 2:
    print "Decimal to Binary converter."
    dec_number = int(raw_input("Enter a decimal number to convert> "))
    print int(bin(dec_number)[2:])
