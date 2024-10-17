#!/usr/bin/env python
# coding: utf-8

# **Coin Flip Simulation** - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads. 
# [[scottdchris (Python)]](https://github.com/scottdchris/CoinFlip)  
# [[dsub15 (Python)]](https://github.com/dsub15/Projects/blob/master/Coin_flip.py)
# [[mandeepbhutani (Python)]](https://github.com/mandeepbhutani/Sample-Projects/blob/master/CoinFlip.py) 

# FIRST TRY

import random 

def coin_flip():

    coin = random.randint(0,1)

    return coin
    
def shell():
    count_heads = 0
    count_tails = 0
    round = 1

    while True:
        try:
            n = int(input("Hey, please insert how many times you want to flip the coin: "))
        except:
            print("Please insert an integer number: ")
            continue
        break
        
    for x in range(n):
       
        if coin_flip() == 0:
            print(f"\nRound {round}: Heads!")
            count_heads += 1
        else:
            print(f"\nRound {round}: Tails!")
            count_tails += 1
        round +=1

    print(f"\nHeads flipped: {count_heads}")
    print(f"Tails flipped: {count_tails}")

if __name__ == "__main__":
    shell()

# SECOND TRY

import random 

class Heads_Tails():
    
    def __init__(self):
        self.heads = 0
        self.tails = 0
        self.historic = {}

    def add_round(self, round, result):

        self.historic[round] = result

        if result.lower() == "head":
            self.heads += 1
        else:
            self.tails += 1 

    def round(self, n):

        print(f"The flip on round {n} was {self.historic[n]}")

    def __str__(self):

        for round, result in self.historic.items():
            print(f"Round {round}: {result}")
        return ""

def coin_flip():

    coin = random.randint(0,1)
    if coin == 0:
        return "Head"
    else:
        return "Tail"
    
if __name__ == "__main__":
    historic = Heads_Tails()
    round = 1
    on = True
    while True:
        try:
            total_rounds = int(input("Hey, please insert how many times you want to flip the coin: "))
        except:
            print("Please insert a number: ")
            continue
        break
            
    for x in range(total_rounds):
        result = coin_flip()
        historic.add_round(round,result)
        round +=1
        
print(f"\nHeads flipped: {historic.heads}")
print(f"\nTails flipped: {historic.tails}")
