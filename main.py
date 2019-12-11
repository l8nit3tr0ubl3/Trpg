#!/usr/bin/python3
"""
A fantasy rpg, using classes to define and track characters, monsters, etc.
"""
#Import all other files and modules
import maps
import character_classes as CC
import creatures as C
import functions as func
import messages

#Welcome screen
func.output(messages.welcome)
func.clear()

#Title
func.output("Chracter Classes")

#Show character menu
print("#", "Job    ", "Ability       ", "Health", "Attack", "Defense", "Speed")
print("1", CC.Cleric.job, "", CC.Cleric.ability, " "*9, CC.Cleric.health, " "*2,
      CC.Cleric.attack, " "*3, CC.Cleric.defense, " "*4, CC.Cleric.speed)
print("2", CC.Brute.job, " ", CC.Brute.ability, " "*8, CC.Brute.health, " "*2,
      CC.Brute.attack, " "*3, CC.Brute.defense, " "*4, CC.Brute.speed)
print("3", CC.Mage.job, " "*2, CC.Mage.ability, " "*8, CC.Mage.health, " "*2,
      CC.Mage.attack, " "*3, CC.Mage.defense, " "*4, CC.Mage.speed)
print("4", CC.Knight.job, "", CC.Knight.ability, " "*7, CC.Knight.health, " "*2,
      CC.Knight.attack, " "*3, CC.Knight.defense," "*4, CC.Knight.speed)
print("5", CC.Warrior.job, CC.Warrior.ability, " "*7, CC.Warrior.health, " "*2,
      CC.Warrior.attack, " "*3, CC.Warrior.defense, " "*4, CC.Warrior.speed)
print("6", CC.Warlock.job, CC.Warlock.ability, ""*13, CC.Warlock.health, " "*2,
      CC.Warlock.attack, " "*3, CC.Warlock.defense, " "*4, CC.Warlock.speed)

#Get USERs character choice and name
_CLASS = input("\nChoose character class number.\n")
if _CLASS == "1":
    USER = CC.Cleric
elif _CLASS == "2":
    USER = CC.Brute
elif _CLASS == "3":
    USER = CC.Mage
elif _CLASS == "4":
    USER = CC.Knight
elif _CLASS == "5":
    USER = CC.Warrior
elif _CLASS == "6":
    USER = CC.Warlock
else:
    print("Incorrect value, try again.")
    _CLASS = input("\nChoose character class number.\n")
USER.name = input("\nPlease enter your name.\n")
print(func.DEC)
func.clear()

#Show chosen charcter type and name
func.output("{}, you have chosen {} as your job type.".format(USER.name, USER.job))

#First achievement
func.achievement(USER, 1, 0, "Begin Your Journey!")
func.clear()
func.output(messages.intro)

#Loop through user input untill map is cleared
func.travel_map(USER, maps.map1, maps.desc1)
func.clear()
#Second achievement
MESSAGE = "First Dungeon Complete!"
func.achievement(USER, 5, 25, MESSAGE)
func.clear()
BOSS = func.boss_battle(USER, C.map1_boss)
if BOSS == 1:
    func.travel_map(USER, maps.map1, maps.desc1)
else:
    pass
func.output(messages.end_level1)

func.travel_map(USER, maps.map2, maps.desc2)
func.clear()

MESSAGE = "Second Dungeon Complete!"
func.achievement(USER, 15, 100, MESSAGE)
func.clear()

BOSS = func.boss_battle(USER, C.map2_boss)
if BOSS == 1:
    func.travel_map(USER, maps.map2, maps.desc2)
else:
    pass

func.output(messages.end_level2)

func.travel_map(USER, maps.map3, maps.desc3)
func.clear()

MESSAGE = "Third Dungeon Complete!"
func.achievement(USER, 50, 225, MESSAGE)
func.clear()

BOSS = func.boss_battle(USER, C.map3_boss)
if BOSS == 1:
    func.travel_map(USER, maps.map3, maps.desc3)
else:
    pass

####################################################
func.output(messages.endgame)
func.status(USER)
func.clear()
