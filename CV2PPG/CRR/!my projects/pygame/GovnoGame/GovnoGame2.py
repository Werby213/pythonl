import pygame
import sys
import time
from pygame.locals import QUIT

b_x = 50
b_y = 50
x = b_x
y = b_y
done = False
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((b_x, b_y))
        self.image.fill(COLOR["Yellow"])
        self.rect = self.image.get_rect()
        self.rect.center = (resolution[0] / 3, resolution[1] / 5)
        self.rect.x = pos[0] - 5
        self.rect.y = pos[1] - 90

    def update(self, b_x, b_y):
        self.rect.y -= 40
        if self.rect.top < 0:
            self.image = pygame.transform.scale(self.image, (b_x, b_y))
            self.kill()
    def getpos(self):
        self.getpos = self.rect.x, self.rect.y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        # self.image.fill(COLOR["Yellow"])
        self.image = pygame.image.load('player.png')
        # self.image = pygame.transform.scale(self.image, (resolution[0] / 2, resolution[1] / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (resolution[0] / 3, resolution[1] / 5)
        self.speed = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 1)

    def update(self):
        self.speed += self.acceleration
        self.rect.move_ip(self.speed)
        if self.acceleration == 0:
            self.image = pygame.image.load('player_fall.png')

        # проверка на выход за пределы экрана
        if self.rect.bottom > resolution[1]:
            self.rect.bottom = resolution[1]
            self.speed.y = 0
        if self.rect.right > resolution[0]:
            self.speed.x = 0
        if self.rect.left <= 0:
            self.speed.x = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.speed.x = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.speed.x = 0

    def shoot(self):
        Bullet.shoot(self)

    def pjump(self):
        if self.rect.bottom > resolution[1] or self.rect.bottom == resolution[1]:
            self.speed.y = -25
            self.image = pygame.image.load('player_jump.png')

    def pleft(self):
        if self.rect.bottom == resolution[1]:
            self.speed.x = -10
            self.image = pygame.image.load('player_left.png')

    def pright(self):
        if self.rect.bottom == resolution[1]:
            self.speed.x = 10
            self.image = pygame.image.load('player_right.png')

    def nothing(self):
        self.image = pygame.image.load('player.png')


pygame.init()
pygame.mixer.init()

resolution = (1280, 720)
FPS = 60
COLOR = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Gray": (128, 128, 128),
    "Maroon": (128, 0, 0),
    "Olive": (128, 128, 0),
    "Lime": (0, 128, 0),
    "Teal": (0, 128, 128),
    "Purple": (128, 0, 128),
    "Navy": (0, 0, 128),
    "Pink": (255, 192, 203),
    "Brown": (165, 42, 42),
    "Orange": (255, 165, 0),
}

DISPLAYSURF = pygame.display.set_mode((resolution))
pygame.display.set_caption("GovnoGame")
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            all_sprites.add(Bullet(player.rect.center))
            pos = player.rect.x, player.rect.y
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.pjump()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            player.pright()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            player.pleft()
        if event.type == pygame.KEYUP:
            player.nothing()
        if Bullet.getpos == resolution[0]:
            for i in range(50):
                x +=1
                y +=1
                Bullet.update(b_x=x)
                Bullet.update(b_y=y)
                done = True

    all_sprites.update()
    pygame.display.update()
    DISPLAYSURF.fill(COLOR["Teal"])
    all_sprites.draw(DISPLAYSURF)
    pygame.display.flip()