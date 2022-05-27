
import time

import sys

import random


class test():
    for_te = 10
    agi_te = 10
    vie_te = 10
    int_te = 10


class Aventurier():
    for_av = 6
    agi_av = random.randint(4, 5)
    vie_av = 6
    int_av = random.randint(3, 4)


class Alchimiste():
    for_al = random.randint(5, 6)
    agi_al = 4
    vie_al = random.randint(3, 4)
    int_al = random.randint(6, 8)


class Assassin():
    for_as = random.randint(7, 10)
    agi_as = random.randint(8, 10)
    vie_as = random.randint(2, 3)
    int_as = random.randint(5, 7)


class Pirate():
    for_pi = random.randint(7, 8)
    agi_pi = random.randint(3, 5)
    vie_pi = random.randint(6, 8)
    int_pi = random.randint(1, 3)


class Archer():
    for_ar = random.randint(6, 8)
    agi_ar = random.randint(6, 8)
    vie_ar = random.randint(3, 4)
    int_ar = random.randint(4, 6)


class Mage():
    for_ma = 6
    agi_ma = random.randint(2, 3)
    vie_ma = random.randint(6, 7)
    int_ma = random.randint(8, 10)


class Gambler():
    for_ga = random.randint(1, 9)
    agi_ga = random.randint(1, 9)
    vie_ga = random.randint(1, 9)
    int_ga = random.randint(1, 9)


def delay_print(s):
    for c in s:
        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(0.01)


intro = "Bienvenue voyageur, vous vous apprêtez à pénétrer dans l’Antre du Dragon. Nombre d’histoires circulent sur ce lieu jonché, par le passé, de cadavres et de sang.", "Alors que vous vous engouffrez dans la pénombre, 7 portes se dévoilent sous vos yeux. Chacune d’entre elles présentant un emblème en son centre.", "Que choisirez-vous noble visiteur : l’épée (choisir Aventurier), l’arc (choisir Archer), la dague (choisir Assassin), la baguette(choisir Mage),", "le mousquet (choisir Pirate), la potion (choisir Alchimiste) ou enfin, le dé (choisir Gambler) ?"

slow_intro = "\n".join(intro)
delay_print(slow_intro)

choix = str(input("\nFaites votres choix : "))
print("Vos stats sont :")
if choix == "test":
    print("Force :", test.for_te, "Agilité :", test.agi_te, "Vie :", test.vie_te, "Intelligence :", test.int_te)
    For = test.for_te
    Agi = test.agi_te
    Vie = test.vie_te
    Int = test.int_te
if choix == "Pirate":
    print("Force :", Pirate.for_pi, "Agilité :", Pirate.agi_pi, "Vie :", Pirate.vie_pi, "Intelligence :", Pirate.int_pi)
    For = Pirate.for_pi
    Agi = Pirate.agi_pi
    Vie = Pirate.vie_pi
    Int = Pirate.int_pi
if choix == "Aventurier":
    print("Force :", Aventurier.for_av, "Agilité :", Aventurier.agi_av, "Vie :", Aventurier.vie_av, "Intelligence :",
          Aventurier.int_av)
    For = Aventurier.for_av
    Agi = Aventurier.agi_av
    Vie = Aventurier.vie_av
    Int = Aventurier.int_av
if choix == "Mage":
    print("Force :", Mage.for_ma, "Agilité :", Mage.agi_ma, "Vie :", Mage.vie_ma, "Intelligence :", Mage.int_ma)
    For = Mage.for_ma
    Agi = Mage.agi_ma
    Vie = Mage.vie_ma
    Int = Mage.int_ma
if choix == "Assassin":
    print("Force :", Assassin.for_as, " Agilité :", Assassin.agi_as, " Vie :", Assassin.vie_as, " Intelligence :",
          Assassin.int_as)
    For = Assassin.for_as
    Agi = Assassin.agi_as
    Vie = Assassin.vie_as
    Int = Assassin.int_as
if choix == "Gambler":
    print("Force :", Gambler.for_ga, " Agilité :", Gambler.agi_ga, " Vie :", Gambler.vie_ga, " Intelligence :",
          Gambler.int_ga)
    For = Gambler.for_ga
    Agi = Gambler.agi_ga
    Vie = Gambler.vie_ga
    Int = Gambler.int_ga
if choix == "Alchimiste":
    print("Force :", Alchimiste.for_al, " Agilité :", Alchimiste.agi_al, " Vie :", Alchimiste.vie_al, " Intelligence :",
          Alchimiste.int_al)
    For = Alchimiste.for_al
    Agi = Alchimiste.agi_al
    Vie = Alchimiste.vie_al
    Int = Alchimiste.int_al
if choix == "Archer":
    print("Force :", Archer.for_ar, " Agilité :", Archer.agi_ar, " Vie :", Archer.vie_ar, " Intelligence :",
          Archer.int_ar)
    For = Archer.for_ar
    Agi = Archer.agi_ar
    Vie = Archer.vie_ar
    Int = Archer.int_ar

vie_max = Vie
for_drg = 1
agi_drg = 2
vie_drg = 1
int_drg = 1



def dé():
    x = random.randint(1, 12)
    print("\nRésultat du dé :", x)
    return x


while vie_drg > 0 :
    choix_6 = str(input("\nFaites votres choix : "))
    if choix_6 == "Attaque":
        if For >= dé():
            vie_drg -= 1
            print("Vous avez touché votre cible !")
        elif For <= dé():
            vie_max -= 3
            print("Vous avez attaqué et raté votre coup lamentablement")
    if choix_6 == "Sort":
        if Int >= dé() :
            if vie_max == 2 :
                vie_max += 4
                print("le sort vous à sauvé! Vous évitez la mort et récupérez 4 points de vie !")
            else : vie_max += 1

            if vie_max - Vie == 1 :
                Vie+= 1
                print("Vous décidez de lancer un sort de soin et récupérez 1 point de vie !")
            if vie_max - Vie == 0 :
                print("Vous êtes déjà en pleine forme, continuez comme ça !")
                continue
        else :
            delay_print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
    if choix_6 == "Esquive":
        if Agi >= dé() :
            print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
            for_drg -= 1
        else:
            print("L'ennemi est trop rapide, vous n'arriverez pas à esquiver !")
    if vie_drg == 0 :
        print("La bête succonbe de ses blessures et tombe !")
        vie_drg -= 1
    if vie_drg > 0 :
        print("L'ennemi attaque !")
        if for_drg >= dé() :
            Vie -= 2
            print("L'ennemi vous a touché, vous subissez 2 points de dégat(s) !")
            if Vie > 0:
                print("Il vous reste", Vie, "pv(s)")
            elif Vie <= 0 :
                delay_print(mort)
                quit()
        else :
            delay_print("L'attaque a raté !")

