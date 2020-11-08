#!/usr/bin/python3.8
# -*-coding:utf-8 -

import random
import time

from constantes import*

class Map():
    #the pygame window.

    def __init__(self, file):
        self.file = file
        self.grid = []

    def generate(self):
        #the file.txt.
        frame = []

        with open(self.file, "r") as file:
            for line in file:
                line = line.strip()
                frame.append(list(line))
        self.grid = frame

    def display(self, window):

        num_line = 0
        for line in self.grid:
            num_sprite = 0
            for sprite in line:
                X = num_sprite * SPRITE_SIZE
                Y = num_line * SPRITE_SIZE
                if sprite == "w":
                    window.blit(WALL, (X + 30, Y + 30))
                if  sprite == "a":
                    window.blit(ARRIVAL, (X + 30, Y + 30))
                num_sprite += 1
            num_line += 1

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

        if self.labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] == self.name:

            #dysplay the pick-up of the elements
            #window.blit(PICKUP, (90 + 30, 120 + 30))
            pygame.display.flip()
            #JINGLE.play()
            time.sleep(1)

            print("Yeah! You caught the {}!".format(self.name))
            self.labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append(self.name)

       # display the scoreboard
        if self.name in TOOLS:
            window.blit(self.surface, (TOOLS.index(self.name) * SPRITE_SIZE, 0))



class Heroe():

    def __init__(self, labyrinth):
        #Position in pixel:
        self.x = 0
        self.y = 0
        #Position in square:
        self.sprite_x = 0
        self.sprite_y = 0
        #Labyrinth
        self.labyrinth = labyrinth

    def move(self, direction):

        #Move to the right
        if direction == "right":
            if self.sprite_x < NB_SPRITE -1:
                if self.labyrinth.grid[self.sprite_y][self.sprite_x+1] != "w":
                    self.sprite_x += 1
                    #Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE

        #Move to the left
        if direction == "left":
            if self.sprite_x > 0:
                if self.labyrinth.grid[self.sprite_y][self.sprite_x-1] != "w":
                    #move of one sprite
                    self.sprite_x -= 1
                    #Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE

        #Move to the bottom
        if direction == "bottom":
            if self.sprite_y < NB_SPRITE-1:
                if self.labyrinth.grid[self.sprite_y+1][self.sprite_x] != "w":
                    #move on one sprite
                    self.sprite_y += 1
                    #Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE


        #Move to the top
        if direction == "up":
            if self.sprite_y > 0: #to avoid go out of the screen
                if self.labyrinth.grid[self.sprite_y-1][self.sprite_x] != "w":
                    #move on one sprite
                    self.sprite_y -= 1
                    #Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE
