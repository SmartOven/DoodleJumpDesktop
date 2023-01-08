from src.display import *


# Mapping coordinates to the normal coordinate system
def map_coords(obj_size: Pair, coords: Pair):
    return coords.x + half_display_size.x - obj_size.x // 2, \
           -coords.y + half_display_size.y + - obj_size.y // 2


def render_background():
    display.blit(background_image, (0, 0))


def render(image, size, coords: Pair):
    display.blit(image, map_coords(size, coords))


def top_coord(obj_size: Pair):
    return half_display_size.y - obj_size.y // 2


def bottom_coord(obj_size: Pair):
    return -half_display_size.y + obj_size.y // 2


def left_coord(obj_size: Pair):
    return -half_display_size.x + obj_size.x // 2


def right_coord(obj_size: Pair):
    return half_display_size.x - obj_size.x // 2


def at_top_with_x(obj_size: Pair, x):
    return Pair(x, top_coord(obj_size))


def at_bottom_with_x(obj_size: Pair, x):
    return Pair(x, bottom_coord(obj_size))


def at_left_with_y(obj_size: Pair, y):
    return Pair(left_coord(obj_size), y)


def at_right_with_y(obj_size: Pair, y):
    return Pair(right_coord(obj_size), y)
