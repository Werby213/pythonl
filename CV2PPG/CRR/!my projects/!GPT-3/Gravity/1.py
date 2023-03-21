import pygame
import random
import math

# константы окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# константы частиц
PARTICLE_COUNT = 50
PARTICLE_RADIUS = 10
PARTICLE_COLOR = (255, 255, 255)
PARTICLE_MASS_RANGE = (1, 5)
PARTICLE_SPEED_RANGE = (1, 3)

# константы гравитации
GRAVITATIONAL_CONSTANT = 1

# инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гравитация")

# функция для расчета притяжения между частицами
def calculate_gravity(particle, other_particles):
    force_x = 0
    force_y = 0

    for other_particle in other_particles:
        if particle == other_particle:
            continue

        distance = math.sqrt((particle.x - other_particle.x) ** 2 + (particle.y - other_particle.y) ** 2)
        force = GRAVITATIONAL_CONSTANT * particle.mass * other_particle.mass / distance ** 2

        angle = math.atan2(other_particle.y - particle.y, other_particle.x - particle.x)
        force_x += force * math.cos(angle)
        force_y += force * math.sin(angle)

    return force_x, force_y

# класс для представления частиц
class Particle:
    def __init__(