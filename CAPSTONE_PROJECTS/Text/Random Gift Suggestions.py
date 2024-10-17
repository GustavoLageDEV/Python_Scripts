#!/usr/bin/env python
# coding: utf-8

# **Random Gift Suggestions** - Enter various gifts for certain people when you think of them. When its time to give them a gift (xmas, birthday, anniversary) it will randomly pick one. *Optional: Suggest places you can get it (link to Amazon page?).*

import random as r
import requests, bs4

database = {"alice":["Viagem","Iphone","Batata"],"pai":["camisa cruzeiro","relogio", "cerveja"],
             "mae":["Plantas","Perfume","vasos"],"bartolomeu":["Osso para cachorro","Petiscos cachorro","Roupa canina"]}
def gift_to():
    while True:
        person = input("Who are we going to gift: ")
        if person.lower() not in database:
            print("This person is not on our database")
            continue
        else:
             return person   

def search_gift(gift): # WEB SCRAPING A GOOGLE SERP FOR THE FIRST 3 ORGANIC RESULTS, SO WE CAN SUGGEST (WORKING IN PROGRESS)

    research = requests.get(f"https://www.google.com/search?gl=us&q={gift}")
    soup = bs4.BeautifulSoup(research.text,"lxml")
    
    pass

if __name__ == "__main__":
    
    person = gift_to() 
    g_list = database[person]
    gift = g_list[r.randint(1,len(g_list))-1]

    print(f"We think {person.capitalize()} would love {gift} as a gift")
