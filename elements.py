#!/usr/bin/python3.8
# -*-coding:utf-8 -

import random
import time

from constantes import*

class Elements():

    def __init__(self, name, SURFACE, labyrinth):
        #Position in pixel:
        self.x = 0
        self.y = 0
        #Position in square:
        self.sprite_x = 0
        self.sprite_y = 0
        #Name of the elements
        self.name = name
        #Labyrinth
        self.labyrinth = labyrinth
        #Surface
        self.surface = SURFACE

    def locate_elements(self):

        position = []
        coordinates = ()
        num_line = 0
        while num_line < len(self.labyrinth.grid):
            num_cell = 1
            while num_cell < len(self.labyrinth.grid[0]):
                if self.labyrinth.grid[num_line][num_cell] == "0":
                    coordinates = (num_line, num_cell)
                    position.append(coordinates)
                num_cell += 1
            num_line += 1

        element_coordinates = random.choice(position)
        self.sprite_y = element_coordinates[0]
        self.sprite_x = element_coordinates[1]
        self.x = self.sprite_x * SPRITE_SIZE
        self.y = self.sprite_y * SPRITE_SIZE


    def pin_elements(self):

        self.labyrinth.grid[self.sprite_y][self.sprite_x] = self.name

    def display_elements(self, window, MacGyver, TOOLS):

        if self.labyrinth.grid[self.sprite_y][self.sprite_x] == self.name:
            window.blit(self.surface, (self.x + 30, self.y + 30))

        if self.labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x]==self.name:

            #print("Yeah! You caught the {}!".format(self.name))
            self.labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append(self.name)

       # display the scoreboard
        if self.name in TOOLS:
            window.blit(self.surface, (TOOLS.index(self.name) * SPRITE_SIZE, 0))
