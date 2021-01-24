#!/usr/bin/python3.8
# -*- coding: Utf-8 -*
"""
MacGyver Maze Game.
Game in which we have to move MacGyver to the Guardian through a labyrinth.
Python script
Files:
"""

import time
import pygame

from constantes import ICONE, TITLE_WINDOW, BLACK_GROUND, SCREEN_SIZE, HOME, \
 BACKGROUND, SYRINGE, ETHER, CUT, GAMEOVER, WIN, MG
from personnage import Heroe
from elements import Elements
from map import Map
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_ESCAPE, K_RIGHT, K_LEFT, \
K_DOWN, K_UP

def main():
    #Open game window
    pygame.display.set_icon(ICONE)
    pygame.display.set_caption(TITLE_WINDOW)
    window = pygame.display.set_mode(SCREEN_SIZE)

    #MAIN
    MAIN_LOOP = True
    while MAIN_LOOP:

        window.blit(BLACK_GROUND, (0, 0))
        window.blit(HOME, (30, 30))
        #Reload display
        pygame.display.flip()

    #HOME LOOP
        HOME_LOOP = True
        while HOME_LOOP:

            #loop delay
            pygame.time.Clock().tick(10)

            for event in pygame.event.get():
                #Quit the program
                if event.type == QUIT:
                    print("Bye bye!")
                    MAIN_LOOP = False
                    HOME_LOOP = False
                    GAME_LOOP = False

                #Quit home loop to enter in game loop
                if event.type == KEYDOWN and event.key == K_RETURN:

                    HOME_LOOP = False
                    GAME_LOOP = True

                    #Load the game's map
                    FILE = "map/N1.txt"

        if FILE != "":

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

            cut = Elements("cut", CUT, labyrinth)
            cut.locate_elements()
            cut.pin_elements()

            #And God create an Heroe
            macgyver = Heroe(labyrinth)

    #GAME
        tools = []
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
                        macgyver.move("right")
                    if event.key == K_LEFT:
                        macgyver.move("left")
                    if event.key == K_DOWN:
                        macgyver.move("bottom")
                    if event.key == K_UP:
                        macgyver.move("up")

            #Display the game board
            window.blit(BACKGROUND, (0+30, 0+30))
            labyrinth.display(window)

            #Add MacGyver in the Labyrinth with his position
            window.blit(MG, (macgyver.high + 30, macgyver.low + 30))
            #Add conditionnal display of Element

            cut.display_elements(window, macgyver, tools)
            syringe.display_elements(window, macgyver, tools)
            ether.display_elements(window, macgyver, tools)

            pygame.display.flip()


            if labyrinth.grid[macgyver.sprite_x][macgyver.sprite_y] == "a":

                #The gamer wins if he has the tree elements
                if len(tools) < 3:

                    #GAME OVER
                    window.blit(GAMEOVER, (30, 30))
                    pygame.display.flip()
                    time.sleep(2)

                    print("You loose")
                    GAME_LOOP = False

                if len(tools) == 3:
                    #YOU WIN
                    window.blit(WIN, (30, 30))
                    pygame.display.flip()
                    time.sleep(2)

                    print("You win!")
                    GAME_LOOP = False




if __name__ == "__main__":
    main()
