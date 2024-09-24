import pygame

from define import *

class PLAYER():
    def __init__(self, imagePlayer, x, y) -> None:
        self.x = x
        self.y = y
        self.imagePlayer = imagePlayer
        self.score = 0

    def show(self, surface):
        surface.blit(self.imagePlayer, (self.x, self.y))

    def moveUp(self):
        self.y -= PLAYER_VELOCITY
        if self.y < 0:
            self.y = 0

    def moveDown(self):
        if self.y + PLAYER_HEIGHT < WINDOW_HEIGHT:
            self.y += PLAYER_VELOCITY

'''
    Player left: W -> Up, S -> Down
    Player right: ^[[A -> Up, ^[[B -> Down
'''
