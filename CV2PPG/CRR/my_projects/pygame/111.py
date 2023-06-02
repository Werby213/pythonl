import pygame, sys
from pygame.locals import QUIT
from pygame import *
import random

WIDTH = 800
HEIGHT = 600
BACKGROUND = "#52a4ff"
P_WIDTH = 32
P_HEIGHT = 32
P_COLOR = "#b90b30"


def generate_level():
    level = []
    for i in range(HEIGHT // P_HEIGHT):
        row = ""
        for j in range(WIDTH // P_WIDTH):
            if i == 0 or i == HEIGHT // P_HEIGHT - 1 or j == 0 or j == WIDTH // P_WIDTH - 1:
                row += "-"
            elif random.random() < 0.1:
                row += "-"
            else:
                row += " "
        level.append(row)
    return level


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Dristnya')
    bg = Surface((WIDTH, HEIGHT))
    bg.fill(BACKGROUND)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(bg, (0, 0))
        x = y = 0
        level = generate_level()
        for row in level:
            for col in row:
                if col == "-":
                    p_block = Surface((P_WIDTH, P_HEIGHT))
                    p_block.fill(P_COLOR)
                    DISPLAYSURF.blit(p_block, (x, y))
                x += P_WIDTH
            y += P_HEIGHT
            x = 0
        pygame.display.update()


if __name__ == "__main__":
    main()
