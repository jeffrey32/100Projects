#!/usr/bin/env python

print "Simple Calculator \nFirstly enter a number."
num1 = int(raw_input("> "))

print "Now enter either +, -, *, or /"
factor = raw_input("> ")

print "And finally enter a second number."
num2 = int(raw_input("> "))


if factor == '+':
    print num1 + num2
elif factor == '-':
    print num1 - num2
elif factor == '*':
    print num1 * num2
elif factor == '/':
    print float(num1) / num2
