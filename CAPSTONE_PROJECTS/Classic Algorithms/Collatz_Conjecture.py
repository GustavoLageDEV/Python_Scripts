#!/usr/bin/env python
# coding: utf-8

# **Collatz Conjecture** - Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process: If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1. 
# [[EpicDavi (Python)]](https://github.com/EpicDavi/RandomProjects/blob/master/Language%20Challenge%20Stuff/CollatzRecursive.py)
# [[rramchand (Java)]](https://github.com/rramchand/Projects-Solutions/blob/master/Collatz.java) 
# [[petehuang (Ruby)]](https://github.com/petehuang/Projects/blob/master/Classic%20Algorithms/collatz.rb) 
# [[quitrk (JavaScript)]](https://github.com/quitrk/LearningJS/blob/master/Classic%20Algorithms/00.%20Collatz%20Conjecture.js) 
# [[taycaldwell (Java)]](https://github.com/taycaldwell/Projects/blob/master/Classic%20Algorithms/collatz.java) 
# [[anggiaj (Go)]](https://github.com/anggiaj/Projects/blob/master/Classic%20Algorithms/collatz.go) 
# [[edeng (Java)]](https://github.com/edeng/Problems/blob/master/Collatz.java)
# [[luisccastillo (C#)]](https://github.com/luisccastillo/Projects/blob/master/Classic%20Algorithms/collatz_cojecture.cs) 
# [[vdrey (Python)]](https://github.com/vdrey/Project-Programs/blob/master/Python/Collatz.py) 
# [[francis36012 (Python)]](https://github.com/francis36012/karan-projects/blob/master/src/classic_algorithms/collatz.py) 
# [[kingballer29 (C++)]](https://github.com/kingballer29/Programming/blob/master/collatzConjecture.cpp)
# [[manateemilitia (Java)]](https://github.com/manateemilitia/CollatzJava/blob/master/CollatzJava/src/collatzjava/CollatzJava.java) 
# [[viktorahlstrom (Python)]](https://github.com/viktorahlstrom/pythonscripts/blob/master/collatz_conjecture.py)

def input_num():
    while True:
        try:
            num = int(input("Please input an integer number greater than 1: "))
        except:
            print("That's not an integer.")
            continue
        if num <= 1:
            print("Integer must be greater than 1.")
            continue
            
        return num

def isodd_even(num):

    if num % 2 == 1:
        return num*3 + 1
    if num % 2 == 0:
        return num/2
    else:
        return num
 
def collatz():

    print("Welcome to Collatz conjucture: ")
    num = input_num()
    og_num = num
    count = 0
    
    while True:

        new_num = int(isodd_even(num))
        count += 1
        
        print(f" Step {count}: {num} to {new_num} ")
        num = new_num
        
        if num == 1:
            break

    print(f"The number {og_num} takes {count} steps to reach 1 by Collatz Conjecture.")
