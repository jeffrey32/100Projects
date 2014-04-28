#!/usr/bin/env python

import math

start = 1
print 'The first prime number is: %d' % start
print 'Push enter to keep seeing more primes'
print 'Push Ctrl+c to exit'


def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return True;

print 2

for n in range(3, 5555555):
    if isPrime(n):
        enter = str(raw_input())
        if enter == "":
            print n
