#!/usr/bin/python3.8
# -*-coding:utf-8 -
"""
Elements are objects of the Elements class.
They have as attribute:
 position, a name, a surface.
"""
import random
from constantes import SPRITE_SIZE

class Elements():
    """
    The Element class takes the maze as a parameter
    to retrieve the grid
    """
    def __init__(self, name, SURFACE, labyrinth):
        #Position in pixel
        self.high = 0
        self.low = 0
        #Position in square
        self.sprite_x = 0
        self.sprite_y = 0
        #Name of the elements
        self.name = name
        #Labyrinth
        self.labyrinth = labyrinth
        #Surface
        self.surface = SURFACE

    def locate_elements(self):
        """
        The locate_elements method generates
        a list of coordinates
        of empty boxes in the Labyrinth,
        a random_choice is operated on this
        list to position the element randomly.
        """
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
        self.high = self.sprite_x * SPRITE_SIZE
        self.low = self.sprite_y * SPRITE_SIZE


    def pin_elements(self):
        """
        The pin_elements method writes the name
        of the object in the Labyrinth grid
        """
        self.labyrinth.grid[self.sprite_y][self.sprite_x] = self.name

    def display_elements(self, window, macgyver, tools):
        """
        The display_element method supports the display,
        it takes macgyver as a parameter
        """
        if self.labyrinth.grid[self.sprite_y][self.sprite_x] == self.name:
            window.blit(self.surface, (self.high + 30, self.low + 30))

        if self.labyrinth.grid[macgyver.sprite_y][macgyver.sprite_x]==self.name:

            self.labyrinth.grid[macgyver.sprite_y][macgyver.sprite_x] = "0"
            tools.append(self.name)

       #display the scoreboard
        if self.name in tools:
            window.blit(self.surface, (tools.index(self.name) * SPRITE_SIZE, 0))
