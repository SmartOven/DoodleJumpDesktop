import pygame

display_size = (530, 830)
half_display_size = (display_size[0] // 2, display_size[1] // 2)

display = pygame.display.set_mode(display_size)


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
