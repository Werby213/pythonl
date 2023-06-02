import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_UP, K_LEFT, K_RIGHT
import random
from player import *
from block import *
from camera import *

WIDTH = 800
HEIGHT = 640
BACKGROUND = "#52a4ff"

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Dristnya')
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill(pygame.Color(BACKGROUND))
    level = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-            --         -",
        "-                       -",
        "--                      -",
        "-                       -",
        "-                   --- -",
        "-                       -",
        "-                       -",
        "-      ---              -",
        "-                       -",
        "-   -----------         -",
        "-                       -",
        "-                -      -",
        "-                   --  -",
        "-                       -",
        "-                       -",
        "-------------------------"
    ]
    all_objects = pygame.sprite.Group()
    platforms = []
    for y, row in enumerate(level):
        for x, col in enumerate(row):
            if col == "-":
                platforms.append(Platform(x * P_WIDTH, y * P_HEIGHT))
                for platform in platforms:
                    all_objects.add(platform)
    player = Player(55, 55)
    all_objects.add(player)

    camera = Camera(Camera.camera_conf, WIDTH, HEIGHT)

    left = right = up = False
    timer = pygame.time.Clock()
    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYUP and event.key == K_LEFT:
                left = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False

        DISPLAYSURF.blit(bg, (0, 0))
        all_objects.update(left, right, up, platforms)

        camera.update(player)  # Update the camera's position based on the player's position

        for obj in all_objects:
            DISPLAYSURF.blit(obj.image, camera.apply(obj))  # Apply camera movement to each game object

        pygame.display.update()


if __name__ == "__main__":
    main()
