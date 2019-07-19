def ecriture(grille,nom,hauteur,largeur):
    with open(nom, "w") as fichier:
        for ligne in range(hauteur):  # parcours de la carte
            for colonne in range(largeur): # parcours de la carte
                fichier.write(str(grille[ligne][colonne]))
            fichier.write("\n")
        fichier.close()

def lecture(nom):
    structure_niveau=[]
    with open(nom, "r") as fichier:
        for ligne in fichier:
            ligne_niveau = []
            #On parcourt les sprites (lettres) contenus dans le fichier
            for sprite in ligne:
                #On ignore les "\n" de fin de ligne
                if sprite != '\n':
                    #On ajoute le sprite à la liste de la ligne
                    ligne_niveau.append(int(sprite))
            #On ajoute la ligne à la liste du niveau si elle n'est pas vide
            if len(ligne_niveau)>0:
                structure_niveau.append(ligne_niveau)
    hauteur=len(structure_niveau)
    largeur=0
    if hauteur > 0:
        largeur = len(structure_niveau[0])
    return structure_niveau,hauteur,largeur
    

