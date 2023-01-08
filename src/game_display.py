import pygame

from src.util import Pair

background_image = pygame.image.load("resources/bg.png")
display_size = Pair(530, 830)
half_display_size = Pair(display_size.x // 2, display_size.y // 2)

display = pygame.display.set_mode((display_size.x, display_size.y))
