import time

import sys

import random


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

intro = "Bienvenue voyageur, vous vous apprêtez à pénétrer dans l’Antre du Dragon. Nombre d’histoires circulent sur ce lieu jonché, par le passé, de cadavres et de sang.", "Alors que vous vous engouffrez dans la pénombre, 7 portes se dévoilent sous vos yeux. Chacune d’entre elles présentant un emblème en son centre.", "Que choisirez-vous noble visiteur : l’épée, l’arc, la dague, la baguette, le mousquet, la potion ou enfin, le dé ?"

slow_intro = "\n".join(intro)
delay_print(slow_intro)

choix = str(input("choisissez une classe ?"))

class Aventurier():
    F = 6
    A = random.randint(4,5)
    V = 6
    I = random.randint(4,5)


class Alchimiste():
    F = random.randint(2,3)
    A = 6
    V = random.randint(3, 4)
    I = random.randint(6, 8)


class Assassin():
    F = random.randint(7, 10)
    A = random.randint(8, 10)
    V = random.randint(1, 2)
    I = random.randint(5, 7)


class Pirate():
    F = random.randint(6, 8)
    A = random.randint(3, 5)
    V = random.randint(6, 8)
    I = random.randint(1, 3)


class Archer():
    F = random.randint(5, 7)
    A = random.randint(6, 8)
    V = random.randint(2, 4)
    I = random.randint(4, 6)


class Mage():
    F = 1
    A = random.randint(2, 3)
    V = random.randint(5, 6)
    I = random.randint(7, 10)


class Gambler():
    F = random.randint(1, 9)
    A = random.randint(1, 9)
    V = random.randint(1, 9)
    I = random.randint(1, 9)

if choix=="Gambler":
    print()
