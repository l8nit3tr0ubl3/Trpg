"""
Character class definitions, multiply values by lvl# except gil
"""
character_name = ""

class Character():
    def __init__(self, name, job, ability, health, attack, defense, speed, exp, lvl, gil):
        self.name = name
        self.job = job
        self.ability = ability
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.exp = exp
        self.lvl = lvl
        self.gil = gil

Cleric = Character(character_name, "Cleric", "Heal", 120, 30, 12, 13, 0, 1, 0)
Brute = Character(character_name, "Brute", "Smash", 100, 26, 10, 11, 0, 1, 0)
Mage = Character(character_name, "Mage", "Flame", 180, 21, 16, 15, 0, 1, 0)
Knight = Character(character_name, "Knight", "Defend", 130, 32, 11, 12, 0, 1, 0)
Warrior = Character(Character_name, "Warrior", "Cleave", 200, 40, 18, 18, 0, 1, 0)
Warlock = Character(Character_name, "Warlock", "Eldrich Blast", 180, 21, 18, 15, 0, 1, 0)

