"""
Creature definitions for enemies, multiply values by lvl#
"""
class Monster():
    def __init__(self, lvl, species, health, attack, defense, speed, weapon, gil, exp):
        self.lvl = lvl
        self.species = species
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.weapon = weapon
        self.gil = gil
        self.exp = exp

#Standard creature
Troll = Monster(1, "Troll", 50, 18, 11, 10, "Small_Axe", 1, 1)
Elf = Monster(1, "Elf", 80, 21, 13, 15, "Bow", 5, 3)
Dwarf = Monster(1, "Dwarf",110, 22, 15, 10, "Battle_Axe", 10, 3)
Giant = Monster(1, "Giant", 250, 27, 13, 16, "Boulder", 100, 20)
Orc = Monster(1, "Orc", 95, 22, 16, 10, "Cudgel", 20, 5)

#BOSSES
map1_boss = Monster(1, "Ent Warrior", 60, 4, 3, 6, "Large_Branch", 100, 50)
map2_boss = Monster(1, "Spider Queen", 180, 12, 5, 9, "Fangs", 250, 150)
map3_boss = Monster(1, "Crazed ciizen", 540, 30, 12, 20, "Headbutt", 400, 230)
