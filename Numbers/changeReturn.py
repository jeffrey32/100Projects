#!/usr/bin/python

cost = float(raw_input("Enter a cost: "))
money_given = float(raw_input("Enter how much to hand over: "))

change = money_given  - cost
if money_given < cost:
    print "cheap cunt"

print "Total change is %.2f" % change

fifty = change // .5
left1 = change % .5
twenty = left1 // .2
left2 = left1 % .2
ten = left2 // .1
left3 = left2 % .1
five = left3 // .05
left4 = left3 % .05
print "Here is %d fifty cent coins"% fifty
print "Here is %d twenty cent coins"% twenty  
print "Here is %d ten cent coins"% ten     
print "Here is %d five cent coins"% five    


