import pygame

from random import randint
from define import *

class BALL():
    def __init__(self, imageBall) -> None:
        self.imageBall = imageBall
        self.setPositon()
    
    def setPositon(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2

        velocityX = BALL_VELOCITY_X
        velocityY = BALL_VELOCITY_Y

        position = randint(1, 4) # 1 -> Top Left, 2 -> Top Right, 3 -> Bottom Left, 4 -> Bottom Right

        if position == 1:
            velocityX = BALL_VELOCITY_X * -1
            velocityY = BALL_VELOCITY_Y * -1
        elif position == 2:
            velocityX = BALL_VELOCITY_X
            velocityY = BALL_VELOCITY_Y * -1
        elif position == 3:
            velocityX = BALL_VELOCITY_X * -1
            velocityY = BALL_VELOCITY_Y
        elif position == 4:
            velocityX = BALL_VELOCITY_X
            velocityY = BALL_VELOCITY_Y

        self.velocityX = velocityX
        self.velocityY = velocityY

    def show(self, surface):
        surface.blit(self.imageBall, (self.x - BALL_SIZE, self.y - BALL_SIZE))

    def run(self):
        self.x += self.velocityX
        self.y += self.velocityY

        if self.y - BALL_SIZE <= 0:
            self.velocityY *= -1
        if self.y + BALL_SIZE >= WINDOW_HEIGHT:
            self.velocityY *= -1
