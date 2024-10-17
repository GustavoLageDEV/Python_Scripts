#!/usr/bin/env python
# coding: utf-8

# **Credit Card Validator** - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discover) and validates it to make sure that it is a valid number (look into how credit cards use a checksum). [[desertwebdesigns (Python)]](https://bitbucket.org/desertwebdesigns/learn_python/src/master/Numbers/credit_card.py) [[dotslash (Python)]](https://github.com/dotslash/Projects/blob/master/solutions/credit_card_validator.py) [[Barvin (Python)]](https://github.com/Barvin/CodeWars-ByArvin/blob/master/TheLuhnAlgorithm.py) 

# #### Web Scrapping a site for CC Numbers and Types

# ##### Test Credit Card Account Numbers
# (https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm)

# In[3]:


import requests
import bs4
import re

# Web scrapping
test_numbers_url = "https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm"
result = requests.get(test_numbers_url)
soup = bs4.BeautifulSoup(result.text,"lxml")

# Found where numbers and types are in the HTML
soup_types = soup.select(".whs4")
soup_numbers = soup.select(".whs5")
# Creating lists with the numbers and types
cc_types = []
cc_numbers = []

for type in soup_types:
    cc_types.append(type.getText()[1:])   

for num in soup_numbers:
    cc_numbers.append(num.getText()[1:])

# Formating number list using "re", so it cotains only integers (being the definition in index[0])
index = 0
for num in cc_numbers:
    if re.findall(r"\d+",num) != []:
        cc_numbers[index] = int(re.findall(r"\d+",num)[0])
    index += 1 
    
# Creating a Dictionary to relate the lists
cc_dict = dict(zip(cc_numbers,cc_types))

# ##### Luhn test
# (https://www.groundlabs.com/blog/anatomy-of-a-credit-card/)

# CHECKING A LIST OF TEST CC NUMBERS

for cc_num in cc_numbers[1:]:
    
    card_number = cc_num
    str_card_number = str(card_number)
    number_list = []
    new_str = ""
    
    # IF NUMBER IS ODD, START COUNT = 1
    if len(str_card_number) % 2 == 0:
        count = 0
    else:
        count = 1
    
    # TURNS INTO A LIST 
    for num in str_card_number:
        number_list.append(num)
    
    # CHANGES THE LIST, MULTIPLYING EVERY OTHER VALUE x2 (BASED ON LUHN TEST)
    for num in number_list[count::2]:
        number_list[count] = str(int(num)*2)
        count += 2 
        
    # TURNS INTO A STRING, THIS WAY TRANSFORMING TWO DIGIT NUMBERS INTO 2 ONE DIGIT NUMBERS (BASED ON LUHN TEST)
    for num in number_list:
        new_str += num
    
    # TURNING THE NEW STR (WITH UPDATED VALUES) INTO A LIST, FOR THE SUM 
    number_list = []
    for num in new_str:
        number_list.append(int(num))
    
    soma = sum(number_list)
    if soma % 10 == 0:
        print(f"{cc_num} is a valid credit card number from {cc_dict[cc_num]}.\n")
    else:
        print(f"{cc_num} is an invalid credit card number, be careful!\n")

# GET CARD NUMBER FROM USER
while True:
    try:
        card_number = int(input("Enter de CC number to validate"))
    except:
        print("That's not a number!")
        continue
    if len(str(card_number)) not in range(10,20):
        print("Number must have between 10 to 19 digits.")
        continue
    break
str_card_number = str(card_number)
number_list = []
new_str = ""
    
# IF NUMBER IS ODD, START COUNT = 1
if len(str_card_number) % 2 == 0:
    count = 0
else:
    count = 1
    
# TURNS INTO A LIST 
for num in str_card_number:
    number_list.append(num)
    
# CHANGES THE LIST, MULTIPLYING EVERY OTHER VALUE x2 (BASED ON LUHN TEST)
for num in number_list[count::2]:
    number_list[count] = str(int(num)*2)
    count += 2 
        
# TURNS INTO A STRING, THIS WAY TRANSFORMING TWO DIGIT NUMBERS INTO 2 ONE DIGIT NUMBERS (BASED ON LUHN TEST)
for num in number_list:
    new_str += num
    
# TURNING THE NEW STR (WITH UPDATED VALUES) INTO A LIST, FOR THE SUM 
number_list = []
for num in new_str:
    number_list.append(int(num))
    
soma = sum(number_list)
if soma % 10 == 0:
    print(f"{card_number} is a valid credit card number.\n")
else:
    print(f"{card_number} is an invalid credit card number, be careful!\n")
