# Emilie Mancera
# Exercice1

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.AFRICAN_VIOLET, arcade.color.AMARANTH_PINK,
arcade.color.ARYLIDE_YELLOW, arcade.color.BLEU_DE_FRANCE]

def on_update(self):
    if cercle_x < rayon_cercle:
        cercle_x *= -1
    if cercle_x > SCREEN_WIDTH - rayon_cercle:
        cercle_x *= -1
    if cercle_y < rayon_cercle:
        cercle_y *= -1
    if cercle_y > SCREEN_HEIGHT - rayon_cercle:
        cercle_y *= -1

def on_draw(self):
   arcade.start_render()
   arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.liste_cercles = []

    def cercles(self):
        for _ in range(20)
        ####

def main():
    my_game = MyGame(800, 600)
    arcade.run()

main()