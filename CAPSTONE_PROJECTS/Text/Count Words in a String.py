#!/usr/bin/env python
# coding: utf-8

# **Count Words in a String** - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary. 
# [[Drhealsgood (Python)]](https://github.com/Drhealsgood/miniprojects/blob/master/text_projects/string_editing.py) 
# [[JLukeC (Python)]](https://github.com/jLukeC/mega-project-list/blob/master/python/count_words.py) 

def countString():

    mystring = input("Type in your string: ")
    return f"This string has a total of {len(mystring.split())} words."

def countText():
    
    txt_file = input("Please input a path to your file: ")
    text = open(txt_file, "r")
    
    str_text= text.read()
    words_text = str_text.split()
    
    return f"This file has a total of {len(words_text)} words."

if __name__ == "__main__":
    while True:
        choice = input("This program will count the amount of words in a string or text file:  1 - String  2 - File.txt ")
        if choice == "1" or choice[0].lower() == "s":
            print(countString())
            break
        elif choice == "2" or choice[0].lower() == "f":
            print(countText())
            break
        else:
            print("Please input: 1 - String  or 2 - File.txt")
            continue
