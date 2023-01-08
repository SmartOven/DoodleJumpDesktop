import random

import pygame

from src.render_util import half_display_size, Pair, at_bottom_with_x, render


class Platform:
    image = pygame.image.load("resources/platform.png")
    size = Pair(94, 22)
    half_size = Pair(size.x // 2, size.y // 2)
    coords = at_bottom_with_x(size, 0)

    min_x = -half_display_size.x + half_size.x
    max_x = half_display_size.x - half_size.x
    min_y = -half_display_size.y + half_size.y
    max_y = half_display_size.y - half_size.y

    def __init__(self, coords: Pair):
        self.coords = coords

    @staticmethod
    def set_coords(coords: Pair):
        Platform.coords = coords

    def render(self):
        render(Platform.image, Platform.size, self.coords)


def random_platform_coords():
    random.randint(0, 1)
