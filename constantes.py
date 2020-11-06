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
TITLE_WINDOW = "MacGyver"
ICONE = pygame.image.load("data/").convert_alpha()

#Screen "home"
HOME = pygame.image.load("data/").convert()

#Screen "Welcome to the game"
WELCOME = pygame.image.load("data/").convert_alpha()

#Screen Pick-up Elements
PICKUP = pygame.image.load("data/").convert_alpha()

#Screen Game-Over
GAMEOVER = pygame.image.load("data/").convert_alpha()

#Screen You win
WIN = pygame.image.load("data/").convert_alpha()

#Game background
BLACK_GROUND = pygame.image.load("data/").convert()
BACKGROUND = pygame.image.load("data/").convert()

#kind of sprite
WALL = pygame.image.load("data/")
ARRIVAL = pygame.image.load("data/").convert_alpha()

#kind of tools
TUBE = pygame.image.load("data/").convert_alpha()
ETHER = pygame.image.load("data/").convert_alpha()
SYRINGE = pygame.image.load("data/").convert_alpha()

#Display MacGyver
MG = pygame.image.load("data/").convert_alpha()
