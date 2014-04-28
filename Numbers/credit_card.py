#!/usr/bin/env python


print "Real:", "4417123456789113"
print "Fake:", "1122334455667788"
raw = str(raw_input("Enter 16 digit CC number: ")).replace(" ", "")
if len(raw) != 16:
    print "Not 16 digits - quitting"
    exit(0)

###  Luhn Algorithm ###
x2 = []
x3 = []


def times2_step1(ccnumber):
    for i in ccnumber[::2]:
        x2.append(int(i) * 2)
    print x2

def add_step2(ccnumber):
    for i in ccnumber[1::2]:
        x3.append(int(i))
    print x3
    
def add2lists(l1,l2):
    for i in l1,l2:
        if len(i) > 1:
            list(''.join(map(str, l1)))
            



def main():
    times2_step1(raw)
    add_step2(raw)
    add2lists(x2,x3)
    split_digits(x2)
if __name__ == "__main__":
    main()


