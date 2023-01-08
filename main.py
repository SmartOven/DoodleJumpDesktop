import sys

import pygame.time
from pygame.locals import *

from src.parameters import fps
from src.platform import Platform
from src.player import Player
from src.render_util import *
from src.util import FramesCounter

pygame.init()
pygame.display.set_caption("Doodle Jump")

platforms = [
    Platform(Pair(100, 100)),
    Platform(Pair(-100, 100)),
    Platform(Pair(100, -100)),
    Platform(Pair(-100, -100))
]

if __name__ == "__main__":
    # Game loop
    while True:
        # Rendering
        render_background()
        Player.render()

        for platform in platforms:
            platform.render()

        # Events catching
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    Player.move_left()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    Player.move_right()

        # Updating display in 200fps
        pygame.display.update()
        pygame.time.delay(1000 // fps)
        FramesCounter.count_frames()
