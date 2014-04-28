#!/usr/bin/env python

print "----Perfect Number Checker----"
raw = int(raw_input("Enter a number to check upto(under 30k or slooow): ")) +1
print "Finding perfect numbers up to %d" % (raw -1)


def perfect_number_check(range_seq): # 30000 checks time = real    0m24.420s
    for i in range_seq: # 1-3000
        count = 0
        perfect_number = i
        perfect_number_plus1 = i + 1
        for j in range(1,perfect_number_plus1):
            if perfect_number_plus1 % j == 0:
                count += j
                if count > perfect_number_plus1: # saves time(~10%) by breaking out of loop if count > perfect number already
                    break
        if count == perfect_number_plus1:
            print str(count) + " is a perfect number."

perfect_number_check(range(1,raw))
