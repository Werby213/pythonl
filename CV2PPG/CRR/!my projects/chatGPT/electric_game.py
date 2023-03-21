import pygame

# Константы для отображения
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Словарь с элементами
elements = {
    'lamp': {
        'inputs': 2,
        'voltage': 220,
        'current': 0.5,
    },
    'switch': {
        'inputs': 1,
        'threshold': 10,
    },
    'voltmeter': {
        'inputs': 1,
    },
    'wattmeter': {
        'inputs': 1,
    },
}

# Источник тока
power_source = {
    'voltage': 220,
    'inputs': 2,
}

# Индекс для добавления элементов
element_index = 1

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # Добавление элемента по клавише 1
                element = elements['lamp']
                print(f"Added element: lamp, voltage: {element['voltage']}V, current: {element['current']}A")
                element_index += 1
            elif event.key == pygame.K_2:
                # Добавление элемента по клавише 2
                element = elements['switch']
                print(f"Added element: switch, threshold: {element['threshold']}A")
                element_index += 1
    screen.fill(WHITE)
    pygame.display.update()
    clock.tick(60)

# Завершение pygame
pygame.quit()
