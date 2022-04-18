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


intro = "Bienvenue voyageur, vous vous apprêtez à pénétrer dans l’Antre du Dragon. Nombre d’histoires circulent sur ce lieu jonché, par le passé, de cadavres et de sang.", "Alors que vous vous engouffrez dans la pénombre, 7 portes se dévoilent sous vos yeux. Chacune d’entre elles présentant un emblème en son centre.","Que choisirez-vous noble visiteur : l’épée (choisir Aventurier), l’arc (choisir Archer), la dague (choisir Assassin), la baguette(choisir Mage),","le mousquet (choisir Pirate), la potion (choisir Alchimiste) ou enfin, le dé (choisir Gambler) ?"

slow_intro = "\n".join(intro)
delay_print(slow_intro)

choix = str(input("\nFaites votres choix : "))
print("Vos stats sont :")
if choix == "Pirate":
   print("Force :", Pirate.ForPi, "Agilité :", Pirate.AgiPi, "Vie :", Pirate.ViePi, "Intelligence :", Pirate.IntPi)
   For = Pirate.ForPi
   Agi = Pirate.AgiPi
   Vie = Pirate.ViePi
   Int = Pirate.IntPi
if choix == "Aventurier":
   print("Force :", Aventurier.ForAv, "Agilité :", Aventurier.AgiAv, "Vie :", Aventurier.VieAv, "Intelligence :", Aventurier.IntAv)
   For = Aventurier.ForAv
   Agi = Aventurier.AgiAv
   Vie = Aventurier.VieAv
   Int = Aventurier.IntAv
if choix == "Mage" :
   print("Force :", Mage.ForMa, "Agilité :", Mage.AgiMa, "Vie :", Mage.VieMa, "Intelligence :", Mage.IntMa)
   For = Mage.ForMa
   Agi = Mage.AgiMa
   Vie = Mage.VieMa
   Int = Mage.IntMa
if choix == "Assassin" :
   print("Force :", Assassin.ForAs, " Agilité :", Assassin.AgiAs, " Vie :", Assassin.VieAs, " Intelligence :", Assassin.IntAs)
   For = Assassin.ForAs
   Agi = Assassin.AgiAs
   Vie = Assassin.VieAs
   Int = Assassin.IntAs
if choix == "Gambler" :
   print("Force :", Gambler.ForGa, " Agilité :", Gambler.AgiGa, " Vie :", Gambler.VieGa, " Intelligence :", Gambler.IntGa)
   For = Gambler.ForGa
   Agi = Gambler.AgiGa
   Vie = Gambler.VieGa
   Int = Gambler.IntGa
if choix == "Alchimiste" :
   print("Force :", Alchimiste.ForAl," Agilité :", Alchimiste.AgiAl," Vie :", Alchimiste.VieAl," Intelligence :", Alchimiste.IntAl)
   For = Alchimiste.ForAl
   Agi = Alchimiste.AgiAl
   Vie = Alchimiste.VieAl
   Int = Alchimiste.IntAl
if choix == "Archer" :
   print("Force :", Archer.ForAr, " Agilité :", Archer.AgiAr, " Vie :", Archer.VieAr, " Intelligence :", Archer.IntAr)
   For = Archer.ForAr
   Agi = Archer.AgiAr
   Vie = Archer.VieAr
   Int = Archer.IntAr

Salle_1 = "Tandis que vous appréhendez les épreuves qui se dresseront devant vous ; des flambeaux s’allument les uns après les autres tout autour de vous."," Quelques secondes de silence sont ensuite interrompues par des cris stridents et irréguliers. Vous faites maintenant face à 3 gobelins."

slow_salle1 = "\n".join(Salle_1)
delay_print(slow_salle1)

action1 = "Que faites-vous dans cette situation? Vous attaquez physiquement (Attaque), vous lancez un sort (Sort),"," vous essayez de les divertir (Diversion), vous vous dissimulez (Cachette)?"

slow_action1 = "\n".join(action1)
delay_print(slow_action1)


choix_2 = str(input("\nFaites votres choix : "))

dé = random.randint(1,12)
print(dé)
Nbgobelin=3


if choix_2 == "Attaque":
   if For >= dé:
       dégât = random.randint(1,3)
       print("Vous avez attaqué le gobelin et vous avez tué", dégât, "gobelin(s)")
       if dégât < 3 :
          Nbgobelin = Nbgobelin - dégât
   elif For <= dé:
       print("Vous avez attaqué et vous avez raté votre coup lamentablement")


if choix_2 == "Sort":
   if Int >= dé:
       dégât = random.randint(1,3)
       print("Vous avez lancé un sort sur le gobelin et vous avez tué", dégât," gobelin(s)")
       if dégât < 3 :
           Nbgobelin = Nbgobelin - dégât
   elif Int <= dé:
       print("Vous avez lancé un sort sur le gobelin et le sort a failli vous toucher en revenant vers vous")

if choix_2 == "Diversion":
   if dé == 1 :
       print("Vous avez réussi à faire diversion sur les trois gobelins et ils ont laissé leurs armes par terre et vous êtes allé les ramasser, vous gagnez donc +1 d'attaque")
       Force = Force + 1
   if Int >= dé :
        print("Vous avez réussi à faire diversion sur les trois gobelins et vous pouvez passé à la salle suivante"

if choix_2 == "Cachette":
    if Agi >= dé:
         print("Vous avez réussi à vous cacher, les gobelins ne vous ont pas vu et ont décidé de partir dans l'entrée car ils ont vu que la porte était ouverte, vous pouvez donc accéder à la salle suivante.")
    elif Agi <= dé :
         print("Vous n'avez pas réussi à vous cacher et les gobelins vous ont remarqué.")
