#!/usr/bin/env python
# coding: utf-8

# **Fizz Buzz** - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
# [[sethlugibihl (Python)]](https://github.com/sethlugibihl/Python-Solutions/blob/master/FizzBuzz.py)
# [[korabum (Python)]](https://github.com/korabum/Projects/blob/master/Text/fizzbuzz.py)

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)