#!/usr/bin/env python
# coding: utf-8

# **Calculator** - A simple calculator to do basic operators. Make it a scientific calculator for added complexity. 
# [[MrBlaise (Python)]](https://github.com/MrBlaise/learnpython/blob/master/Numbers/calc.py) 

# CLASS TO CALCULATE

class Calculator():

    def __init__(self,last_result=0):
        self.last_result = last_result

    def sum(self,a,b):
        return a + b

    def minus(self,a,b):
        return a - b
        
    def mult(self,a,b):
        return a*b
        
    def div(self,a,b):
        return a/b
        
    def elevate(self,a,b):
        return a**b
        
    def sqroot(self,a):
        return a**0.5
                
#CALCULATOR FOR USER (With option to keep going with last result)

operations = ["+","-","/","*"]
result = ""
on = True
print("Welcome to my calculator app.")
while on:
    if result == "":
        while True:
            try:
                num1 = float(input("Insert a number(use . instead of ,): \n"))
            except:
                print("Input needs to be a number!")
                continue
            break

    op_type = ""
    while op_type not in operations:
        
        op_type = input("Type in the related sign for the desired operation:\nAddition: +\nSubtraction:  -\nDivision: /\nMultiplication: *\n")
        
    while True:
        try:
            num2 = float(input("Insert a number(use . instead of ,): \n"))
        except:
            print("Input needs to be a number!")
            continue
        break

    if op_type == "+":
        result = num1 + num2
    if op_type == "-":
        result = num1 - num2
    if op_type == "/":
        result = num1 / num2
    if op_type == "*":
        result = num1 * num2

    print(f" The result of {num1} {op_type} {num2} is: {result}")

    while True:
        stop = input("Do you want to operate with your last result? Y/N\n")
        if stop[0].upper() == "Y":
            num1 = result
            break
        if stop[0].upper() == "N":
            result = ""
            on = False
            break
        print("Please input Y/N.")