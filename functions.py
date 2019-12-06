"""
Needed functions for main
"""
from os import system, name
from time import sleep
import random
import sys
import creatures

DIRECTIONS = ["left", "right", "forward", "backward"]
COMMANDS = ["walk", "fight"]
BATTLE_COMMANDS = ["run", "fight", "attack", "special"]
DEC = "-" * 75

###########################################################
# System functions
###########################################################
def check_command(user, map_number, square_counter):
    """get and check movement input"""
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
    random_encounter(user)
    return 1

def clear(time):
    """Used to clear screen for readability"""
    sleep(time)
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def output(message):
    """Nicer output"""
    if len(message) > 1:
        print(DEC)
        print(message)
        print(DEC)

def travel_map(user, map_number, desc_number):
    """Loop through map directions, calling encounters"""
    square_counter = 0 #counter
    #Loop until correct steps # >= length of map
    while square_counter < len(map_number) - 1:
        #Correct answer + random encounter chance
        while check_command(user, map_number, square_counter) != 1:
            check_command(user, map_number, square_counter)
        clear(1)
        if len(desc_number) > 1:
            output(desc_number[square_counter])
        square_counter += 1
        #if correct choice counter equals map size, you win
        if square_counter == len(map_number) - 1:
            output("Congratulations, Dungeon {} complete!".format(map_number[-1:]).strip("'"))

def user_input(message):
    """Get and sanitize user input"""
    ask_user = input(message).split()
    while len(ask_user) == 0:
        ask_user = input(message).split()
    if len(ask_user) >= 2:
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
    if len(ask_user) < 2:
        command = ask_user[0].lower()
        if command in BATTLE_COMMANDS:
            pass
        else:
            print("Command {} not acceptable.".format(command))
            ask_user = input(message).split()
    return ask_user

###########################################################
# User and creature functions
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
    return user

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

def stats_creature(user, creature):
    """Increment creature stats """
    creature.health *= (user.lvl + 1.2)
    creature.attack *= (user.lvl + 1.2)
    creature.defense *= (user.lvl + 1.2)
    creature.speed *= (user.lvl + 1.2)
    creature.exp *= (user.lvl + 1.2)
    creature.gil *= (user.lvl + 1.2)
    creature.lvl = user.lvl
    return creature

def stats_user(user):
    """Increment user stats """
    user.health *= (user.lvl + 1.1)
    user.attack *= (user.lvl + 1.1)
    user.speed *= (user.lvl + 1.1)
    user.speed *= (user.lvl + 1.1)
    return user

def status(user):
    """pull all user stats into a string"""
    stats = str(user.__dict__)
    stats = stats.strip("{").strip("}")
    stats = stats.replace(",", "\n").replace("'", "").replace(" ", "")
    #Print it nicely, multi-lined
    print(DEC)
    print(stats.replace(":", " : "), "\n")
    print(DEC)

################################################################
# Battle functions
################################################################
def attack_chance():
    """Whether attack hits or misses"""
    hit = 0
    chance = random.randrange(1, 100)
    if chance < 65:
        hit = 1
    return hit

def begin_battle(user, creature, boss):
    """Automated battle sequences"""
    remaining_special = user.lvl
    special = 0
    turn_counter = first_attack(user, creature)
    while (user.health > 0 or creature.health > 0):
        chance = attack_chance()
        if turn_counter % 2 != 0:  #creature attack
            creature_attack(user, creature, chance)
        elif turn_counter % 2 == 0:  #user attack
            option = user_input("Attack, special or run?\n")
            if "attack" in option:
                pass
            elif "special" in option:
                special = 1
                if remaining_special <= 0:
                    output("All special attacks used")
                    special = 0
                remaining_special -= 1
            elif "run" in option:
                break
            elif option not in BATTLE_COMMANDS:
                option = user_input("Attack or run?\n")
            user_attack(user, creature, chance, special)
            special = 0
        result = check_health(user, creature, boss)
        turn_counter += 1
        if result == 2:
            return 1
        elif result == 1:
            break
    turn_counter = 0
    clear(6)

def boss_battle(user, boss):
    """Start a boss battle"""
    print("Boss Incoming!!!")
    stats_creature(user, boss)
    #user = stats_user(user)
    win = begin_battle(user, boss, 1)
    complete = 0
    if win != 1:
        output("You have defeated the {} boss!".format(boss.species))
    else:
        output("You have lost, and been sent back to the start of the level.")
        complete = 1
        clear(3)
        output("You are back at the beginning of the level.")
    return complete

def check_health(user, creature, boss):
    """Determine winner of battle"""
    health_reset = user.health
    creature_reset = creature.health
    if user.health <= 0 and boss == 0:
        print(DEC)
        print("You have been beaten, the world goes dark.")
        print("You have lost the game.")
        print(DEC)
        sys.exit()
    if creature.health <= 0:
        print(DEC)
        print("You have defeated the {}!".format(creature.species))
        user.health = health_reset
        creature.health = creature_reset
        achievement(user, creature.exp, creature.gil, "")
        return 1
    if user.health <= 0 and boss == 1:
        return 2
    return 0

def creature_attack(user, creature, chance):
    """Creature attack code"""
    if chance == 1:
        damage = (creature.attack - user.defense)
        if damage <= 0.0:
            damage = 0.1
        print("The {} hits you for {} damage".format(creature.species, damage))
        user.health -= damage
    else:
        print("The {} missed you.".format(creature.species))

def first_attack(user, creature):
    """determine first attack by speed"""
    turn_counter = 0
    if float(user.speed) <= creature.speed:
        turn_counter = 2
        print("You surprised the {} and attack first.".format(creature.species))
    else:
        turn_counter = 1
        print("The {} got the drop on you and attacks first.".format(creature.species))
    return turn_counter

def random_encounter(user):
    """Call creature battles randomly"""
    #chance of encounter - random number between 1-100
    chance = random.randrange(1, 100)
    if chance < 55: # 45% chance of encounter
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
        if user.lvl > 1:
            user = stats_user(user)
            monster = stats_creature(user, monster)
        status(monster)
        stay = user_input("Run, or fight the {}?\n".format(monster.species).lower())
        if 'run' in stay:
            return
        begin_battle(user, monster, 0)

def user_attack(user, creature, chance, special):
    """User attack code"""
    if chance == 1:
        if special == 1:
            attack = user.attack * 2
        else:
            attack = user.attack
        damage = (attack - creature.defense)
        if damage <= 0.0:
            damage = 0.1
        if special == 1:
            print("You attacked the {} with {} for {} damage.".format(creature.species, user.ability, damage))
        else:
            print("You hit the {} for {} damage.".format(creature.species, damage))
        creature.health -= damage
    else:
        print("You missed the {}.".format(creature.species))
