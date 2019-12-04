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

#Standard creature
Troll = Monster("Troll", 50, 18, 11, 10, "Small_Axe", 1, 1, 1)
Elf = Monster("Elf", 80, 21, 13, 15, "Bow", 1, 5, 3)
Dwarf = Monster("Dwarf",110, 22, 15, 10, "Battle_Axe", 1, 10, 3)
Giant = Monster("Giant", 250, 27, 13, 16, "Boulder", 1, 100, 20)

#BOSSES
map1_boss = Monster("Ent Warrior", 60, 4, 3, 6, "Large_Branch", 1, 100, 50)
map2_boss = Monster("Spider Queen", 180, 12, 5, 9, "Fangs", 1, 250, 150)
map3_boss = Monster("Crazed ciizen", 540, 30, 12, 20, "Headbutt", 1, 400, 230)
