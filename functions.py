"""
Needed functions for main
"""
from os import system, name
from time import sleep
import random as random

DEC = "-------------------------------------------------"
###########################################################
# System functions
###########################################################
def status(user):
    #pull all user stats into a string
    status = str(user.__dict__)
    #Print it nicely, multi-lined
    print(status.replace(",", "\n").strip("{").strip("}"))
    
def level_up(user):
    print(DEC)
    print("You have gained a level!")
    user.lvl += 1
    print("You are now level {}".format(user.lvl))
    print(DEC)
    status(user)
    print(DEC, "\n")
    
def clear(time):
    sleep(time)
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

###########################################################
# Game core functions
###########################################################
def travel_map(map_number, desc_number, dungeon):
    i = 0 #counter
    y = 0
    #Loop until correct steps # >= length of map
    while i <= len(map_number):
        choice = input("What do you do?\n")
        #Incorrect choice, plus random encounter chance
        if map_number[i] not in choice:
            print("Cannot {}, please try again.\n".format(choice))
            random_encounter()
        #Correct answer + random encounter chance
        else:
            clear(0)
            print(desc_number[i])
            i += 1
            random_encounter()
        #if correct choice counter equals map size, you win
        if i == len(map_number):
            print("Congratulations, Dungeon {} complete!".format(dungeon))
            break

def random_encounter():
    #chance of encounter - random number between 1-100
    chance = random.randrange(1, 100)
    if chance < 75: # 25% chance of encounter
        pass
    else:
        print("Monster Encounter!!!")

def achievement(user, exp, message):
    print(DEC)
    #Show amount earned
    print("You have gained +{} experience! - {}".format(exp, message))
    #Add to total
    user.exp += exp
    #Display total
    print("Total Experience: {}".format(user.exp))
