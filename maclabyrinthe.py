# !/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MacGyver Maze Game.
Game in which we have to move MacGyver to the Guardian through a labyrinth.
Python script
Files:
"""
import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

# Open windows pygame (sqare : width = height)
fenetre = pygame.display.set_mode((side_windows, side_windows))
# Icone
icone = pigame.image.load(image_icone)
pygame.display.set_icon(icone)
# Title
pygame.display.set_caption(title_windows)
#BOUCLE PRINCIPALE
continuer = 1
while continuer:
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN
			and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0

		       # elif event.type == KEYDOWN:
				#Lancement du niveau
			#	if event.key == K_F1:
			#		continuer_accueil = 0	#On quitte l'accueil
			#		choix = 'n1'		#On définit le niveau à charger
				#Lancement du niveau 2
			#	elif event.key == K_F2:
			#		continuer_accueil = 0
			#		choix = 'n2'



	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
#	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load().convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de MacGyver
		mg = Perso()


	#BOUCLE DE JEU
	while continuer_jeu:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0

			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0

				#Touches de déplacement de MacGyver
				elif event.key == K_RIGHT:
					mg.deplacer('droite')
				elif event.key == K_LEFT:
					mg.deplacer('gauche')
				elif event.key == K_UP:
					mg.deplacer('haut')
				elif event.key == K_DOWN:
					mg.deplacer('bas')

		#Affichages aux nouvelles positions
		windows.blit(fond, (0,0))
		niveau.afficher(windows)
		windows.blit(dk.direction, (mg.x, mg.y))
        #mg.direction = l'image dans la bonne direction

        pygame.display.flip()

		#Victoire -> Retour à l'accueil
		if niveau.structure[mg.case_y][mg.case_x] == 'a':
			continuer_jeu = 0
