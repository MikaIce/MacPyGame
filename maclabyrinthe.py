#!/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
MacGyver Maze Game.
Game in which we have to move MacGyver to the Guardian through a labyrinth.
Python script
Files:
"""
from constantes import*
from classes import*


#Open game window
pygame.display.set_icon(ICONE)
pygame.display.set_caption(TITLE_WINDOW)


#MAIN
MAIN_LOOP = True
while MAIN_LOOP:

    #Load home screen
    window.blit(BLACK_GROUND, (0, 0))
    window.blit(HOME, (30, 30))
    #Reload display
    pygame.display.flip()


#HOME LOOP
    HOME_LOOP = True
    while HOME_LOOP:

        #loop delay
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #Quit the program
            if event.type == QUIT:
                print("Bye bye!")
                MAIN_LOOP = False
                HOME_LOOP = False
                GAME_LOOP = False

            #Quit home loop to enter in game loop
            if event.type == KEYDOWN and event.key == K_RETURN:

                #WELCOME TO THE GAME
                #SOUNDTRACK.stop()
                window.blit(BACKGROUND, (30, 30))
                #window.blit(WELCOME, (120, 150))
                pygame.display.flip()
                time.sleep(1)


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
        MacGyver = Heroe(labyrinth)

#GAME
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
        window.blit(MG, (MacGyver.x + 30, MacGyver.y + 30))
        #Add conditionnal display of Element

        cut.display_elements(window, MacGyver, TOOLS)
        syringe.display_elements(window, MacGyver, TOOLS)
        ether.display_elements(window, MacGyver, TOOLS)

        pygame.display.flip()


        if labyrinth.grid[MacGyver.sprite_x][MacGyver.sprite_y] == "a":

            #The gamer wins if he has the tree elements
            if len(TOOLS) < 3:

                #GAME OVER
                #window.blit(GAMEOVER, (150+30, 150+30))
                pygame.display.flip()
                time.sleep(2)

                print("You loose")
                GAME_LOOP = False

            if len(TOOLS) == 3:
                #YOU WIN
                #window.blit(WIN, (100+30, 150+30))
                pygame.display.flip()
                time.sleep(2)

                print("You win!")
                GAME_LOOP = False
