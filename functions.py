"""
Needed functions for main
"""
from os import system, name
from time import sleep
import random
import sys
import creatures

DIRECTIONS = ["left", "right", "forward", "backward"]
COMMANDS = ["walk", "look", "fight", "grab", "unlock"]
BATTLE_COMMANDS = ["run", "fight", "attack"]
DEC = "-------------------------------------------------"
###########################################################
# System functions
###########################################################
def output(message):
    """Nicer output"""
    print(DEC)
    print(message)
    print(DEC)

def status(user):
    """pull all user stats into a string"""
    stats = str(user.__dict__)
    #Print it nicely, multi-lined
    print(DEC)
    print(stats.replace(",", "\n").strip("{").strip("}"), "\n")
    print(DEC)

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
            stat *= (user.lvl * 1.1)
    status(user)
    print(DEC, "\n")
    return user

def clear(time):
    """Used to clear screen for readability"""
    sleep(time)
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def user_input(message):
    """Get and sanitize user input"""
    ask_user = input(message).split()
    if len(ask_user) > 1:
        command = ask_user[0].lower()
        if command in COMMANDS:
            pass
        else:
            print("Command {} not acceptable.".format(command))
        direction = ask_user[1].lower()
        if direction in DIRECTIONS:
            pass
        else:
            print("Direction {} not acceptable.".format(direction))
    elif len(ask_user) == 1:
        command = ask_user[0].lower()
        if command in BATTLE_COMMANDS:
            pass
        else:
            print("Command {} not acceptable.".format(command))
    return ask_user

def achievement(user, exp, gil, message):
    """Assign exp to an achievement, and call
    level up when needed"""
    print(DEC)
    #Show amount earned
    print("You have gained +{} experience and {} gil! - {}".format(exp, gil, message))
    #Add to total
    user.exp += exp
    user.gil += gil
    #Display total
    print("Total Experience: {}".format(user.exp))
    print("Total Gil: {}".format(user.gil))
    print(DEC)
    if user.exp >= int((10 * user.lvl) * (1.2 * user.lvl)): #leveling algo
        level_up(user)
###########################################################
# Game core functions
###########################################################
def travel_map(user, map_number, desc_number):
    """Loop through map directions, calling encounters"""
    message = "What do you do?\n"
    square_counter = 0 #counter
    #Loop until correct steps # >= length of map
    while square_counter < len(map_number) - 1:
        choice = user_input(message)
        random_encounter(user)
        #Incorrect choice, plus random encounter chance
        if map_number[square_counter] != choice[1].strip("'").strip("[").strip("]"):
            clear(3)
            print("Cannot {}, please try again.\n".format(choice))
        #Correct answer + random encounter chance
        else:
            clear(3)
            print(DEC)
            print(desc_number[square_counter])
            print(DEC, "\n")
            square_counter += 1
        #if correct choice counter equals map size, you win
        if square_counter == len(map_number) - 1:
            print(DEC)
            print("Congratulations, Dungeon {} complete!".format(map_number[-1:]).strip("'"))
            print(DEC)
            break
    del message

def random_encounter(user):
    """Call creature battles randomly"""
    #chance of encounter - random number between 1-100
    chance = random.randrange(1, 100)
    if chance < 65: # 35% chance of encounter
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
        print(DEC)
        print("You have encountered a level {} {}\n".format(monster.lvl, monster.species))
        print(DEC)
        stay = user_input("Run, or fight the {}?\n".format(monster.species).lower())
        if 'run' in stay:
            return
        begin_battle(user, monster)

def attack_chance():
    """Whether attack hits or misses"""
    hit = 0
    chance = random.randrange(1, 100)
    if chance < 65:
        hit = 1
    return hit

def begin_battle(user, creature):
    """Automated battle sequences"""
    turn_counter = 1
    health_reset = user.health
    creature_reset = creature.health
    if user.lvl > 1:
        creature.lvl *= int(user.lvl * 1.2)
        creature.gil *= int(user.lvl * 1.2)
        creature.attack *= int(user.lvl * 1.2)
        creature.health *= int(user.lvl * 1.2)
        user.health *= (user.lvl * 1.1)
        user.attack *= (user.lvl * 1.1)
    status(creature)
    #run = 0
    while (user.health > 0 or creature.health > 0): #and run != 1:
        chance = attack_chance()
        if turn_counter % 2 != 0:  #creature attack
            if chance == 1:
                print("{} hits you for {} damage".format(creature.species, creature.attack))
                user.health -= creature.attack
                turn_counter += 1
            else:
                print("{} missed you.".format(creature.species))
                turn_counter += 1
        elif turn_counter % 2 == 0:  #user attack
            option = user_input("Attack or run?\n")
            if "attack" in option:
                pass
            elif "run" in option:
                break
            if chance == 1:
                print("You hit the {} for {} damage.".format(creature.species, user.attack))
                creature.health -= user.attack
                turn_counter += 1
            else:
                print("You missed {}.".format(creature.species))
                turn_counter += 1
        if user.health <= 0:
            print(DEC)
            print("You have been beaten, the world goes dark.")
            print("You have lost the game.")
            print(DEC)
            sys.exit()
        elif creature.health <= 0:
            print(DEC)
            print("You have defeated the {}!".format(creature.species))
            achievement(user, creature.exp, creature.gil, "")
            break
    user.health = health_reset
    creature.health = creature_reset
    turn_counter = 0
    clear(6)
