import time

import sys

import random



class Aventurier():
   for_av = 6
   agi_av = random.randint(4,5)
   vie_av= 6
   int_av = random.randint(4,5)

class Alchimiste():
   for_al = random.randint(2,3)
   agi_al = 6
   vie_al = random.randint(3,4)
   int_al = random.randint(6,8)

class Assassin():
   for_as = random.randint(7,10)
   agi_as = random.randint(8,10)
   vie_as = random.randint(1,3)
   int_as = random.randint(5,7)

class Pirate():
   for_pi = random.randint(6,8)
   agi_pi = random.randint(3,5)
   vie_pi = random.randint(6,8)
   int_pi = random.randint(1,3)

class Archer():
   for_ar = random.randint(5,7)
   agi_ar = random.randint(6,8)
   vie_ar = random.randint(3,4)
   int_ar = random.randint(4,6)

class Mage():
   for_ma = 1
   agi_ma = random.randint(2,3)
   vie_ma = random.randint(6,7)
   int_ma = random.randint(8,10)

class Gambler():
   for_ga = random.randint(1,9)
   agi_ga = random.randint(1,9)
   vie_ga = random.randint(1,9)
   int_ga = random.randint(1,9)


def delay_print(s):
   for c in s:
       sys.stdout.write(c)

       sys.stdout.flush()

       time.sleep(0.01)


intro = "Bienvenue voyageur, vous vous apprêtez à pénétrer dans l’Antre du Dragon. Nombre d’histoires circulent sur ce lieu jonché, par le passé, de cadavres et de sang.", "Alors que vous vous engouffrez dans la pénombre, 7 portes se dévoilent sous vos yeux. Chacune d’entre elles présentant un emblème en son centre.","Que choisirez-vous noble visiteur : l’épée (choisir Aventurier), l’arc (choisir Archer), la dague (choisir Assassin), la baguette(choisir Mage),","le mousquet (choisir Pirate), la potion (choisir Alchimiste) ou enfin, le dé (choisir Gambler) ?"

slow_intro = "\n".join(intro)
delay_print(slow_intro)

choix = str(input("\nFaites votres choix : "))
print("Vos stats sont :")
if choix == "Pirate":
   print("Force :", Pirate.for_pi, "Agilité :", Pirate.agi_pi, "Vie :", Pirate.vie_pi, "Intelligence :", Pirate.int_pi)
   For = Pirate.for_pi
   Agi = Pirate.agi_pi
   Vie = Pirate.vie_pi
   Int = Pirate.int_pi
if choix == "Aventurier":
   print("Force :", Aventurier.for_av, "Agilité :", Aventurier.agi_av, "Vie :", Aventurier.vie_av, "Intelligence :", Aventurier.int_av)
   For = Aventurier.for_av
   Agi = Aventurier.agi_av
   Vie = Aventurier.vie_av
   Int = Aventurier.int_av
if choix == "Mage" :
   print("Force :", Mage.for_ma, "Agilité :", Mage.agi_ma, "Vie :", Mage.vie_ma, "Intelligence :", Mage.int_ma)
   For = Mage.for_ma
   Agi = Mage.agi_ma
   Vie = Mage.vie_ma
   Int = Mage.int_ma
if choix == "Assassin" :
   print("Force :", Assassin.for_as, " Agilité :", Assassin.agi_as, " Vie :", Assassin.vie_as, " Intelligence :", Assassin.int_as)
   For = Assassin.for_as
   Agi = Assassin.agi_as
   Vie = Assassin.vie_as
   Int = Assassin.int_as
if choix == "Gambler" :
   print("Force :", Gambler.for_ga, " Agilité :", Gambler.agi_ga, " Vie :", Gambler.vie_ga, " Intelligence :", Gambler.int_ga)
   For = Gambler.for_ga
   Agi = Gambler.agi_ga
   Vie = Gambler.vie_ga
   Int = Gambler.int_ga
if choix == "Alchimiste" :
   print("Force :", Alchimiste.for_al," Agilité :", Alchimiste.agi_al," Vie :", Alchimiste.vie_al," Intelligence :", Alchimiste.int_al)
   For = Alchimiste.for_al
   Agi = Alchimiste.agi_al
   Vie = Alchimiste.vie_al
   Int = Alchimiste.int_al
