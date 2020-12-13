#!/usr/bin/python3.8
# -*-coding:utf-8 -
"""
The class Map takes into account a .txt file
representing the different elements of the labyrinth
"""
from constantes import SPRITE_SIZE, WALL, ARRIVAL

class Map():
    """ the pygame window map. """

    def __init__(self, file):
        self.file = file
        self.grid = []

    def generate(self):
        """ the file.txt. """
        frame = []

        with open(self.file, "r") as file:
            for line in file:
                line = line.strip()
                frame.append(list(line))
        self.grid = frame

    def display(self, window):
        """
        The display method displays on the game window
        the element corresponding to "w" or "a"
        """
        num_line = 0
        for line in self.grid:
            num_sprite = 0
            for sprite in line:
                high = num_sprite * SPRITE_SIZE
                low = num_line * SPRITE_SIZE
                if sprite == "w":
                    window.blit(WALL, (high + 30, low + 30))
                if  sprite == "a":
                    window.blit(ARRIVAL, (high + 30, low + 30))
                num_sprite += 1
            num_line += 1
