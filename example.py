import keyboard

import pgt

game = pgt.PGT(700, 450)
game.set_background_color("gray")
game.set_up_key("w")

game.create_sprite("test_sprite", 5, 5, 4, True, game)

running = True


while running:
    pg = game.pygame
    game.repaint()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    game.set_current_key(keyboard.read_key())
    print(keyboard.read_key())
