import pygame  
from pygame.locals import *
from random import randrange,choice

#fonction permettant l'affichage de la grille, envoyée en argument
def affichage(grille,largeur,hauteur,x=-1,y=-1,liste=[]) :
    fenetre.fill((0,0,0))
    for l in range(hauteur):
        for c in range(largeur):
            if grille[l][c]==1 :
                pygame.draw.rect(fenetre,(0,0,255),(c*taille,l*taille,taille,taille),0)
            elif grille[l][c]==2 :
                pygame.draw.rect(fenetre,(0,255,255),(c*taille,l*taille,taille,taille),0)
            elif grille[l][c]==3 :
                pygame.draw.rect(fenetre,(255,255,0),(c*taille,l*taille,taille,taille),0)
    # effet « trainée »
    degrade=0
    for centre in liste[-42:] :
        pygame.draw.circle(fenetre,(degrade*6,0,degrade*6),centre,taille//4,0)
        degrade+=1
    # perso
    pygame.draw.rect(fenetre,(255,0,255),(x*taille,y*taille,taille,taille),0)
    pygame.display.flip()
    pygame.time.delay(100)

def cartePLeineDeUns(largeur,hauteur):
    # une carte pleine de 1
    grille=[]
    for ligne in range(hauteur):
        grille.append([])
        for colonne in range(largeur):
            grille[ligne].append(1)
    return grille

def copieCarte(c,largeur,hauteur):
    copie=[]
    for ligne in range(hauteur):
        copie.append([])
        for colonne in range(largeur):
            copie[ligne].append(c[ligne][colonne])
    return copie

def origineInitiale(carte,largeur,hauteur):
    x=randrange(largeur//2)
    y=randrange(hauteur//2)
    return 2*x+1,2*y+1

def afficheCarte(carte,largeur,hauteur):
    for ligne in range(hauteur):
        for colonne in range(largeur):
            print(carte[ligne][colonne],end='')
        print()
    print()

def nbreCasesEncoreACreuser(carte,largeur,hauteur):
    somme=0
    for x in range(largeur//2) :
        for y in range(hauteur//2) :
            somme+=carte[2*y+1][2*x+1]
    return somme

def destinationsPossiblesSansZero(carte,x,y,largeur,hauteur):
    liste=[]
    if x+2<largeur-1 and carte[y][x+2]>0 :
        liste.append(0)
    if x-2>0 and carte[y][x-2]>0 :
        liste.append(2)
    if y+2<hauteur-1 and carte[y+2][x]>0 :
        liste.append(3)
    if y-2>0 and carte[y-2][x]>0 :
        liste.append(1)
    return liste

def destinationsPossiblesAvecZero(carte,x,y,largeur,hauteur):
    liste=[]
    if x+2<largeur-1 :
        liste.append(0)
    if x-2>0 :
        liste.append(2)
    if y+2<hauteur-1 :
        liste.append(3)
    if y-2>0 :
        liste.append(1)
    return liste

def nouveauCheminInitial(carte,largeur,hauteur,t):
    x,y=origineInitiale(carte,largeur,hauteur)
    carte[y][x]=0
    # Allez, un affichage !
    affichage(carte,largeur,hauteur)
    liste=destinationsPossiblesSansZero(carte,x,y,largeur,hauteur)
    while len(liste)>0 and t>0 :
        choix=choice(liste)
        if choix==0:
            carte[y][x+1]=0
            carte[y][x+2]=0
            x,y=x+2,y
        elif choix==2:
            carte[y][x-1]=0
            carte[y][x-2]=0
            x,y=x-2,y
        elif choix==1:
            carte[y-1][x]=0
            carte[y-2][x]=0
            x,y=x,y-2
        else :
            carte[y+1][x]=0
            carte[y+2][x]=0
            x,y=x,y+2
        t-=1
        liste=destinationsPossiblesSansZero(carte,x,y,largeur,hauteur)
        # Allez, un affichage !
        affichage(carte,largeur,hauteur)
    return carte
        
  
def nouveauChemin(carte,largeur,hauteur):
    x,y=origineInitiale(carte,largeur,hauteur) #pour rentrer dans while
    while carte[y][x]==0 :
        x,y=origineInitiale(carte,largeur,hauteur)
    ancienne=copieCarte(carte,largeur,hauteur)
    while ancienne[y][x]>0:
        carte[y][x]=0
        # Allez, un affichage !
        affichage(carte,largeur,hauteur)
        
        liste=destinationsPossiblesAvecZero(carte,x,y,largeur,hauteur)
        choix=choice(liste)
        if choix==0:
            carte[y][x+1]=0
            x,y=x+2,y
        elif choix==2:
            carte[y][x-1]=0
            x,y=x-2,y
        elif choix==1:
            carte[y-1][x]=0
            x,y=x,y-2
        else :
            carte[y+1][x]=0
            x,y=x,y+2
    return carte
        
def newCarte(largeur,hauteur):

    # Une grille initiale pleine de uns
    grille=cartePLeineDeUns(largeur,hauteur)
    # Allez, un affichage !
    affichage(grille,largeur,hauteur)
    #afficheCarte(grille,largeur,hauteur)

    # Une estimation de la longueur maximale du premier chemin
    # formule improvisée : un petit tiers des sommets oranges
    t=((largeur)//2*(hauteur)//2)//3

    # On creuse le chemin initial
    grille=nouveauCheminInitial(grille,largeur,hauteur,t)
    # Allez, un affichage !
    affichage(grille,largeur,hauteur)
    pygame.time.delay(1000)
    #afficheCarte(grille,largeur,hauteur)

    # Des tours de boucle
    while nbreCasesEncoreACreuser(grille,largeur,hauteur) >0 :
        grille=nouveauChemin(grille,largeur,hauteur)
        # Allez, un affichage !
        affichage(grille,largeur,hauteur)
        pygame.time.delay(300)
        #afficheCarte(grille,largeur,hauteur)
    pygame.time.delay(3000)
    return grille

def newCoord(x,y,d):
    if d==0 :   # droite
        x+=1
    elif d==1:  # bas
        y+=1
    elif d==2 : # gauche
        x-=1
    else :      # haut
        y-=1
    return x,y
    
def deplacement(grille,l,h,x,y,d):
    # on essaie plus à droite
    d=(d+1)%4
    # on récupère les nouvelles coordonnées
    c,l=newCoord(x,y,d)
    # tant que ça ne convient pas ...
    while grille[l][c]%2==1 :
        d=(d+3)%4   #on décale vers la gauche
        # on récupère alors les nouvelles coordonnées
        c,l=newCoord(x,y,d)
    # ça convient
    return d,c,l    
    

def parcours(grille,largeur,hauteur) :
    # départ
    xD=randrange(largeur//2)
    grille[0][2*xD+1]=3
    # arrivée
    xA=randrange(largeur//2)
    grille[hauteur-1][2*xA+1]=2
    #perso en dessous du départ
    x,y=2*xD+1,1
    # direction initiale
    direction=1 # bas
    # historique des positions
    listePos=[(x*taille+taille//2,y*taille+taille//2)]
    while grille[y][x]!=2 :
        # Allez, un affichage !
        affichage(grille,largeur,hauteur,x,y,listePos)
        # On bouge
        direction,x,y=deplacement(grille,largeur,hauteur,x,y,direction)
        listePos.append((x*taille+taille//2,y*taille+taille//2))
    affichage(grille,largeur,hauteur,x,y,listePos)    
    pygame.time.delay(2000)

pygame.init()

largeur = 21
hauteur = 13
taille = 42
fenetre=pygame.display.set_mode((largeur*taille,hauteur*taille))
pygame.display.set_caption("Creusons le labyrinthe et visitons le avec nos algorithmes !")

continuer=True

while continuer:
    grille=newCarte(largeur,hauteur)
    parcours(grille,largeur,hauteur)
    #gestion des événements
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer=False
        elif event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                print("touche Escape")
                continuer=False
pygame.quit()

