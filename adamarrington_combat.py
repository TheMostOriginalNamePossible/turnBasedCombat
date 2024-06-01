"""adamarrington_combat.py
I just pulled from the assignment. I changed the Monster to Joshua and changed some stats
"""


import tbc


def main():
    hero = tbc.Character()
    hero.name = "Sunny"
    hero.hitPoints = 3000
    hero.hitChance = 90
    hero.maxDamage = 600
    hero.armor = 100

    monster = adamarrington_tbc.Character("Joshua", 6000, 85, 300, 200)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)


if __name__ == "__main__":
    main()

