#!/usr/bin/env python
# coding: utf-8

# **Binary to Decimal and Back Converter** - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent. 
# [[Drhealsgood (Python)]](https://github.com/Drhealsgood/miniprojects/blob/master/number_projects/conversion/conversions.py) 

def choice():
    while True:
        choice = input("Welcome.\nType 1 to convert Decimal to a Binary: \nType 2 to convert a Binary to a Decimal: ")
        if choice in ["1","2"]:
            return choice
        else:
            print("Invalid input.")
            continue

def bin_to_dec(str_num):

    num_list = []
    for num in str_num:
        num_list.append(int(num))

    sum = 0
    count = 0
    for num in num_list[::-1]:
        if num == True:
            sum += 2**count
        count += 1

    return sum

def dec_to_bin(num):
    bin_str = ""
    while True:
        
        bin_str += str(num%2)
        num = num//2
        
        if num == 1:
            bin_str += "1"
            while len(bin_str) % 4 != 0:
                bin_str += "0"
            return bin_str[::-1]
        if num == 0:
            bin_str += "0"
            while len(bin_str) % 4 != 0:
                bin_str += "0"
            return bin_str[::-1]

if __name__ == "__main__":
    choice = choice()
    if choice == "1":
        while True:
            try:
                number = int(input("Type in a number to convert from Decimal to Binary: "))
            except:
                print("Please type in an integer.")
                continue
            break
        print(f"The Decimal number {number} is equal to {dec_to_bin(number)} in Binary.")

    if choice == "2":
        bin = False
        while bin == False:
                number = str(input("Type in a number to convert from Binary to Decimal: "))
                for digit in number:
                    if digit not in ["0","1"]:
                        print("This is not a binary number, please try again.")
                        bin = False
                        break
                    else:
                        bin = True

        print(f"\nThe Binary number {number} is equal to {bin_to_dec(number)} in Decimal.")