#!/usr/bin/env python
import sys
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

first = str(raw_input("Choose either:\nA: upto a number\nB: the Nth number in the fib series\n> "))
if first == 'A':
    second = int(raw_input("Enter a number to print up to in the Fib series\n>"))
    def fibA(n):    # write Fibonacci series up to n
        """Print a Fibonacci series up to n."""
        a = 0
        b = 1
        while a < n:
            print a,
            a, b = b, a+b
    fibA(second)

elif first == 'B':
    second = int(raw_input("Enter a Nth number to print up to:"))
    def fibB(n):
        """Print to the Nth number"""
        a,b = 0,1
        for i in range(second):
            print a,
            a,b = b, a+b
    fibB(second)

else: print 'thats not an option.... quiting'






