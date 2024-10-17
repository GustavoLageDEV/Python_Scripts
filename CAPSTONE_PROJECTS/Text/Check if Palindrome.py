#!/usr/bin/env python
# coding: utf-8

# **Check if Palindrome** - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar” 
# [[Drhealsgood (Python)]](https://github.com/Drhealsgood/miniprojects/blob/master/text_projects/string_editing.py) 
# [[JLukeC (Python)]](https://github.com/jLukeC/mega-project-list/blob/master/python/palindrome.py) 


mystring = str(input("Please insert a string to check for Palindrome: ")).lower()
clean_string = []
for char in mystring:
    if char.isalpha():
        clean_string.append(char)

clean_string = "".join(clean_string)
mystring = clean_string.lower()

if mystring == mystring[::-1]:
    print("This is a palindrome\n")
else:
    print("Not a palindrome\n")
    
print(mystring)
print(mystring[::-1])