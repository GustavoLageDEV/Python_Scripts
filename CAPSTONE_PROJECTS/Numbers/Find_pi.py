#!/usr/bin/env python
# coding: utf-8

# **Find PI to the Nth Digit** - Enter a number and have the program generate &pi; (pi) up to that many decimal places. Keep a limit to how far the program will go.
# MY FIRST TRY DOING (but I did not generate pi)

from math import pi
import decimal as d

pi_updated= d.Decimal(pi)
pi_string = str(pi_updated)

while True: 
    try:
        decimal_digit = int(input("Please insert how many decimal places should pi be generated: Min = 2 Máx = 48 "))
        if decimal_digit not in range(2,49):
            print("Invalid number. Min = 2 Máx = 48")
            continue
    except:
        print("Sorry, thats not a number. Try again.")
        continue
    break

print(f" Here is your pi: {pi_string[:(decimal_digit+2)]}")

#SECOND TRY (this time I did generate, but did not know how to make more than 48 decimal places)

import math
import decimal as d
from decimal import *
getcontext().prec = 100

def calculo_pi():

    k = 10000
    pi_bbp = 0               
    for k in range(k):
        pi_bbp += (1/(16**k)) * ((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6)))
    return pi_bbp

def valid_digit_input():
    while True: 
        try:
            decimal_digit = int(input("Please insert how many decimal places should pi be generated: Min = 2 Máx = 48 "))
            if decimal_digit not in range(2,49):
                print("Invalid number. Min = 2 Máx = 48")
                continue
        except:
            print("Sorry, thats not a number. Try again.")
            continue
        return decimal_digit
   
pi_updated= d.Decimal(calculo_pi())
pi_string = str(pi_updated)
decimal_digit = valid_digit_input()

print(f" Here is your pi: {pi_string[:(decimal_digit+2)]}")

