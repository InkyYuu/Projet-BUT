# =========================== IMPORTS ================================
from hashlib import blake2b
from tkinter import CENTER
from matplotlib.pyplot import text
from upemtk import *
from math import *
from random import *
from time import *
# ======================= NOS MODULES A NOUS ======================
from COLORS import choixcouleur
# ========================== FONCTIONS ===============================
def pose_ronds (liste_boule_allie,liste_boule_ennemi, couleur_allie, couleur_ennemi, tour, rayon) :
    """
    Arguments :
    liste_boule_allie sous forme [Ox,Oy,rayon,tag]
    liste_boule_ennemi sous forme [Ox,Oy,rayon,tag]
    couleur_allie est un string de la couleur de l'équipe allié
    couleur_ennemi est un string de la couleur de l'équipe ennemi
    tour représente à quel tour nous somme
    rayon est le rayon de la boule que nous allons posée
    """
    Ox, Oy, RIEN = attente_clic()
    Cas1 = False
    Cas2 = False
    Cas3 = False
    if liste_boule_allie == [] and liste_boule_ennemi == []:
        cercle(Ox,Oy,rayon,'black',couleur_allie,tag='boule'+couleur_allie+str(tour))
        liste_boule_allie.append([Ox,Oy,rayon,'boule'+couleur_allie+str(tour)])
    else :
        for j in range(len(liste_boule_allie)):
            if sqrt((liste_boule_allie[j][0]-Ox)**2 + (liste_boule_allie[j][1]-Oy)**2) < liste_boule_allie[j][2] :
                return
            elif sqrt((liste_boule_allie[j][0]-Ox)**2 + (liste_boule_allie[j][1]-Oy)**2) < liste_boule_allie[j][2] + rayon:
                return
        for i in range(len(liste_boule_ennemi)):
            print(liste_boule_ennemi[i])
            if sqrt((liste_boule_ennemi[i][0]-Ox)**2 + (liste_boule_ennemi[i][1]-Oy)**2) < liste_boule_ennemi[i][2] :
                Cas3 = True
                print('Cas3')
                indice = i
                break
            elif sqrt((liste_boule_ennemi[i][0]-Ox)**2 + (liste_boule_ennemi[i][1]-Oy)**2) < liste_boule_ennemi[i][2] + rayon:
                Cas2 = True
                print('Cas2')
                break
        if Cas2 == False and Cas3 == False :
            Cas1 = True
        if Cas1 == True :
            cercle(Ox,Oy,rayon,'black',couleur_allie,tag='boule'+couleur_allie+str(tour))
            liste_boule_allie.append([Ox,Oy,rayon,'boule'+couleur_allie+str(tour)])
        elif Cas2 == True :
            print(('Faux'))
            #texte(0,0,"IMPOSSIBLE !", 'black', 'center')
        elif Cas3 == True :
            efface(liste_boule_ennemi[indice][3])

            vecteurU = [(Ox-liste_boule_ennemi[indice][0]),(Oy-liste_boule_ennemi[indice][1])]
            normeU = sqrt((vecteurU[0]**2)+vecteurU[1]**2)

            rayon_bouleclic = int(liste_boule_ennemi[indice][2]- normeU)
            rayon_boulerestante = int(normeU)

            NewOx = (liste_boule_ennemi[indice][0])-((rayon_bouleclic/rayon_boulerestante)*(Ox-liste_boule_ennemi[indice][0]))
            NewOy = (liste_boule_ennemi[indice][1])-((rayon_bouleclic/rayon_boulerestante)*(Oy-liste_boule_ennemi[indice][1]))

            cercle(NewOx,NewOy,rayon_boulerestante,'black',couleur_ennemi,tag='boule'+couleur_allie+str(tour))
            cercle(Ox,Oy,rayon_bouleclic,'black',couleur_ennemi,tag='boule'+couleur_ennemi+str(tour))

            liste_boule_ennemi.append([Ox,Oy,rayon_bouleclic,'boule'+couleur_ennemi+str(tour)+'0'])
            liste_boule_ennemi.append([NewOx,NewOy,rayon_boulerestante,'boule'+couleur_allie+str(tour)+'1'])
            liste_boule_ennemi.pop(indice)

    mise_a_jour()
   
def calcul_score (lstJ1,lstJ2):
    scoreJ1 = 0
    scoreJ2 = 0
    #CALCUL DES AIRES DES JOUEURS
    for i in range(len(lstJ1)):
        scoreJ1 = scoreJ1 + (pi*(lstJ1[i][2]))
    for i in range(len(lstJ2)):
        scoreJ2 = scoreJ2 + (pi*(lstJ2[i][2]))
    print(scoreJ1,scoreJ2)

    if scoreJ1 > scoreJ2 :
        return 'Joueur1'
    elif scoreJ1 == scoreJ2 :
        return 'Egalité'
    else :
        return 'Joueur2'
    
def autre ():
    pass

# ========================== VARIABLES ===============================

victoire = False
variant_sablier = False
variant_score = False
variant_taille_boule = False
variant_dynamique = False
variant_terminaison = False
variant_obstacles = False
hauteurFenetre = 540
largeurFenetre = 960
# ========================= CODE PRINCIPAL ===========================
couleurJ1 = 'red' #choixcouleur(300,300)
couleurJ2 = 'blue'#choixcouleur(300,300)
cree_fenetre(largeurFenetre, hauteurFenetre)
tour = 0
lst_boule_J1 = []
lst_boule_J2 = []
while victoire != True :
    for joueur in range (2):
        if not(joueur%2) :
            pose_ronds (lst_boule_J1,lst_boule_J2, couleurJ1, couleurJ2, tour, 50)
        else :
            pose_ronds (lst_boule_J2,lst_boule_J1, couleurJ2, couleurJ1, tour, 50)
    tour += 1
    if tour == 5 :
        victoire = True
gagnant = calcul_score(lst_boule_J1,lst_boule_J2)
print ("Le gagnant est :",gagnant)
#attente_clic()
#ferme_fenetre()