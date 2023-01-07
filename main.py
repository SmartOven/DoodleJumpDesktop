import time
import pygame
import sys
from pygame.locals import *

pygame.init()

# Variables
display_size = (530, 830)
half_display_size = (display_size[0] // 2, display_size[1] // 2)

# player_coords = (half_display_size[0], )

background = (pygame.image.load("resources/bg.png"), display_size)
player = (pygame.image.load("resources/player.png"), (48, 74))
platform = (pygame.image.load("resources/platform.png"), (94, 22))

# Display
display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Doodle Jump")


# Mapping coordinates to the normal coordinate system
def map_coords(obj_size, coords):
    return coords[0] + half_display_size[0] - obj_size[0] // 2, -coords[1] + half_display_size[1] + - obj_size[1] // 2


def render(obj, coords):
    image, size = obj[0], obj[1]
    display.blit(image, map_coords(size, coords))


def stick_to_top(obj):
    return half_display_size[1] - obj[1][1] // 2


def stick_to_bottom(obj):
    return -half_display_size[1] + obj[1][1] // 2


def stick_to_left(obj):
    return -half_display_size[0] + obj[1][0] // 2


def stick_to_right(obj):
    return half_display_size[0] - obj[1][0] // 2


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
