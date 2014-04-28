#!/usr/bin/env python

from urllib2 import urlopen

print "Unit Converter.\nFirstly enter type of unit:\t\n1. Temperature\t\n2. Currency\t\n3. Mass\t\n4. Distance"
unit_type = int(raw_input("> "))


if unit_type == 1: #temp
    print "Now choose the starting unit type:\t\n1. Celsius\t\n2. Fahrenheit\t\n3. Kelvin"
    temp_start = int(raw_input("> "))
    print "Now enter the amount." 
    amount = float(raw_input("> "))
    print "And finally enter the scale you wish to convert to:\t\n1. Celsius\t\n2. Fahrenheit\t\n3. Kelvin"
    temp_end = int(raw_input("> "))

    if temp_start == 1 and temp_end == 2:#celsius 2 farenheit
        conversion = (amount * 9/5) + 32
        print "%d degrees Celsius is %.1f degrees Farenheit." % (amount, conversion)

    if temp_start == 1 and temp_end == 3:#celsius 2 kelvin
        conversion = amount + 273.15
        print "%d degrees Celsius is %.1f degrees Kelvin." % (amount, conversion)

    if temp_start == 2 and temp_end == 1:#farenheit 2 celsius
        conversion = (amount - 32) * 5/9
        print "%d degrees Farenheit is %.1f degrees Celsius." % (amount, conversion)

    if temp_start == 2 and temp_end == 3:#farenheit 2 kelvin
        conversion = (amount - 32) * 5/9 + 273.15
        print "%d degrees Farenheit is %.1f degrees Kelvin." % (amount, conversion)

    if temp_start == 3 and temp_end == 1:#kelvin 2 celsius 
        conversion = amount - 273.15
        print "%d degrees Kelvin is %.1f degrees Celsius." % (amount, conversion)

    if temp_start == 3 and temp_end == 2:#kelvin 2 farenheit      
        conversion = (amount - 273.15)  * 9/5 + 32
        print "%d degrees Kelvin is %.2f degrees Farenheit." % (amount, conversion)
    else:
        print "eh?"
#DONE


#"http://www.x-rates.com/table/?from=AUD&amount=1"


if unit_type == 2:#currency
    starting_link = "http://www.x-rates.com/table/?from="
    dollar = raw_input("Enter either \n1. AUD to USD\n2. USD to AUD")
#

if unit_type == 3:#Mass
    print ''


if unit_type == 4:#Distance
    print ''
