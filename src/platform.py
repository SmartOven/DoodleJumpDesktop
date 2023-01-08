import random

import pygame

from src.display import display_size
from src.render_util import half_display_size, Pair, at_bottom_with_x, render


class Platform:
    image = pygame.image.load("resources/platform.png")
    size = Pair(94, 22)
    half_size = Pair(size.x // 2, size.y // 2)

    min_x = -half_display_size.x + half_size.x
    max_x = half_display_size.x - half_size.x
    min_y = -half_display_size.y + half_size.y
    max_y = half_display_size.y - half_size.y

    def __init__(self, coords: Pair):
        self.coords = coords

    def render(self):
        render(Platform.image, Platform.size, self.coords)


def random_coords_platform():
    return Platform(Pair(
        random.randint(Platform.min_x, Platform.max_x),
        random.randint(Platform.min_y, Platform.max_y)
    ))


def bottom_floor_platforms():
    return [
        Platform(Pair(-half_display_size.x + i * Platform.size.x, -half_display_size.y - Platform.half_size.y))
        for i in range(int(1.5 * display_size.x) // Platform.size.x)
    ]


def n_random_platforms(n):
    return [random_coords_platform() for _ in range(n)]


class Platforms:
    current_count = random.randint(8, 12)
    platforms = bottom_floor_platforms() + n_random_platforms(current_count)

    @staticmethod
    def render():
        Platforms.filter_and_add_new()
        for platform in Platforms.platforms:
            platform.render()

    @staticmethod
    def filter_and_add_new():
        filtered_platforms = []
        # Filtering
        for platform in Platforms.platforms:
            if platform.coords.y >= -display_size.y:
                filtered_platforms.append(platform)
        # Adding new
        new_platforms_count = Platforms.current_count - len(filtered_platforms)
        Platforms.platforms = filtered_platforms + n_random_platforms(new_platforms_count)
