import datetime
import os

import pygame
import pygame as pg

pg.init()

gameClass = None


class PGT:
    def __init__(self, window_x_size, window_y_size):
        self.winX = window_x_size
        self.winY = window_y_size

        self.pygame = pg
        self.screen = pg.display.set_mode((self.winX, self.winY))

        self.current_key = ""
        self.movement_keys = {
            "up": (0, 1),
            "down": (0, -1),
            "left": (-1, 0),
            "right": (1, 0)
        }
        self.sprites = []
        self.bg_color = "white"

    def set_background_color(self, color):
        self.bg_color = color

    def create_sprite(self, image_name, x_pos, y_pos, speed, is_controlled, game_class):
        new_sprite = Sprite()
        new_sprite.image = image_name
        new_sprite.xPos = x_pos
        new_sprite.yPos = y_pos
        new_sprite.speed = speed
        new_sprite.isControlled = is_controlled
        new_sprite.gameClass = game_class
        self.sprites.append(new_sprite)

    def set_current_key(self, key):
        self.current_key = key

    def set_up_key(self, key):
        self.movement_keys[0] = key

    def set_down_key(self, key):
        self.movement_keys[1] = key

    def set_left_key(self, key):
        self.movement_keys[2] = key

    def set_right_key(self, key):
        self.movement_keys[3] = key

    def repaint(self):
        self.screen.fill(self.bg_color)

        for sprite in self.sprites:
            if sprite.isControlled:
                sprite.check_move(self.current_key)

            self.screen.blit(pygame.image.load(os.path.join("textures\\" + sprite.image + ".png")),
                             (sprite.xPos, sprite.yPos))

        pg.display.flip()


class Sprite:
    image: ""
    xPos: 0
    yPos: 0
    speed: 1
    isControlled: True
    gameClass: PGT

    def check_move(self, key):
        if key in self.gameClass.movement_keys:
            self.xPos += self.gameClass.movement_keys[key][0] * self.speed
            self.yPos += self.gameClass.movement_keys[key][1] * -self.speed
