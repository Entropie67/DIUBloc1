##############################################################
#           Corrigé du TP 01  Version avec liste             #
##############################################################

import pygame
from pygame.locals import *

# importation des constantes de configuration
from configuration import *

pygame.init()

fenetre=pygame.display.set_mode(TAILLE_FENETRE)
pygame.display.set_caption("Test souris et clavier de pygame")

rouge, vert, bleu = 0, 0, 255

fenetre.fill((rouge, vert, bleu))
liste = []
continuer = True

xclic, yclic = -100, -100

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                rouge += 16
                if rouge > 255:
                    rouge = 0
                print("Flèche vers le bas, rouge =", rouge)
            elif event.key == K_LEFT:
                vert += 16
                if vert > 255:
                    vert = 0
                print("Flèche vers la gauche, vert =", vert)
            elif event.key == K_RIGHT:
                bleu -= 16
                if bleu < 0:
                    bleu = 255
                print("Flèche vers la droite, bleu =", bleu)
            elif event.key == K_ESCAPE:
                print("Touche Escape")
                continuer = False
            else :
                print("Autre touche")

        elif event.type == MOUSEBUTTONDOWN :
            (xclic, yclic) = event.pos
            print("clic en ("+str(xclic)+","+str(yclic)+")")

        elif event.type == MOUSEMOTION :
            (x, y) = event.pos
            liste.append((x, y))

    fenetre.fill((rouge, vert, bleu))

    for centre in liste[-100:] :
        pygame.draw.rect(fenetre, COULEUR_TRAIT, (centre[0]-5,
                                                  centre[1]-5, 10, 10), 0)
    pygame.draw.circle(fenetre, COULEUR_CERCLE, (xclic, yclic), 20, 0)
    pygame.display.flip()
        
pygame.quit()
