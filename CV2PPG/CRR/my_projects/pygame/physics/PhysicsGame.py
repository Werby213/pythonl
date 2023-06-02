import pygame
import pymunk
import random

# инициализируем pygame
pygame.init()

# определяем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SAND_GRAIN_SIZE = 5
SAND_DENSITY = 0.2
SAND_FRICTION = 1.0
BACKGROUND_COLOR = (255, 255, 255)
SAND_COLOR = (194, 178, 128)
GRAVITY = (0, 1000)

# создаем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Физическая песочница")

# создаем физический движок
space = pymunk.Space()
space.gravity = GRAVITY

# создаем пустой массив, который будет представлять песок
sand = []

# определяем функцию, которая будет обновлять экран
def update_screen():
    screen.fill(BACKGROUND_COLOR)
    for grain in sand:
        x, y = grain.body.position
        pygame.draw.circle(screen, SAND_COLOR, (int(x), int(y)), SAND_GRAIN_SIZE)
    pygame.display.update()

# создаем функцию, которая будет создавать новую зерно песка
def create_grain(x, y):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, SAND_GRAIN_SIZE))
    body.position = x, y
    shape = pymunk.Circle(body, SAND_GRAIN_SIZE)
    shape.density = SAND_DENSITY
    shape.friction = SAND_FRICTION
    space.add(body, shape)
    return shape

# запускаем игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grain = create_grain(x, y)
            sand.append(grain)

    # обновляем физический движок
    space.step(1/60)

    # обновляем экран
    update_screen()
