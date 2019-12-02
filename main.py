#!/usr/bin/python3
"""
A fantasy rpg, using classes to define and track characters, monsters, etc.
"""
#Import all other files and modules
import maps
import character_classes as CC
import functions as func

#Welcome screen
print(func.DEC)
print("Welcome to 'PLACEHOLDER NAME' fantasy rpg.\n")
print("You have multiple choices in this adventure,")
print("and each has its benefits or consquences.")
print(func.DEC)
func.clear(3) #Clear screen for nicer USER readability
#
#func.show_image("pic.png")
#func.clear(10)
#
#Print instructions
print(func.DEC)
print("""
Within this game, commands consist of an action
and an object, direction, person or monster.

Directions: left, right, forward, backward
Commands: walk, look, fight, grab, unlock
Battle Commands: attack, run
""")
print(func.DEC)
input("Press enter to continue......")
func.clear(0)

#Title
print(func.DEC)
print("Character Classes.")
print(func.DEC)

#Show character menu
print("#", "Job   ", "Ability", "Health", "Attack", "Exp", "LVL", "Gil")
print("1", CC.Cleric.job, CC.Cleric.ability, "  ", CC.Cleric.health, " "*3,
      CC.Cleric.attack, " "*4, CC.Cleric.exp, " ", CC.Cleric.lvl, " ", CC.Cleric.gil)
print("2", CC.Brute.job, "", CC.Brute.ability, " ", CC.Brute.health, " "*3,
      CC.Brute.attack, " "*4, CC.Brute.exp, " ", CC.Brute.lvl, " ", CC.Brute.gil)
print("3", CC.Mage.job, " ", CC.Mage.ability, " ", CC.Mage.health, " "*3,
      CC.Mage.attack, " "*4, CC.Mage.exp, " ", CC.Mage.lvl, " ", CC.Mage.gil)
print("4", CC.Knight.job, CC.Knight.ability, "", CC.Knight.health, " "*3,
      CC.Knight.attack, " "*4, CC.Knight.exp, " ", CC.Knight.lvl, " ", CC.Knight.gil)

#Get USERs character choice and name
print(func.DEC)
_CLASS = input("Please choose your characters job class number.\n")
print(func.DEC)
if _CLASS == "1":
    USER = CC.Cleric
elif _CLASS == "2":
    USER = CC.Brute
elif _CLASS == "3":
    USER = CC.Mage
elif _CLASS == "4":
    USER = CC.Knight
else:
    print("Incorrect value, try again.")
USER.name = input("Please enter your name.\n")
print(func.DEC)
func.clear(0)

#Show chosen charcter type and name
print(func.DEC)
print("{}, you have chosen {} as your job type.".format(USER.name, USER.job), "\n"+func.DEC)
print(func.DEC)

#First achievement
func.achievement(USER, 1, 0, "Begin Your Journey!")
func.clear(4)

#Print start of game
print(func.DEC)
print("""
You wake up in a dark forest. Sore, bleeding, and
dizzy you stand up. You have no memory of how
you've gotten here. You step outside, and see a
path in front of you.
""")
print(func.DEC)
#Loop through user input untill map is cleared
func.travel_map(USER, maps.map1, maps.desc1)
func.clear(6)

#Second achievement
MESSAGE = "First Dungeon Complete!"
func.achievement(USER, 5, 25, MESSAGE)
del MESSAGE #Free up memory thats no longer used
func.clear(4)

print(func.DEC)
print("""
After leaving the forest you follow a small path into
a farm town. Walking about the town, you see a
marketplace, and decide to steal an apple to sate your
hunger.
As you walk away eating the apple, a large
angry looking troll grabs you by the hair and throws
you to the ground. Not wanting to tempt fate, you run,
and come upon a cave entrance.
""")
print(func.DEC)

func.travel_map(USER, maps.map2, maps.desc2)
func.clear(6)

MESSAGE = "Second Dungeon Complete!"
func.achievement(USER, 15, 100, MESSAGE)
del MESSAGE
func.clear(4)

print(func.DEC)
print("""
Your eyes burn slighlty as you exit the cave into the sun.
Wiping the cobwebs and dirt from your clothes, you head
off towards the next town.
When approaching the gates, you encounter a man in a dark
cloak. His face is hidden, and he makes you uneasy.
'This town is a maze, and none who enter these gates emerge
from the other side.' The gates swing open.....
""")
print(func.DEC)

func.travel_map(USER, maps.map3, maps.desc3)
func.clear(6)

MESSAGE = "Third Dungeon Complete!"
func.achievement(USER, 50, 225, MESSAGE)
del MESSAGE #Free up memory thats no longer used
func.clear(4)
####################################################
print(func.DEC)
print("You have reached the end of the game so far.")
print("Please wait for updates.")
print(func.DEC)
func.status(USER)
func.clear(25)
