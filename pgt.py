import datetime

import pygame as pg

pg.init()

gameClass = None


class PGT:
    def __init__(self, window_x_size, window_y_size):
        self.winX = window_x_size
        self.winY = window_y_size

        self.pygame = pg
        self.screen = pg.display.set_mode((self.winX, self.winY))

        self.sprites = []

    def set_background_color(self, color):
        self.screen.fill(color)

    def repaint(self):
        for sprite in self.sprites:
            self.screen.blit(sprite.image, (sprite.xPos, sprite.yPos))


class Sprite:
    xPos: 0
    yPos: 0
    image: ""
