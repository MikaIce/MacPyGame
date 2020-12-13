#!/usr/bin/python3.8
# -*-coding:utf-8 -
"""
The class personnage manages the movement of our heroe
"""
from constantes import SPRITE_SIZE, NB_SPRITE

class Heroe():
    """
    The class Heroe has x and y positions
    (pixel and real) as an attribute.
    It takes the labyrinth as a parameter
    in order to recover the structure.
    """
    def __init__(self, labyrinth):
        """ Position in pixel: """
        self.high = 0
        self.low = 0
        """ Position in square: """
        self.sprite_x = 0
        self.sprite_y = 0
        #Labyrinth
        self.labyrinth = labyrinth

    def move(self, direction):

        """ Move to the right """
        if direction == "right":
            if self.sprite_x < NB_SPRITE -1:
                if self.labyrinth.grid[self.sprite_y][self.sprite_x+1] != "w":
                    self.sprite_x += 1
                    #Position in pixel:
                    self.high = self.sprite_x * SPRITE_SIZE

        #Move to the left
        if direction == "left":
            if self.sprite_x > 0:
                if self.labyrinth.grid[self.sprite_y][self.sprite_x-1] != "w":
                    #move of one sprite
                    self.sprite_x -= 1
                    #Position in pixel:
                    self.high = self.sprite_x * SPRITE_SIZE

        #Move to the bottom
        if direction == "bottom":
            if self.sprite_y < NB_SPRITE-1:
                if self.labyrinth.grid[self.sprite_y+1][self.sprite_x] != "w":
                    #move on one sprite
                    self.sprite_y += 1
                    #Position in pixel:
                    self.low = self.sprite_y * SPRITE_SIZE


        #Move to the top
        if direction == "up":
            if self.sprite_y > 0: #to avoid go out of the screen
                if self.labyrinth.grid[self.sprite_y-1][self.sprite_x] != "w":
                    #move on one sprite
                    self.sprite_y -= 1
                    #Position in pixel:
                    self.low = self.sprite_y * SPRITE_SIZE
