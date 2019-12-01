"""
Creature definitions for enemies, multiply values by lvl#
"""
class Monster():
    def __init__(self, species, health, attack, weapon, lvl, gil):
        self.species = species
        self.health = health
        self.attack = attack
        self.weapon = weapon
        self.lvl = lvl
        self.gil = gil

Troll = Monster("Troll", 1, 1, "Small Axe", 1, 1)
Elf = Monster("Elf", 3, 1, "Bow", 1, 5)
Dwarf = Monster("Dwarf", 5, 3, "Battle Axe", 1, 10)
Giant = Monster("Giant", 10, 5, "Boulder", 1, 100)
