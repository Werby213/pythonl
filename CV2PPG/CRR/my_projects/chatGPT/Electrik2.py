import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()


class Wire:
    def __init__(self, start_element, start_port, end_element, end_port):
        self.start_element = start_element
        self.start_port = start_port
        self.end_element = end_element
        self.end_port = end_port
        self.calculate_path()

    def calculate_path(self):
        start_pos = self.start_element.ports[self.start_port]
        end_pos = self.end_element.ports[self.end_port]
        self.path = [(start_pos[0], start_pos[1]), (end_pos[0], end_pos[1])]


class Element:
    def __init__(self, x, y, texture_on, texture_off):
        self.x = x
        self.y = y
        self.texture_on = texture_on
        self.texture_off = texture_off
        self.ports = {}




class Element:
    def __init__(self, image_on, image_off, pos, resistance):
        self.image_on = pygame.image.load("C:\placeholder.png")
        self.image_off = pygame.image.load("C:\placeholder.png")
        self.pos = pos
        self.resistance = resistance
        self.voltage = 0
        self.power = 0
        self.state = False
        self.ports = {}

    def add_port(self, name, x, y):
        self.ports[name] = (self.x + 10, self.y + 90)

    def update(self):
        self.voltage = self.power / self.resistance
        if self.voltage > 100:
            self.state = False
            self.power = 0
            self.voltage = 0

    def draw(self, screen):
        if self.state:
            screen.blit(self.image_on, self.pos)
        else:
            screen.blit(self.image_off, self.pos)

def spawn_element(key):
    if key == pygame.K_1:
        pos = [random.randint(0, 800), random.randint(0, 600)]
        resistance = random.uniform(0.1, 1)
        elements.append(Element("lamp_on.png", "lamp_off.png", pos, resistance))
    elif key == pygame.K_2:
        pos = [random.randint(0, 800), random.randint(0, 600)]
        resistance = random.uniform(1, 10)
        elements.append(Element("switch_on.png", "switch_off.png", pos, resistance))

elements = []
selected_element = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            spawn_element(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for element in elements:
                    x, y = element.pos
                    w, h = element.image_on.get_size()
                    if x < pos[0] < x + w and y < pos[1] < y + h:
                        selected_element = element
        if event.type == pygame.MOUSEBUTTONUP:
            selected_element = None

    screen.fill((255, 255, 255))

    if selected_element:
        x, y = pygame.mouse.get_pos()
        selected_element.pos = [x - selected_element.image_on.get_size()[0] / 2,
                                y - selected_element.image_on.get_size()[1] / 2]

    for element in elements:
        element.update()
        element.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
