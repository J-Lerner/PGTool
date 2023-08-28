import pygame as pg

pg.init()

running = False
gameClass = None


def start(game):


    global running
    running = True
    gameClass = game


def end():
    global running
    running = False


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()


class PGT:
    def __init__(self, windowXSize, windowYSize):
        self.winX = windowXSize
        self.winY = windowYSize

        self.screen = pg.display.set_mode((self.winX, self.winY))

        test_sprite = Sprite()
        test_sprite.xPos = 2
        self.sprites = [test_sprite]

    def setBackgroundColor(self, color):
        self.screen.fill(color)

    def repaint(self):
        for sprite in self.sprites:
            self.screen.blit(sprite.image, (sprite.xPos, sprite.yPos))


class Sprite:
    xPos: 0
    yPos: 0
    image: ""
