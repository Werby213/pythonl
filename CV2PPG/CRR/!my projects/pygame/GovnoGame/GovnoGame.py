import pygame
import sys
import random
import tkinter as tk
import time
from pygame.locals import QUIT
score_count = 0
hp = 100

wave_elapsed = time.localtime()


meteors = ['meteor1.png', 'meteor2.png', 'meteor3.png', 'meteor4.png', 'meteor5.png']


class Wave:
    def __init__(self):
        self.wave = 1
        self.enemy_spawn_chance = 15

    def update_wave(self):
        self.enemy_spawn_chance -= 1
        self.wave += 1

    def get_spawn_chance(self):
        return self.enemy_spawn_chance
class UI_shop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500+100+100")
        self.title("Shop")
        self.count1 = tk.Label(self, textvariable="123123")
        self.count1.place(x=10, y=10)

    def run(self):
        self.mainloop()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Загрузка изображения, содержащего спрайты
        sprite_sheet = pygame.image.load('asteroids.png')

        # Размеры каждого спрайта
        sprite_width = sprite_sheet.get_width() // 8
        sprite_height = sprite_sheet.get_height() // 8

        # Создание списка поверхностей для каждого спрайта
        sprites = []
        for y in range(8):
            for x in range(8):
                sprite_rect = pygame.Rect(x * sprite_width, y * sprite_height, sprite_width, sprite_height)
                sprite = sprite_sheet.subsurface(sprite_rect)
                sprites.append(sprite)

        # Инициализация остальных атрибутов класса
        self.image_temp = sprites[random.randint(0, 63)]  # случайный спрайт из списка
        self.image = self.image_temp.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.image = pygame.transform.scale(self.image, (random.randint(self.rect.width - 10, self.rect.height + 100),
                                                         random.randint(self.rect.width - 10, self.rect.height + 100)))
        self.image = pygame.transform.rotate(self.image, (random.randint(0, 360)))
        self.rect.x = random.randint(-100, 1000)
        self.rect.y = -100
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 10)
        self.rot = 0
        self.rot_speed = random.randrange(-3, 3)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > resolution[0] or self.rect.left > resolution[1] or self.rect.right < 0:
            self.kill()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_temp, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = (resolution[0] / 3, resolution[1] / 5)
        self.rect.x = pos[0] - 5
        self.rect.y = pos[1] - 90

    def update(self):
        self.rect.y -= 40
        if self.rect.top < 0:
            self.kill()

    def getpos(self):
        self.getpos = self.rect.x, self.rect.y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        # self.image.fill(COLOR["Yellow"])
        self.image = pygame.image.load('player_gamma.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (resolution[0] / 2, resolution[1])
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)
        if self.speed == 0:
            self.image = pygame.image.load('player_fall.png')

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed.y = -10
        elif keys[pygame.K_s]:
            self.speed.y = 10
        else:
            self.speed.y = 0

        if keys[pygame.K_a]:
            self.speed.x = -10
        elif keys[pygame.K_d]:
            self.speed.x = 10
        else:
            self.speed.x = 0


        # проверка на выход за пределы экрана
        if self.rect.bottom > resolution[1]:
            self.rect.bottom = resolution[1]
            self.speed.y = -1
        if self.rect.right > resolution[0]:
            self.speed.x = -1
        if self.rect.left <= 0:
            self.speed.x = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.speed.x = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.speed.x = 0

    def shoot(self):
        Bullet.shoot(self)

    def pleft(self):
        if self.rect.bottom == resolution[1]:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.speed.x = -10
            else:
                self.speed.x = 0

    def pright(self):
        if self.rect.bottom == resolution[1]:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.speed.x = 10
            else:
                self.speed.x = 0

    def ptop(self):
        if self.rect.bottom == resolution[1]:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.speed.y = -10
            else:
                self.speed.y = 0

    def pdown(self):
        if self.rect.bottom == resolution[1]:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.speed.y = 10
            else:
                self.speed.y = 0

    def score(self):
        global score_count
        score_count = score_count + 1



pygame.init()
pygame.mixer.init()

resolution = (1280, 1280)
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
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
enemy = Enemy()
shop = UI_shop()
wave = Wave()
all_sprites.add(player)
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (resolution[0], 1280))
y=0
bg_width = background.get_rect().width
while running:
    clock.tick(FPS)
    rel_x = y % bg_width
    DISPLAYSURF.blit(background, (rel_x - bg_width, 0))
    y -= 1

    if rel_x < resolution[0]:
        DISPLAYSURF.blit(background, (rel_x , 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            b = Bullet(player.rect.center)
            all_sprites.add(b)
            bullets.add(b)
            pos = player.rect.x, player.rect.y
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            player.pright()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            player.pleft()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.ptop()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            player.pdown()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            shop.run()
        if random.randint(1, wave.get_spawn_chance()) == 1:
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)

    hit = pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_circle)
    if hit:
        hp = hp - 1

    bullet_hit = pygame.sprite.groupcollide(bullets, enemies, True, True, pygame.sprite.collide_circle)
    if bullet_hit:
        score_count +=1
    if hp == 0:
        print("Game Over")
        running = False

    f1 = pygame.font.Font(None, 50)
    text1 = f1.render('Счет: ' + str(score_count)+ '    HP: '+ str(hp) + '       Волна: '+ str(wave) + '  Конец волны:', 1, (180, 0, 0))
    all_sprites.update()
    #pygame.display.update()
    DISPLAYSURF.blit(text1, (10, 50))
    all_sprites.draw(DISPLAYSURF)
    pygame.display.flip()