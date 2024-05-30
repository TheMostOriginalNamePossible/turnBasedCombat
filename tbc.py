"""tbc.py
Turn Based Combat system
"""


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
        print("Armor: " + str(self.armor))

def fight(x,y):

def main():
    c = Character("Monster")
    c.printStats()


main()
