import pygame

from src.render_util import at_bottom_with_x, render
from src.util import Pair, FramesCounter
from src.parameters import horizontal_player_movement, vertical_player_movement, fps, half_fps


class Player:
    image = pygame.image.load("resources/player.png")
    size = Pair(48, 74)
    half_size = Pair(size.x // 2, size.y // 2)
    coords = at_bottom_with_x(size, 0)

    @staticmethod
    def set_coords(coords: Pair):
        Player.coords = coords

    @staticmethod
    def move_left():
        Player.coords.x -= horizontal_player_movement

    @staticmethod
    def move_right():
        Player.coords.x += horizontal_player_movement

    @staticmethod
    def move_up():
        Player.coords.y += vertical_player_movement

    @staticmethod
    def move_down():
        Player.coords.y -= vertical_player_movement

    @staticmethod
    def render():
        render(Player.image, Player.size, Player.coords)
        Player.animate()

    @staticmethod
    def animate():
        if FramesCounter.frame < half_fps:
            Player.move_up()
        else:
            Player.move_down()