if choix == "Archer" :
   print("Force :", Archer.for_ar, " Agilité :", Archer.agi_ar, " Vie :", Archer.vie_ar, " Intelligence :", Archer.int_ar)
   For = Archer.for_ar
   Agi = Archer.agi_ar
   Vie = Archer.vie_ar
   Int = Archer.int_ar

Salle_1 = "Tandis que vous appréhendez les épreuves qui se dresseront devant vous, des flambeaux s’allument les uns après les autres tout autour de vous.","Quelques secondes de silence sont ensuite interrompues par des cris stridents et irréguliers. Vous faites maintenant face à 3 gobelins.","Que faites-vous dans cette situation ? Vous attaquez physiquement (Attaque), vous lancez un sort (Sort), ou bien essayez d'esquiver (Esquive) ?"

slow_salle1 = "\n".join(Salle_1)
delay_print(slow_salle1)


for_go = 3

def dé() :
    x = random.randint(1,12)
    print("Résultat du dé :", x)
    return x

nb_gobelin=3
mort = "Le coup vous est mortel, vous avez échoué...","Pour cette fois..."


while nb_gobelin > 0 :
    choix_2 = str(input("\nFaites votres choix : "))
    if choix_2 == "Attaque":
        if For >= dé() :
            dégât = random.randint(1,nb_gobelin)
            print("Vous réussissez et tuez", dégât, "gobelin(s)")
            if dégât < 3 :
                nb_gobelin -= dégât
            if dégât == 3 :
                nb_gobelin = 0
        else :
            delay_print("Vous avez attaqué et raté votre coup lamentablement")
    if choix_2 == "Sort":
        if Int >= dé() :
            Vie += 2
            print("Vous décidez de lancer un sort de soin et récupérez 2 points de vie !")
        else :
            delay_print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
    if choix_2 == "Esquive" :
        if Agi >= dé():
            print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
            for_go = 0
        else :
            print("L'ennemi est trop rapide, vous n'arriverez pas à esquiver !")

    if nb_gobelin > 0 :
        print("L'ennemi attaque !")
        if for_go >= dé() :
            Vie -= nb_gobelin
            print("L'ennemi vous a touché, vous subissez", nb_gobelin,"points de dégat(s) !")
            if Vie > 0:
                print("Il vous reste", Vie, "pv(s)")
            elif Vie <= 0 :
                delay_print(mort)
                quit()
        else :
            delay_print("L'attaque a raté !")
    for_go = 3

print("Vous avez triomphé ! Vous pouvez maintenant poursuivre votre avancée.")

print("Dans quelle salle voulez-vous aller?")
choix_3 = str(input("\nFaites votres choix : "))
nb_fauves = 2
for_fa = 5
vie_fa = 2
choix_4 = str(input("\nFaites votres choix : "))
salle_2 = "Vous faites maintenant face à deux fauves."," Que faites-vous dans cette situation ? Vous attaquez (Attaque), vous lancez un sort de soin (Sort), ou bien essayez d'esquiver (Esquive) ?"

while nb_fauves > 0 :
    if choix_3 == "Salle 2":
       delay_print(salle_2)
       print(choix_4)
       if choix_4 == "Attaque":
           if For >= dé():
               vie_fa -= 1
               print("Vous avez touché votre cible !")
           elif For <= dé():
               print("Vous avez attaqué et raté votre coup lamentablement.")
       if choix_4 == "Sort":
           if Int >= dé():
               Vie += 2
               print("Vous lancer un sort de soin et récupérez 2 points de vie !","Vous avez")
           elif Int <= dé():
               print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
       if choix_2 == "Esquive":
           if Agi >= dé() :
               print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
               for_fa = 0
           else:
               print("L'ennemi est trop rapide, vous n'arriverez pas à esquiver !")
    if vie_fa == 0 :
        nb_fauves -= 1
        vie_fa = 2
    if nb_fauves > 0 :
        print(" n\L'ennemi attaque !")
        if for_fa >= dé() :
            Vie -= nb_fauves
            print("L'ennemi vous a touché, vous subissez", nb_fauves,"points de dégat(s) !")
            if Vie > 0:
                print("Il vous reste", Vie, "pv(s)")
            elif Vie <= 0 :
                delay_print(mort)
                quit()
        else :
            delay_print("L'attaque a raté !")
