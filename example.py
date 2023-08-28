import keyboard

import pgt

# Initialize the game
game = pgt.PGT(700, 450)
game.set_background_color("gray")

# Key bindings
game.set_up_key("w")
game.set_down_key("s")
game.set_left_key("a")
game.set_right_key("d")

# Bad way to create a sprite
game.create_sprite("test_sprite", 200, 200, 4, True, game)
game.create_sprite("test_sprite", 200, 200, 6, True, game)
game.create_sprite("test_sprite", 200, 200, 8, True, game)
game.create_sprite("test_sprite", 200, 200, 10, True, game)
game.create_sprite("test_sprite", 200, 200, 12, True, game)
game.create_sprite("test_sprite", 200, 200, 14, True, game)

# Good way to create a sprite
player_sprite = pgt.Sprite()
player_sprite.image = "test_sprite"  # Required
player_sprite.xPos = 200
player_sprite.yPos = 200
player_sprite.speed = 16
player_sprite.isControlled = True    # Required
player_sprite.gameClass = game       # Required
game.add_sprite(player_sprite)

# Main loop
running = True

while running:
    # * IMPORTANT *
    # Directly copy everything in this loop
    pg = game.pygame
    game.repaint()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    game.set_current_key(keyboard.read_key())
