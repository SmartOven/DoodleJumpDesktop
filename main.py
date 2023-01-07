import sys
from pygame.locals import *

from src.player import Player
from src.render import *

pygame.init()
pygame.display.set_caption("Doodle Jump")

player = Player(pygame.image.load("resources/player.png"), (48, 74))
platform = (pygame.image.load("resources/platform.png"), (94, 22))

if __name__ == "__main__":
    # Game loop
    while True:
        render_background()
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
