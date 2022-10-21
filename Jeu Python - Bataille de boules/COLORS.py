from cgitb import text
from telnetlib import NOOPT
from upemtk import *
from random import *
from time import *
from math import *
from PIL import *

def choixcouleur(largeurFenetre,hauteurFenetre):
    cree_fenetre(largeurFenetre, hauteurFenetre)
#=================== VARIABLES ET LISTES DE BASE ==================================================
    lstcolo=['red','blue','green','cyan','pink','purple','yellow','orange']
    lstcolofr=['rouge','bleu','vert','cyan','rose','violet','jaune','orange']
    a = 0 #a c'est l'indice de la position dans la liste (voir en dessous)

#============CREATION TRUC DE BASE DESSIN ========================================================
    
    #C'EST LE FONC D'ECRAN
    #image(100,100,'G:\SAE 1.1\Mes brouillons\shiny.png')

    #CEST LE TEXTE D'INFORMATION
    texte(0,0,"Choississez votre couleur d'équipe : ",taille=14)

    #FLECHE GAUCHE
    ligne(50,125,25,150,'black',3) #   /
    ligne(24,150,50,175,'black',3) #   \
    texte(15,185,"Gauche",taille=14)
    
    #FLECHE DROITE
    ligne(250,125,275,150,'black',3)  # \
    ligne(276,150,250,175,'black',3)  # /
    texte(225,185,"Droite",taille=14)
    
#============ MES AUTRES VARIABLES ================================================================
    maxcolo = len(lstcolo)
    couleurT1 = None
    #print(maxcolo)

#============ MON WHILE ================================================================
    # dans la doc c'est while true mais je fais arreter mon programme après selection de la couleur d'équipe dans couleurT1 (couleurTeam1)
    while couleurT1 is None :

        #Truc pr faire des événement de la doc
        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type = touche ou clic

        #Le ROND AU MILIEU
        cercle((largeurFenetre/2),(hauteurFenetre/2),50,'black',lstcolo[a],3)

        #RAJOUT DALTONIEN
        efface('lol')
        texte(150,75,lstcolofr[a],lstcolo[a],"center",tag='lol')

        #BOUTON DE SELECTION
        rectangle(65,225,235,265,'black','light gray')
        texte(150,245,"ENTER",ancrage='center')
        

#============ LES TOUCHES ================================================================
        if type_ev == 'Touche': #Dire le type de evenement (touche ou clic)
            nom_touche = touche(evenement)
            if nom_touche == 'Left':
                a -= 1 
        # a c'est pour rappel l'indice dans la position de la liste donc si a change, la couleur aussi
                #print(a)
            if nom_touche == 'Right':
                a += 1
                #print(a)
            if nom_touche == 'Return': 
        #RETURN CEST ENTRER
                couleurT1 = lstcolo[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                affichagecoloT1 = lstcolofr[a]
                ferme_fenetre()
                return couleurT1
                print("couleur séléctionnée de l'équipe 1 :",affichagecoloT1)
            if a == maxcolo or a == -(maxcolo) :
                a = 0
        #ce if c'est pour éviter le out of range

        if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                x = int(clic_x(evenement)) #On note les co de x
                y = int(clic_y(evenement)) #On note les co de y
                #print((clic_x(evenement)),(clic_y(evenement)))
                if 75<x<225 and 220<y<275: #Dimension du bouton et if si le clic est dedans
                    couleurT1 = lstcolo[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                    #Confirmation
                    affichagecoloT1 = lstcolofr[a]
                    ferme_fenetre()
                    return couleurT1
                    print("couleur séléctionnée de l'équipe 1 :",affichagecoloT1)
    
        mise_a_jour()
    