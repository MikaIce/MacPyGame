#!/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
MacGyver Maze Game.
Game in which we have to move MacGyver to the Guardian through a labyrinth.
Python script
Files:
"""
import pygame

from classes import *
from constantes import *

# Open window pygame
pygame.display.set_icon(ICON)
pygame.display.set_caption(TITLE_WINDOW)

# Main loop
main_loop = True
while main_loop:

	# Load home screen
	window.blit(black_ground, (0, 0))
	window.blit(home, (30, 30))
	# Reload display
	pygame.display.flip()

	# Home loop
	home_loop = True
	while home_loop:

		# Time loop
		pygame.time.clock().tick(30)
		for event in pygame.event.get():
			# Exit the program
			if event.type == quit:
				print("See you later")
				main_loop = False
				home_loop = False
				Game_loop = False

			# Enter in the game loop
			if event.type == KEYDOWN and envent.key == K_RETURN:
				# enter the Game
				window.blit(BACKGROUND, (30, 30))
                window.blit(WELCOME, (120, 150))
                pygame.display.flip()
                time.sleep(1)

				HOME_LOOP = False
                GAME_LOOP = True

                #Load the game's map
                FILE = "map/N1.txt"

    if FILE != "": #We make sure that the file really exists and is not empty

        #load the background
        window.blit(BACKGROUND, (30, 30))

        #generate the labyrinth
        labyrinth = Map(FILE)
        labyrinth.generate()
        labyrinth.display(window)

        #Get the items in the labyrinthe

        syringe = Elements("syringe", SYRINGE, labyrinth)
        syringe.locate_elements()
        syringe.pin_elements()

        ether = Elements("ether", ETHER, labyrinth)
        ether.locate_elements()
        ether.pin_elements()

        tube = Elements("tube", TUBE, labyrinth)
        tube.locate_elements()
        tube.pin_elements()

        #And God create an Heroe
    	MacGyver = Heroe(labyrinth)

    #Initialyse at every game_loop an empty list to put the elements inside
    TOOLS = []
    while  GAME_LOOP:

        pygame.time.Clock().tick(30)
        for event in pygame.event.get():

            #Quit the program
            if event.type == QUIT:
                print("Bye bye!")
                MAIN_LOOP = False
                GAME_LOOP = False

            if event.type == KEYDOWN:

                #Quit the game and go back Home
                if event.key == K_ESCAPE:
                    GAME_LOOP = False

                #Move our heroe!
                if event.key == K_RIGHT:
                    MacGyver.move("right")
                if event.key == K_LEFT:
                    MacGyver.move("left")
                if event.key == K_DOWN:
                    MacGyver.move("bottom")
                if event.key == K_UP:
                    MacGyver.move("up")

        #Display the game board
        window.blit(BACKGROUND, (0+30, 0+30))
        labyrinth.display(window)

        #Add MacGyver in the Labyrinth with his position
        window.blit(MG, (MacGyver.x + 30, MacGyver.y + 30)) # + 30 for the offset of the black outline

        #Add conditionnal display of Element

        tube.display_elements(window, MacGyver, TOOLS)
        syringe.display_elements(window, MacGyver, TOOLS)
        ether.display_elements(window, MacGyver, TOOLS)

        pygame.display.flip()


        if labyrinth.grid[MacGyver.sprite_x][MacGyver.sprite_y] == "a":

            #The gamer wins if he has the tree elements
            if len(TOOLS) < 3:

                #DISPLAY GAME OVER
                window.blit(GAMEOVER, (150+30, 150+30))
                pygame.display.flip()
                time.sleep(2)

                print("You loose")
                GAME_LOOP = False

            if len(TOOLS) == 3:
                #DISPLAY YOU WIN
                window.blit(WIN, (100+30, 150+30))
                pygame.display.flip()
                time.sleep(2)

                print("You win!")
                GAME_LOOP = False
