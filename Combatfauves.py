print("Dans quelle salle voulez-vous aller?")
choix_3 = str(input("\nFaites votres choix : "))
nbfauves = 2
if choix_3 == "Salle 2":
   print("Vous faites maintenant face à deux fauves.")
   action2 = ("Que faites-vous dans cette situation ? Vous attaquez physiquement (Attaque),"," vous lancez un sort (Sort), vous essayer d'esquiver (Esquive)?")
   slow_action2 = "\n".join(action2)
   delay_print(slow_action2)
   choix_4 = str(input("\nFaites votres choix : "))
   print(choix_4)
   if choix_4 == "Attaque":
       if For >= dé():
           dégât = random.randint(1, nbfauves)
           print("Vous avez attaqué et avez tué", dégât, "fauve(s)")
           if dégât < 3:
               nbfauves -= dégât
       elif For <= dé():
           print("Vous avez attaqué et vous avez raté votre coup lamentablement")

   if choix_4 == "Sort":
       if Int >= dé():
           dégât = random.randint(1, nbfauves)
           print("Vous avez lancé un sort et avez tué", dégât, " fauve(s)")
           if dégât < 3:
               nbfauves -= dégât
       elif Int <= dé():
           print("Vous avez lancé un sort sur les fauves et le sort a failli vous toucher en revenant vers vous")
