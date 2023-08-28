import pgt


game = pgt.PGT(700, 450)
game.set_background_color("white")

running = True


while running:
    pg = game.pygame
    game.repaint()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
