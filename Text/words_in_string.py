#!/usr/bin/python

raw = str(raw_input("Enter sentance: ")).lstrip().rstrip()

counter = 1
for i in raw:
    if " " == i:
        counter +=1
    
print "Number of words: %d " % counter
