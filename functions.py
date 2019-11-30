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
    print(status.replace(",", "\n").strip("{").strip("}"), "\n")
    
def level_up(user):
    print(DEC)
    print("You have gained a level!")
    user.lvl += 1
    print("You are now level {}".format(user.lvl))
    print(DEC)
    incrementing_stats = ['health', 'attack']
    for stat in user.__dict__:
        if stat in incrementing_stats:
            stat *= user.lvl
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
            if random_encounter() == 0:
                pass
                
            else:
                pass
                #begin_battle(user, creatures)
            print("Cannot {}, please try again.\n".format(choice))
        #Correct answer + random encounter chance
        else:
            clear(0)
            if random_encounter() == 0:
                pass
            else:
                pass
                #begin_battle(user, creatures)
            print(desc_number[i])
            i += 1
        #if correct choice counter equals map size, you win
        if i == len(map_number):
            print("Congratulations, Dungeon {} complete!".format(dungeon))
            break

def random_encounter():
    #chance of encounter - random number between 1-100
    chance = random.randrange(1, 100)
    if chance < 75: # 25% chance of encounter
        return 0
    else:
        import creatures
        monster_type = random.randrange(1,10)
        if monster_type < 5:
            monster = creatures.Troll
        elif monster_type > 5 and monster_type < 7:
            monster = creatures.Elf
        elif monster_type > 7 and monster_type < 9:
            monster = creatures.Dwarf
        else:
            monster = creatures.Giant
        print("You have encountered a level {} {}\n".format(monster.lvl, monster.species))
        status(monster)
        #begin_battle(user, creature)

#def begin_battle(user, creature)

def achievement(user, exp, message):
    print(DEC)
    #Show amount earned
    print("You have gained +{} experience! - {}".format(exp, message))
    #Add to total
    user.exp += exp
    #Display total
    print("Total Experience: {}".format(user.exp))
