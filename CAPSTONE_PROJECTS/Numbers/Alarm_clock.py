#!/usr/bin/env python
# coding: utf-8

# **Alarm Clock** - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time. 
# [[smthc (Python)]](https://github.com/smthc/mini_projects/blob/master/alarm.py) 

# perguntar se quer um cronometro ou um despertador para um determinado horario
# 
# 1- para cronometro = timer
# 
# 2- despertador = alarm
# 
# 1 - para testes, limitar a 60 minutos.
#     min = perguntar minutos (caso queira apenas segundos digite 0 nesse campo)
#     seg = perguntar segundos
# 
#     tempo_despertar = tempo_atual/real do ultimo input + (tempo_total_input = min+seg)
# 
#     tempo_atual == tempo_despertar ---> tocar um som
# 
# 2 - para testes, limitar ao dia atual.
#     hora = perguntar a hora do despertador (formato 24h)
#     min = perguntar os minutos do despertador (se quiser hora fechada, digitar 0)
# 
#     tempo_despertar = dia atual/hora/min
# 
#     tempo_atual == tempo_despertar ---> tocar um som

import datetime, time
from playsound import playsound

def timer_or_alarm():
    
    while True:
        choice = input("Type 1 for Timer, or 2 for Alarm")
        if choice not in ["1","2"]:
            print("Invalid input.")
            continue
        else:
            break

    return int(choice)
        

def input_time(x):

    if x == 1:
        print("This is the timer feature:\n")
        while True:
            try:
                min = int(input("How many minutes? "))
                sec = int(input("How many seconds? "))
            except:
                print("Invalid, please input an integer.")
                continue
            return min*60 + sec

    else:
        print("This is the alarm feature:\n")
        while True:
            try:
                hour = int(input("Type in what hour: 0-23"))
                min = int(input("Type in what minute: "))
            except:
                print("Invalid, please input an integer.")
                continue
            return (hour,min)

def timer(i_time):

    print(f"Timer was set to: {i_time//60} minutes and {i_time%60}")
    time.sleep(i_time)

    playsound(r"C:\Users\Gustavo Lage\Desktop\protagma_ark.wav")

def alarm(i_time):
    if i_time[0] < 10:   
        hour = "0"+str(i_time[0])
    else:
        hour = str(i_time[0])

    if i_time[1] < 10:   
        min = "0"+str(i_time[1])
    else:
        min = str(i_time[1])
        
    target_time = f"{hour}:{min}:00.000000"
    print(f"Alarm was set to: {target_time[:8]}")
    while True:
        rn = str(datetime.datetime.today().time())
        if rn >= target_time:
            playsound(r"C:\Users\Gustavo Lage\Desktop\protagma_ark.wav")
            break
        else:
            pass
        
if __name__ == "__main__":
    choice = timer_or_alarm()
    i_time = input_time(choice)

    if choice == 1:
        timer(i_time)
    else:
        alarm(i_time)

import datetime, time
from playsound import playsound

def timer_or_alarm():
    
    while True:
        choice = input("Type 1 for Timer, or 2 for Alarm")
        if choice not in ["1","2"]:
            print("Invalid input.")
            continue
        else:
            break

    return int(choice)
        

def input_time(x):

    if x == 1:
        print("This is the timer feature:\n")
        while True:
            try:
                min = int(input("How many minutes? "))
                sec = int(input("How many seconds? "))
            except:
                print("Invalid, please input an integer.")
                continue
            return min*60 + sec

    else:
        print("This is the alarm feature:\n")
        while True:
            try:
                hour = int(input("Type in what hour: 0-23"))
                min = int(input("Type in what minute: "))
            except:
                print("Invalid, please input an integer.")
                continue
            return (hour,min)

def timer(i_time):

    print(f"Timer was set to: {i_time//60} minutes and {i_time%60}")
    time.sleep(i_time)

    playsound(r"C:\Users\Gustavo Lage\Desktop\protagma_ark.wav")

def alarm(i_time):
    
    hour = i_time[0]
    min = i_time[1]
        
    target_time = f"{hour}:{min}:00.000000"
    print(f"Alarm was set to: {target_time[:8]}")
    
    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(),datetime.time(hour,min,0))

    time.sleep((alarm_time - now).total_seconds())

    playsound(r"C:\Users\Gustavo Lage\Desktop\protagma_ark.wav")
   
if __name__ == "__main__":
    choice = timer_or_alarm()
    i_time = input_time(choice)

    if choice == 1:
        timer(i_time)
    else:
        alarm(i_time)
