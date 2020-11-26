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
