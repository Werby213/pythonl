import pygame
import numpy as np
class Player:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = np.zeros((height, width))
pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Raycawsting')
clock = pygame.time.Clock()
player = Player(3, 3, np.pi/2)
world_map = Map(10, 10)
world_map.map[0] = 1
world_map.map[-1] = 1
world_map.map[:,0] = 1
world_map.map[:,-1] = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка клавиатуры
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.x += np.sin(player.dir)
        player.y += np.cos(player.dir)
    if keys[pygame.K_s]:
        player.x -= np.sin(player.dir)
        player.y -= np.cos(player.dir)
    if keys[pygame.K_a]:
        player.x += np.cos(player.dir)
        player.y -= np.sin(player.dir)
    if keys[pygame.K_d]:
        player.x -= np.cos
