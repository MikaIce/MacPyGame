#!/usr/bin/python3.8
# -*-coding:utf-8 -

import pygame
from pygame.locals import *

pygame.init()

#Constant for loops
MAIN_LOOP = True
HOME_LOOP = True
GAME_LOOP = True

#Dimensions of game window
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NB_SPRITE + 2) * SPRITE_SIZE, (NB_SPRITE + 2) * SPRITE_SIZE)

#Display video of window game
window = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "Help to Escape!"
ICONE = pygame.image.load("data/guardian.png").convert_alpha()

#Screen "home"
HOME = pygame.image.load("data/ether.png").convert()

#Screen "Welcome to the game"
WELCOME = pygame.image.load("data/lifebar.png").convert_alpha()

#Screen Pick-up Elements
PICKUP = pygame.image.load("pictures/pickup.png").convert_alpha()

#Screen Game-Over
GAMEOVER = pygame.image.load("pictures/game_over.png").convert_alpha()

#Screen You win
WIN = pygame.image.load("pictures/win.png").convert_alpha()

#Game background
BLACK_GROUND = pygame.image.load("pictures/back_ground.png").convert()
BACKGROUND = pygame.image.load("pictures/background.jpg").convert()

#kind of sprite
WALL = pygame.image.load("pictures/wall.png")
ARRIVAL = pygame.image.load("pictures/guardian.png").convert_alpha()

#kind of tools
TUBE = pygame.image.load("pictures/tube.png").convert_alpha()
ETHER = pygame.image.load("pictures/ether.png").convert_alpha()
SYRINGE = pygame.image.load("pictures/syringe.png").convert_alpha()

#Display MacGyver
MG = pygame.image.load("pictures/MacGyver.png").convert_alpha()

#variable contain map
FILE = ""

#sound
SOUNDTRACK = pygame.mixer.Sound("sound/soundtrack.wav")
JINGLE = pygame.mixer.Sound("sound/little_sound.wav")
