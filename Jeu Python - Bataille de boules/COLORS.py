from cgitb import text
from upemtk import *
from random import *
from time import *
from math import *

if __name__ == '__main__':
    largeurFenetre = 300
    hauteurFenetre = 300
    lstcolo=['red','blue','green','cyan','pink','purple','yellow','orange']
    a = 0

    cree_fenetre(largeurFenetre, hauteurFenetre)
    texte(0,0,"Choississez votre couleur d'équipe : ",taille=14)
    texte(0,280,"Appuyez sur Space pour Sortir",taille=10)
    #FLECHE GAUCHE
    ligne(50,125,25,150,'black',3)
    ligne(24,150,50,175,'black',3)
    texte(15,200,"Gauche",taille=14)
    #FLECHE DROITE
    ligne(250,125,275,150,'black',3)
    ligne(276,150,250,175,'black',3)
    texte(225,200,"Droite",taille=14)
    
    maxcolo = len(lstcolo)
    #print(maxcolo)

    while True :
        evenement = donne_evenement()
        type_ev = type_evenement(evenement)
        cercle((largeurFenetre/2),(hauteurFenetre/2),50,'black',lstcolo[a],3)
        if type_ev == 'Touche':
            nom_touche = touche(evenement)
            if nom_touche == 'Left':
                a -= 1
                #print(a)
            if nom_touche == 'Right':
                a += 1
                #print(a)
            if nom_touche == 'space': 
                ferme_fenetre()
            if a == maxcolo or a == -(maxcolo) :
                a = 0
        mise_a_jour() 
