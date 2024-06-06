# turnBasedCombat
Turn based combat module with implementation

Character class has the following attributes: 
name : name of the character, type = str
hitPoints : hitpoints of the character, type = int
hitChance : chance of the character landing a hit out of 100, type int
maxDamage : maximum possible damage the character can inflict, type int
armor : absorbs incoming damage, subtracts from total damage, type int

printStats(self):
prints the stats of a character.

hit(self, target), target is a character.
self hits target for with a chance of self.hitChance with damage being a random number between 1 and self.maxDamage

fight(character1, character2)
plays a start to finish round of combat. character1 goes first, character2 goes second until one of them goes below 1 hitpoint.
