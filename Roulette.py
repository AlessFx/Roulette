#!/usr/bin/env python3.9

import random

print (" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Projet de roulette russe de Casino ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
budget = int (input ("Quel est votre budget en entrant au casino ?"))
print ("~~~~~~~~~~~~~~~~~~~~~~ Votre budget de départ est donc de " + str(budget) + " euros ~~~~~~~~~~~~~~~~~~~~~~")

while (budget != 0) :
    if (budget <= 0):
        print("Vous n'avez plus rien ! Merci d 'avoir joué !")
        break
    else :
        numero = int (input("Veuillez indiquer le numéro sur lequel parier : "))
    if (numero % 2 == 0):
        print ("~~~~~~~~~~~~~~~~~~~~~~ Votre mise est donc sur " + str(numero) + " noir ~~~~~~~~~~~~~~~~~~~~~~")
    else :
        print ("~~~~~~~~~~~~~~~~~~~~~~ Votre mise est donc sur " + str(numero) + " rouge ~~~~~~~~~~~~~~~~~~~~~~")

    bet = int (input("Quel est votre pari ? "))
    print ("~~~~~~~~~~~~~~~~~~~~~~ Votre mise est donc de " + str(bet) + " ~~~~~~~~~~~~~~~~~~~~~~")
    budget = budget - bet

    roulette = int(random.randint(0,49))
    print ("~~~~~~~~~~~~~~~~~~~~~~ Et c'est parti, lançons la roulette ! ~~~~~~~~~~~~~~~~~~~~~~")
    print (" Et la roulette tombe sur " + str(roulette) + " !")
    if (roulette == numero) :
        print ("~~~~~~~~~~~~~~~~~~~~~~ Bravo ! Vous avez trouvé le bon numéro ! Vous gagnez donc trois fois votre mise ! ~~~~~~~~~~~~~~~~~~~~~~")
        budget = budget + bet*3
        print ("Nouveau budget : " + str(budget) + " euros")
    elif ((numero % 2 == 0 and roulette % 2 == 0) or (numero % 2 == 1 and roulette % 2 == 1)) :
        print ("~~~~~~~~~~~~~~~~~~~~~~ Ouf ! Vous avez trouvé la bonne numéro ! Vous gagnez donc la moitié de votre pari ! ~~~~~~~~~~~~~~~~~~~~~~")
        budget = budget + (3*bet/2)
        print ("Nouveau budget : " + str(budget) + " euros")
    else :
        print ("~~~~~~~~~~~~~~~~~~~~~~ Perdu ! ~~~~~~~~~~~~~~~~~~~~~~")
        print ("Nouveau budget : " + str(budget) + " euros")
    choix = input ("Voulez-vous continuer de jouer ? oui ou non ? ")
    if (choix == "oui"):
        continue
    else :
        print ("Merci d'avoir joué")
        break
        


