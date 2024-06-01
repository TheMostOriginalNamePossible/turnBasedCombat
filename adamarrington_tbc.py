"""adamarrington_tbc.py
Turn Based Combat system
"""
import random


class Character(object):
    def __init__(self, name="hero", hp=50, hc=20, md=10, armor=5):
        super().__init__()
        self.name = name
        self.hitPoints = hp
        self.hitChance = hc
        self.maxDamage = md
        self.armor = armor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
        else:
            self.__name = "hero"

    @property
    def hitPoints(self):
        return self.__hitPoints

    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            self.__hitPoints = value
        else:
            self.__hitPoints = 50

    @property
    def hitChance(self):
        return self.__hitChance

    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            self.__hitChance = value
        else:
            self.__hitChance = 20

    @property
    def maxDamage(self):
        return self.__maxDamage

    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            self.__maxDamage = value
        else:
            self.__maxDamage = 10

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        if type(value) == int:
            self.__armor = value
        else:
            self.__armor = 5

    def printStats(self):
        print(self.name)
        print("Hit Points: " + str(self.hitPoints))
        print("Hit Chance: " + str(self.hitChance))
        print("Max Damage: " + str(self.maxDamage))
        print("Armor: " + str(self.armor) + "\n")

    def hit(self, value):
        if type(value) == Character:
            hitRoll = random.randint(1, 100)
            print(f"{self.name} attacks...")
            if hitRoll <= self.hitChance:
                damage = random.randint(1, self.maxDamage)
                if damage <= value.armor:
                    print(value.name + "'s armor deflected the damage.\n")
                else:
                    value.hitPoints = value.hitPoints - (damage - value.armor)
                    print(self.name + " hit for " + str(damage - value.armor) + "\n")
            else:
                print(self.name + " missed.\n")


def fight(x,y):
    inCombat = True
    while inCombat:
        if x.hitPoints > 0:
            input("type anything to continue ")
            print("")
            x.hit(y)
            print(x.name + ": " + str(x.hitPoints))
            print(y.name + ": " + str(y.hitPoints) + "\n")
            if y.hitPoints <= 0:
                print(x.name + " wins")
                inCombat = False
        if y.hitPoints > 0:
            input("type anything to continue ")
            print("")
            y.hit(x)
            print(x.name + ": " + str(x.hitPoints))
            print(y.name + ": " + str(y.hitPoints) + "\n")
            if x.hitPoints <= 0:
                print(y.name + " wins")
                inCombat = False


def main():
    c = Character("Monster")
    c.printStats()



