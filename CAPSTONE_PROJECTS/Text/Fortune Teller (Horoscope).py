#!/usr/bin/env python
# coding: utf-8

# **Fortune Teller (Horoscope)** - A program that checks your horoscope on various astrology sites and puts them together for you each day. 
# [[cahitonur (Python)]](https://github.com/cahitonur/mini-project/blob/master/horoscope/horoscope.py) 
# [[tapasweni-pathak (Python)]](https://github.com/tapasweni-pathak/Scripts/blob/master/Your-Horoscope.py) 

from IPython.display import clear_output
import requests, bs4, datetime

zodiac_signs={1:"Aries",2:"Taurus",3:"Gemini",4:"Cancer",5:"Leo",6:"Virgo",7:"Libra",8:"Scorpio",9:"Sagittarius",10:"Capricorn",11:"Aquarius",12:"Pisces"}

date_to_signs={ "Aries": "March 21 – April 19",
"Taurus" : "April 20 – May 20",
"Gemini": "May 21 – June 21",
"Cancer": "June 22 – July 22",
"Leo": "July 23 – August 22",
"Virgo": "August 23 – September 22",
"Libra": "September 23 – October 23",
"Scorpio": "October 24 – November 21",
"Sagittarius": "November 22 – December 21",
"Capricorn": "December 22 – January 19",
"Aquarius": "January 20 – February 18",
"Pisces": "February 19 – March 20"
}

today = datetime.date.today()
today_str = f"{today.strftime("%B")} {today.day}, {today.year}"

def display_signs():
    count = 1
    for sign, date in date_to_signs.items():
        print(f"{count}: {sign} ({date})")
        count += 1 

def request(url):
    res = requests.get(url)
    return bs4.BeautifulSoup(res.text,"lxml")

while True:
    display_signs()
    try:
        user_sign_id = int(input("\nChoose a number corresponding to your zodiac sign:"))
        clear_output()
        if user_sign_id in zodiac_signs.keys():
            user_sign = zodiac_signs[user_sign_id]
            print(f"{user_sign} was chosen.\n")
            break
        else:
            print("There is not a zodiac sign related to this number, try again.\n")
            continue
    except:
        clear_output()
        print("Incorrect input, try again.\n")

print(f"Here are 3 daily horoscopes from different sources for today ({today_str}): \n")

url_horoscope = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={user_sign_id}"
soup1 = request(url_horoscope)
daily_horoscope1 = soup1.select(".main-horoscope>p")[0].text

print(daily_horoscope1)
print(f"\nSource: {url_horoscope}\n")

url_astrology = f"https://www.astrology.com/horoscope/daily/{user_sign.lower()}.html"
soup2 = request(url_astrology)
daily_horoscope2 = soup2.select("#content>p")[0].text

print(daily_horoscope2)
print(f"\nSource: {url_astrology}\n")

url_vogue = f"https://www.vogue.in/horoscope/product/{user_sign}-horoscope-today-{today.strftime("%B")}-{today.day}-{today.year}/"
soup3 = request(url_vogue)
daily_horoscope3 = soup3.select(".description.mb-20 span")[0].text

print(daily_horoscope3)
print(f"\nSource: {url_vogue}")