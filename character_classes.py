"""
Character class definitions, multiply values by lvl# except gil
"""
character_name = ""

class Character():
    def __init__(self, name, job, ability, health, attack, exp, lvl, gil):
        self.name = name
        self.job = job
        self.ability = ability
        self.health = health
        self.attack = attack
        self.exp = exp
        self.lvl = lvl
        self.gil = gil

Cleric = Character(character_name, "Cleric", "Heal", 20, 2, 0, 0, 0)
Brute = Character(character_name, "Brute", "Smash", 9, 4, 0, 0, 0)
Mage = Character(character_name, "Mage", "Flame", 13, 1, 0, 0, 0)
Knight = Character(character_name, "Knight", "Defend", 15, 3, 0, 0, 0)
