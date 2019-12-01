"""
Needed functions for main
"""
from os import system, name
from time import sleep
import random
import matplotlib.pyplot as plot
import matplotlib.image as image
import creatures


DEC = "-------------------------------------------------"
###########################################################
# System functions
###########################################################
def status(user):
    """pull all user stats into a string"""
    stats = str(user.__dict__)
    #Print it nicely, multi-lined
    print(stats.replace(",", "\n").strip("{").strip("}"), "\n")

def level_up(user):
    """Used to increase a users level and stats"""
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
    """Used to clear screen for readability"""
    sleep(time)
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def show_image(picture):#########FIX ME
    """Display images to user"""
    read = image.imread(picture)
    plot.imshow(read)
###########################################################
# Game core functions
###########################################################
def travel_map(user, map_number, desc_number):
    """Loop through map directions, csalling encounters"""
    square_counter = 0 #counter
    #Loop until correct steps # >= length of map
    while square_counter < len(map_number):
        choice = input("What do you do?\n")
        #Incorrect choice, plus random encounter chance
        if map_number[square_counter] not in choice:
            print("Cannot {}, please try again.\n".format(choice))
        #Correct answer + random encounter chance
        else:
            print(desc_number[square_counter], "\n")
            square_counter += 1
        #if correct choice counter equals map size, you win
        if square_counter == len(map_number) - 1:
            print("Congratulations, Dungeon {} complete!".format(map_number[-1:].strip("'"))
            break
        random_encounter()

def random_encounter():#user):
    """Call creature battles randomly"""
    #chance of encounter - random number between 1-100
    chance = random.randrange(1, 100)
    if chance < 75: # 25% chance of encounter
        monster = 0
    else:
        monster_type = random.randrange(1, 10)
        if monster_type < 5:
            monster = creatures.Troll
        elif monster_type >= 5 < 7:
            monster = creatures.Elf
        elif monster_type >= 7 < 9:
            monster = creatures.Dwarf
        else:
            monster = creatures.Giant
        print("You have encountered a level {} {}\n".format(monster.lvl, monster.species))
        status(monster)
    return monster
        #begin_battle(user, creature)

#def begin_battle(user, creature)

def achievement(user, exp, message):
    """Assign exp to an achievement, and call
    level up when needed"""
    print(DEC)
    #Show amount earned
    print("You have gained +{} experience! - {}".format(exp, message))
    #Add to total
    user.exp += exp
    #Display total
    print("Total Experience: {}".format(user.exp))
    if user.exp % 10 == 0 or (user.exp > 100 and user.exp % 100 == 0):
        level_up(user)
