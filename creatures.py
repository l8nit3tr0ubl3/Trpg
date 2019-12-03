"""
Creature definitions for enemies, multiply values by lvl#
"""
class Monster():
    def __init__(self, species, health, attack, defense, speed, weapon, lvl, gil, exp):
        self.species = species
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.weapon = weapon
        self.lvl = lvl
        self.gil = gil
        self.exp = exp

Troll = Monster("Troll", 4, 1, 1, 0.2, "Small Axe", 1, 1, 1)
Elf = Monster("Elf", 6, 1.5, 1, 1.2, "Bow", 1, 5, 3)
Dwarf = Monster("Dwarf", 9, 2.7, 0.8, 1.7, "Battle Axe", 1, 10, 3)
Giant = Monster("Giant", 20, 4.9, 1.8, 1, "Boulder", 1, 100, 20)
