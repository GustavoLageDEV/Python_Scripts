#!/usr/bin/env python
# coding: utf-8

# **Change Return Program** - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change. 
# [[Drhealsgood (Python)]](https://github.com/Drhealsgood/miniprojects/blob/master/number_projects/money_changing/money_changing.py) 

def change(cost,payment):
    # Full change value
    change = round(float(payment - cost),2)
    full_dollars = int(change//1)
    # Getting only the cents
    cents = round(change - full_dollars,2)

    #0.25 
    quarters = int(cents//0.25)
    cents = cents - quarters*0.25
    cents = round(cents,2)
    #0.10
    dimes = int(cents//0.1)
    cents = cents -dimes*0.1
    cents = round(cents,2)
    #0.05
    nickels = int(cents//0.05)
    cents -= nickels*0.05
    cents = round(cents,2)
    #0.01
    pennies = int(cents//0.01)
    cents -= pennies*0.01

    print(f"Your change is {change}. {full_dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies.")

if __name__ == "__main__":
    cost = float(input("Please enter the cost: "))
    payment = float(input("Please enter the payment: "))
    change(cost,payment)