#!/usr/bin/python3.8
# -*-coding:utf-8 -*
"""
the constants file contains the images
and display settings.
"""

import pygame

# Constant for loops
MAIN_LOOP = True
HOME_LOOP = True
GAME_LOOP = True

# Dimensions of game window
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NB_SPRITE + 2) * SPRITE_SIZE, (NB_SPRITE + 2) * SPRITE_SIZE)

# Display video of window game
window = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "MacGyver"
ICONE = pygame.image.load("data/MacGyver_Logo.png").convert_alpha()

# Screen "home"
HOME = pygame.image.load("data/Acceuil.png").convert()

# Screen Game-Over
GAMEOVER = pygame.image.load("data/youlose.png").convert_alpha()

# Screen You win
WIN = pygame.image.load("data/youwin.png").convert_alpha()

# Game background
BLACK_GROUND = pygame.image.load("data/Backwindow.png").convert()
BACKGROUND = pygame.image.load("data/Back.png").convert()

# kind of sprite
WALL = pygame.image.load("data/Wall.png")
ARRIVAL = pygame.image.load("data/guardian.png").convert_alpha()

# kind of tools
CUT = pygame.image.load("data/Cut.png").convert_alpha()
ETHER = pygame.image.load("data/Ether.png").convert_alpha()
SYRINGE = pygame.image.load("data/Seringue.png").convert_alpha()

# Display MacGyver
MG = pygame.image.load("data/MacGyver.png").convert_alpha()

# Map
FILE = ""
