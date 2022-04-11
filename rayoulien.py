import time

import sys

import random



class Aventurier():
   ForAv = 6
   AgiAv = random.randint(4,5)
   VieAv = 6
   IntAv = random.randint(4,5)

class Alchimiste():
   ForAl = random.randint(2,3)
   AgiAl = 6
   VieAl = random.randint(3,4)
   IntAl = random.randint(6,8)

class Assassin():
   ForAs = random.randint(7,10)
   AgiAs = random.randint(8,10)
   VieAs = random.randint(1,2)
   IntAs = random.randint(5,7)

class Pirate():
   ForPi = random.randint(6,8)
   AgiPi = random.randint(3,5)
   ViePi = random.randint(6,8)
   IntPi = random.randint(1,3)

class Archer():
   ForAr = random.randint(5,7)
   AgiAr = random.randint(6,8)
   VieAr = random.randint(2,4)
   IntAr = random.randint(4,6)

class Mage():
   ForMa = 1
   AgiMa = random.randint(2,3)
   VieMa = random.randint(5,6)
   IntMa = random.randint(7,10)

class Gambler():
   ForGa = random.randint(1,9)
   AgiGa = random.randint(1,9)
   VieGa = random.randint(1,9)
   IntGa = random.randint(1,9)


def delay_print(s):
   for c in s:
       sys.stdout.write(c)

       sys.stdout.flush()

       time.sleep(0.01)


intro = "Bienvenue voyageur, vous vous apprêtez à pénétrer dans l’Antre du Dragon. Nombre d’histoires circulent sur ce lieu jonché, par le passé, de cadavres et de sang.", "Alors que vous vous engouffrez dans la pénombre, 7 portes se dévoilent sous vos yeux. Chacune d’entre elles présentant un emblème en son centre.","Que choisirez-vous noble visiteur : l’épée (choisir Aventurier), l’arc (choisir Archer), la dague (choisir Assassin), la baguette(choisir Mage), le mousquet (choisir Pirate), la potion (choisir Alchimiste) ou enfin, le dé (choisir Gambler) ?"

slow_intro = "\n".join(intro)
delay_print(slow_intro)

choix = str(input("\nFaites votres choix : "))
print("Vos stats sont :")
if choix == "Pirate":
   print("Force :", Pirate.ForPi, "Agilité :", Pirate.AgiPi, "Vie :", Pirate.ViePi, "Intelligence :", Pirate.IntPi)

if choix == "Aventurier":
   print("Force :", Aventurier.ForAv, "Agilité :", Aventurier.AgiAv, "Vie :", Aventurier.VieAv, "Intelligence :", Aventurier.IntAv)

if choix == "Mage" :
   print("Force :", Mage.ForMa, "Agilité :", Mage.AgiMa, "Vie :", Mage.VieMa, "Intelligence :", Mage.IntMa)

if choix == "Assassin" :
   print("Force :", Assassin.ForAs, " Agilité :", Assassin.AgiAs, " Vie :", Assassin.VieAs, " Intelligence :", Assassin.IntAs)

if choix == "Gambler" :
   print("Force :", Gambler.ForGa, " Agilité :", Gambler.AgiGa, " Vie :", Gambler.VieGa, " Intelligence :", Gambler.IntGa)

if choix == "Alchimiste" :
   print("Force :", Alchimiste.ForAl," Agilité :", Alchimiste.AgiAl," Vie :", Alchimiste.VieAl," Intelligence :", Alchimiste.IntAl)

if choix == "Archer" :
   print("Force :", Archer.ForAr, " Agilité :", Archer.AgiAr, " Vie :", Archer.VieAr, " Intelligence :", Archer.IntAr)
   
Salle_1 = "Tandis que vous appréhendez les épreuves qui se dresseront devant vous ; des flambeaux s’allument les uns après les autres tout autour de vous. Quelques secondes de silence sont ensuite interrompues par des cris stridents et irréguliers. Vous faites maintenant face à 3 gobelins."
print(Salle_1)



