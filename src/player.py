import pygame

from src.display import half_display_size
from src.render_util import at_bottom_with_x, render
from src.util import Pair, FramesCounter
from src.parameters import horizontal_player_movement, vertical_player_movement, fps, half_fps


class Player:
    image = pygame.image.load("resources/player.png")
    size = Pair(48, 74)
    half_size = Pair(size.x // 2, size.y // 2)
    coords = at_bottom_with_x(size, 0)
    moving_left = False
    moving_right = False

    @staticmethod
    def is_moving_left_now():
        Player.moving_left = True
        Player.moving_right = False

    @staticmethod
    def is_moving_right_now():
        Player.moving_left = False
        Player.moving_right = True

    @staticmethod
    def is_not_moving_left_now():
        Player.moving_left = False

    @staticmethod
    def is_not_moving_right_now():
        Player.moving_right = False

    @staticmethod
    def move():
        if Player.moving_left:
            move_player_left()
        elif Player.moving_right:
            move_player_right()

    @staticmethod
    def render():
        render(Player.image, Player.size, Player.coords)
        Player.move()
        Player.animate()

    @staticmethod
    def animate():
        if FramesCounter.frame < half_fps:
            move_player_up()
        else:
            move_player_down()


def move_player_left():
    Player.coords.x -= horizontal_player_movement
    if Player.coords.x <= -half_display_size.x - Player.half_size.x:
        Player.coords.x = half_display_size.x


def move_player_right():
    Player.coords.x += horizontal_player_movement
    if Player.coords.x >= half_display_size.x + Player.half_size.x:
        Player.coords.x = -half_display_size.x


def move_player_up():
    Player.coords.y += vertical_player_movement


def move_player_down():
    Player.coords.y -= vertical_player_movement
