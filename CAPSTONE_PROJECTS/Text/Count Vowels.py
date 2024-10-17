#!/usr/bin/env python
# coding: utf-8

# **Count Vowels** - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found. 
# [[Drhealsgood (Python)]](https://github.com/Drhealsgood/miniprojects/blob/master/text_projects/string_editing.py) 
# [[JLukeC (Python)]](https://github.com/jLukeC/mega-project-list/blob/master/python/count_vowels.py) 

text = str(input("Please insert a string, I'll count the number of vowels in it for you: ")).lower()
vowels = ("a","e","i","o","u")
total_vowels = 0
for car in text:
    if car in vowels:
        total_vowels += 1

print(f"Total of vowels is {total_vowels}.")
print(f"A = {text.count("a")}")
print(f"E = {text.count("e")}")
print(f"I = {text.count("i")}")
print(f"O = {text.count("o")}")
print(f"U = {text.count("u")}")
