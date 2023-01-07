import pygame
import sys
from pygame.locals import *
from util import display_size, half_display_size
from util import render, stick_to_top, stick_to_bottom, stick_to_left, stick_to_right

pygame.init()
pygame.display.set_caption("Doodle Jump")

background = (pygame.image.load("resources/bg.png"), display_size)
player = (pygame.image.load("resources/player.png"), (48, 74))
platform = (pygame.image.load("resources/platform.png"), (94, 22))

if __name__ == "__main__":
    # Game loop
    while True:
        render(background, (0, 0))
        render(player, (0, 0))
        render(platform, (100, 100))
        render(platform, (-100, 100))
        render(platform, (100, -100))
        render(platform, (-100, -100))
        render(player, (stick_to_left(player), stick_to_top(player)))
        render(player, (stick_to_left(player), stick_to_bottom(player)))
        render(player, (stick_to_right(player), stick_to_top(player)))
        render(player, (stick_to_right(player), stick_to_bottom(player)))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
