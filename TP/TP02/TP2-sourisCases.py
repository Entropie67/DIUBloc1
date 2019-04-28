##############################################################
#                       Corrigé du TP 02                     #
##############################################################
import pygame
from pygame.locals import *
# importation des constantes de configuration
from configuration import *

pygame.init()

fenetre = pygame.display.set_mode(TAILLE_FENETRE)
pygame.display.set_caption("Des cases ?")

fenetre.fill(COULEUR_FENETRE)

continuer = True

grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

x = 0
y = 0

while continuer:
        for i in range(9):
                x1 = i // 3
                y1 = i % 3
                rectangle = pygame.draw.rect(
                        fenetre, (grille[y1][x1], grille[y1][x1],
                                  grille[y1][x1]), (x1 * 200, y1 * 100,
                                                    200, 100), 0)
        #gestion des événements
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = False
                elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                print("Touche Escape")
                                continuer = 0
                        else :
                                print("Autre touche")
                elif event.type == MOUSEBUTTONDOWN :
                        (x, y) = event.pos
                        print("Clic en ("+str(x)+", "+str(y)+")")
                        x2 = x // 200
                        y2 = y // 100
                        print("Clic en ("+str(x2)+", "+str(y2)+")")
                        grille[y2][x2] += 50
                        if grille[y2][x2] > 255:
                                grille[y2][x2] = 0
                        print(grille)
        pygame.display.flip()
pygame.quit()
