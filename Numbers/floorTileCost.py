#!/usr/bin/env python


tiles = 12.45
print "These tiles cost $12.45 per meter"
width = int(raw_input("Enter width of room in meters> "))
height = int(raw_input("Enter height of room in meters> "))
area = float(width) * float(height)
print type(area)
print "You have a floor area of %d" % area
spending_limit = int(raw_input("Enter how much you want to spend in dollars> "))


def calculate_cost(width,height):


    afford = (spending_limit / area) * 100
    if area <= spending_limit:
        print "With your limit of $%d, you can cover all %d square meters" %(spending_limit, area)
    else:
        print "With your limit of $%d, you can only cover %d percent of your %d square meters" %(spending_limit,afford ,area)

calculate_cost(width,height)
