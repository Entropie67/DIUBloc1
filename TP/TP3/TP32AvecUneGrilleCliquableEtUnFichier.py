import pygame  
from pygame.locals import *

# import depuis notre autre script
from TP32GestionDuFichier import ecriture,lecture

pygame.init()

largeur,hauteur = 7,5   # dimensions de la grille
taille = 60             # taille d'une case en pixels

fenetre=pygame.display.set_mode((largeur*taille,hauteur*taille))
pygame.display.set_caption("Un labyrinthe depuis un fichier texte ?")

# notre grille initiale "tableau à double entrée"
grille=[[1,1,1,1,1,0,1],
        [1,0,0,0,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,0,0,0,1],
        [1,0,1,1,1,1,1]]

#fonction permettant l'affichage de la grille, envoyée en argument
def affichage(grille) :
    fenetre.fill((0,0,0))
    for l in range(hauteur):
        for c in range(largeur):
            if grille[l][c] :
                pygame.draw.rect(fenetre,(0,0,255),(c*taille,l*taille,taille,taille),0)
    pygame.display.flip()

continuer=True

while continuer:
    
    affichage(grille)
    
    #gestion des événements
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer=False
        elif event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                print("touche Escape")
                continuer=0
            elif event.key==K_l:
                print("Lecture du fichier")
                grille,hauteur,largeur=lecture("carte.txt")
                fenetre=pygame.display.set_mode((largeur*taille,hauteur*taille))
            elif event.key==K_e:
                print("Ecriture du fichier")
                ecriture(grille,"carte.txt",hauteur,largeur)
            else :
                print("autre touche")
        elif event.type==MOUSEBUTTONDOWN : # on a cliqué !
            # le pixel du clic
            (x,y)=event.pos
            print("clic en ("+str(x)+","+str(y)+")")
            # qui correspond à la case de grille en ligne l et en colonne c
            c=x//taille
            l=y//taille
            print("case : ("+str(c)+","+str(l)+")")
            # on passe de 0 à 1 ou de 1 à 0
            grille[l][c]=1-grille[l][c]
            # affichage de la grille en console
            print(grille)
    
pygame.quit()
