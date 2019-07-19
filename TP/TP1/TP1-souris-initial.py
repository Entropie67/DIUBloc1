import pygame
from pygame.locals import * 
# importation des constantes de configuration
from configuration import *


pygame.init()
fenetre = pygame.display.set_mode(TAILLE_FENETRE)
pygame.display.set_caption("TP1 souris coordonnees et pygame")
fenetre.fill(COULEUR_FENETRE)
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("Touche Escape")
                continuer = False
            else :
                print("Autre touche")
        elif event.type == MOUSEMOTION :
            (x, y) = event.pos
            pygame.draw.rect(fenetre, (0, 255, 0), (x-5, y-4, 10, 8), 0)
    pygame.display.flip()
    
pygame.quit()
