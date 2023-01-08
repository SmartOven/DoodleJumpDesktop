import sys

import pygame.color
from pygame.locals import *

from src.parameters import fps
from src.platform import Platforms
from src.player import Player
from src.render_util import *
from src.util import FramesCounter, Game

pygame.init()
pygame.display.set_caption("Doodle Jump")

if __name__ == "__main__":
    # Game loop
    while True:
        if not Game.is_running:
            display.fill((140, 140, 140))
            pygame.draw.line(display, (0, 0, 0), (0, 0), (100, 100))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            continue

        # Rendering
        render_background()

        Platforms.update_and_render()
        Player.update_and_render()

        # Events catching
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Moving player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    Player.is_moving_left_now()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    Player.is_moving_right_now()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    Player.is_not_moving_left_now()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    Player.is_not_moving_right_now()

        # Updating display in 200fps
        pygame.display.update()
        pygame.time.delay(1000 // fps)
        FramesCounter.count_frames()
