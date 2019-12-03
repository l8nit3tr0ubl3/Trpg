"""
Needed functions for main
"""
from os import system, name
from time import sleep
import string
import random
import sys
import creatures

DIRECTIONS = ["left", "right", "forward", "backward"]
COMMANDS = ["walk", "fight"]
BATTLE_COMMANDS = ["run", "fight", "attack"]
DEC = "-" * 75

###########################################################
# System functions
###########################################################
def output(message):
    """Nicer output"""
    print(DEC)
    print(message)
    print(DEC)

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
            ask_user = input(message).split()
        direction = ask_user[1].lower()
        if direction in DIRECTIONS:
            pass
        else:
            print("Direction {} not acceptable.".format(direction))
            ask_user = input(message).split()
    elif len(ask_user) < 2:
        command = ask_user[0].lower()
        if command in BATTLE_COMMANDS:
            pass
        else:
            print("Command {} not acceptable.".format(command))
            ask_user = input(message).split()
    return ask_user

def check_command(user, map_number, square_counter):
    message = "What do you do?\n"
    choice = user_input(message)
    if len(choice) < 2:
        print("Incorrect option {}.".format(choice))
        random_encounter(user)
        return 0
    #Incorrect choice, plus random encounter chance
    if map_number[square_counter] != choice[1].strip("'").strip("[").strip("]"):
        print("Cannot {}, please try again.\n".format(choice))
        random_encounter(user)
        return 0
    else:
        random_encounter(user)
    return 1

###########################################################
# Status and leveling functions
###########################################################
def achievement(user, exp, gil, message):
    """Assign exp to an achievement, and call
    level up when needed"""
    print(DEC)
    #Show amount earned
    print("You have gained +{} experience and +{} gil!\n{}\n".format(exp, gil, message))
    #Add to total
    user.exp += exp
    user.gil += gil
    #Display total
    print("Total Experience: {}".format(user.exp))
    print("Total Gil: {}".format(user.gil))
    print(DEC)
    if user.exp >= int((10 * user.lvl) * (int(1.2 * float(user.lvl)))): #leveling algo
        level_up(user)
        
def stats_user(user):
    counter = 1
    if user.lvl >= 1:
        increase_list = [user.health,
                         user.attack,
                         user.defense,
                         user.speed]
        if user.lvl % 10 == 0:
            counter += 1
        modifier = float(str(counter) + "." + str(user.lvl))
        for stat in increase_list:
            round(stat)
            stat *= modifier
        return user
    
def stats_creature(user, creature):
    counter = 1
    if user.lvl >= 1:
        increase_list = [creature.health,
                         creature.attack,
                         creature.defense,
                         creature.speed,
                         creature.gil]
        if user.lvl % 10 == 0:
            counter += 1
        modifier = float(str(counter) + "." + str(user.lvl + 1))
        for stat in increase_list:
            round(stat)
            stat *= modifier
        creature.lvl *= user.lvl
    return creature

def status(user):
    """pull all user stats into a string"""
    stats = str(user.__dict__)
    stats = stats.strip("{").strip("}")
    stats = stats.replace(",", "\n").replace("'", "").replace(" ", "")
    #Print it nicely, multi-lined
    print(DEC)
    print(stats.replace(":", " : "), "\n")
    print(DEC)

def level_up(user):
    """Used to increase a users level and stats"""
    print(DEC)
    print("You have gained a level!")
    user.lvl += 1
    print("You are now level {}".format(user.lvl))
    print(DEC)
    stats_user(user)
    status(user)
    print(DEC, "\n")
    return user

################################################################
# Battle + map functions
################################################################

def travel_map(user, map_number, desc_number):
    """Loop through map directions, calling encounters"""
    square_counter = 0 #counter
    #Loop until correct steps # >= length of map
    while square_counter < len(map_number) - 1:
        #Correct answer + random encounter chance
        while check_command(user, map_number, square_counter) == 0:
            check_command(user, map_number, square_counter)
        else:
            clear(1)
            if len(desc_number) > 1:
                output(desc_number[square_counter])
            square_counter += 1
        #if correct choice counter equals map size, you win
        if square_counter == len(map_number) - 1:
            output("Congratulations, Dungeon {} complete!".format(map_number[-1:]).strip("'"))
            return

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
        output("You have encountered a level {} {}\n".format(monster.lvl, monster.species))
        stats_creature(user, monster)
        status(monster)
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
    health_reset = user.health
    creature_reset = creature.health
    if float(user.speed) <= creature.speed:
        turn_counter = 2
        print("You surprised the {} and attack first.".format(creature.species))
    else:
        turn_counter = 1
        print("The {} got the drop on you and attacks first.".format(creature.species))
    while (user.health > 0 or creature.health > 0):
        chance = attack_chance()
        if turn_counter % 2 != 0:  #creature attack
            if chance == 1:
                damage = (creature.attack - user.defense)
                if damage < 0:
                    print("Blocked all damage with defense stat")
                    damage = 0
                print("The {} hits you for {} damage".format(creature.species, damage))
                user.health -= damage
                turn_counter += 1
            else:
                print("The {} missed you.".format(creature.species))
                turn_counter += 1
        elif turn_counter % 2 == 0:  #user attack
            option = user_input("Attack or run?\n")
            if "attack" in option:
                pass
            elif "run" in option:
                break
            if chance == 1:
                damage = (user.attack - creature.defense)
                if damage < 0:
                    print("Blocked all damage with defense stat")
                    damage = 0
                print("You hit the {} for {} damage.".format(creature.species, damage))
                creature.health -= damage
                turn_counter += 1
            else:
                print("You missed the {}.".format(creature.species))
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
            user.health = health_reset
            creature.health = creature_reset
            achievement(user, creature.exp, creature.gil, "")
            break
    turn_counter = 0
    clear(6)
