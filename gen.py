with open('Verb.txt', 'r') as fileopen:
    verbs = [line.strip() for line in fileopen]
with open('Type.txt', 'r') as fileopen:
    attack = [line.strip() for line in fileopen]
with open('Animals.txt', 'r') as fileopen:
    animal = [line.strip() for line in fileopen]

import random
animalMod = ["yes", "no"]
yearMod = ["yes", "no"]

years = ["'91", "'92", "'93", "'94", "'95", "'96", "'97", "'98", "'99", "2000"]

f = open("King's Road Moves.txt","w")
for i in range (0,20):
    if random.choice(animalMod) == "yes":
        move = (random.choice(animal))
    else:
        move = (random.choice(verbs))

    move += (" ")
    move += (random.choice(attack))
    move += (" ")

    if random.choice(yearMod) == "no":
        move += (random.choice(years))
    print (move.upper())
    f.write(move.upper() + '\n')

    move = ("")
f.close()
