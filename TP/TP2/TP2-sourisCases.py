import pygame  
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Des cases ?")

fenetre.fill((255, 255, 255))

continuer = True

# notre grille "tableau à double entrée"
grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

while continuer:
    for i in range(9):
        c = i // 3      # cette astuce d'affichage devra certainement être
        l = i % 3       # expliquée aux élèves plusieurs fois ;-)
        # la lecture dans le tableau se fait avec la ligne d'abord
        # colonne = c et ligne = l
        gris = grille[l][c]   # on se cantonne au niveaux de gris ici
        # le dessin du rectangle en niveaux de gris
        pygame.draw.rect(fenetre,(gris, gris, gris), (c*200, l*100, 200, 100), 0)

    #gestion des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("touche Escape")
                continuer = 0
            else:
                print("autre touche")
        elif event.type == MOUSEBUTTONDOWN : # on a cliqué !
            # le pixel du clic
            (x, y) = event.pos
            print("clic en ("+str(x)+","+str(y)+")")
            # qui correspond à une des neuf cases
            c = x//200
            l = y//100
            print("case : ("+str(c)+","+str(l)+")")
            # on augmente l'intensité
            grille[l][c] += 50
            # on teste si on dépasse les bornes des limites
            # on aurait pu faire grille[l][c]=(grille[l][c]+50)%300
            if grille[l][c] > 255:
                grille[l][c] = 0
            # affichage de la grille pour comprendre quelque chose
            # à la choucroute
            print(grille)
    # mise à jour de l'affichage
    pygame.display.flip()
pygame.quit()
