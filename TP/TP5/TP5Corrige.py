import pygame  
from pygame.locals import *
from random import randrange,choice
from TP4CarteALeatoire import newCarte

#fonction permettant l'affichage de la grille, envoyée en argument
def affichage(grille,largeur,hauteur,x,y) :
    fenetre.fill((0,0,0))
    for l in range(hauteur):
        for c in range(largeur):
            if grille[l][c]==1 :
                pygame.draw.rect(fenetre,(0,0,255),(c*taille,l*taille,taille,taille),0)
            elif grille[l][c]==2 :
                pygame.draw.rect(fenetre,(0,255,255),(c*taille,l*taille,taille,taille),0)
            elif grille[l][c]==3 :
                pygame.draw.rect(fenetre,(255,255,0),(c*taille,l*taille,taille,taille),0)
    # perso
    pygame.draw.rect(fenetre,(255,0,255),(x*taille,y*taille,taille,taille),0)
    pygame.display.flip()
    pygame.time.delay(100)

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
        affichage(grille,largeur,hauteur,x,y)
        # On bouge
        direction,x,y=deplacement(grille,largeur,hauteur,x,y,direction)
        listePos.append((x*taille+taille//2,y*taille+taille//2))
    affichage(grille,largeur,hauteur,x,y)    
    pygame.time.delay(2000)

pygame.init()

largeur = 21
hauteur = 13
taille = 42
fenetre=pygame.display.set_mode((largeur*taille,hauteur*taille))
pygame.display.set_caption("Parcours en profondeur -> toujours à droite !")

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

