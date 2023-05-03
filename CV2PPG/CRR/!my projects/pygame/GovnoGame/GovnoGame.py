import pygame
import sys
import random
import tkinter as tk
import time
from pygame.locals import QUIT
from tqdm import tqdm
score_count = 0
hp = 100
hit_count = 0
wave_elapsed = 0



#class settings():
#    def __init__(self):
#        self.control_type = "mouse"
#    def get_control_type(self):
#        return self.control_type

class Wave:
    def __init__(self):
        self.wave = 1
        self.base_enemy_spawn_chance = 20
        self.enemy_spawn_chance = self.base_enemy_spawn_chance
        self.wave_time = 60

    def update_wave(self):
        self.enemy_spawn_chance = max(1, self.base_enemy_spawn_chance - self.wave)
        self.wave += 1

    def get_spawn_chance(self):
        return self.enemy_spawn_chance
    def get_wave_number(self):
        return self.wave
    def get_wave_time(self):
        return self.wave_time

class Stats():
    def __init__(self):
        self.player_speed = 10
        self.reload_speed = 3
        self.bullet_speed = 10
    def get_player_speed(self):
        return self.player_speed
    def get_player_reload_speed(self):
        return self.reload_speed
    def get_player_bullet_speed(self):
        return self.bullet_speed

class UI_shop(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500+100+100")
        self.title("Shop")

        self.stats = Stats()

        self.count1 = tk.Label(self, text=self.stats.player_speed)
        self.count1.place(x=10, y=10)

        button1 = tk.Button(self, text="Increase", command=self.increase_player_speed)
        button1.place(x=10, y=50)

        button2 = tk.Button(self, text="Decrease", command=self.decrease_player_speed)
        button2.place(x=100, y=50)

    def increase_player_speed(self):
        self.stats.player_speed += 1
        self.count1.config(text=self.stats.player_speed)

    def decrease_player_speed(self):
        self.stats.player_speed -= 1
        self.count1.config(text=self.stats.player_speed)

    def run(self):
        self.mainloop()
    def stop(self):
        self.quit()

class Space_Dust(pygame.sprite.Sprite):
    enteties_on_screen = 0
    damage = 0
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
            enemy.enteties_on_screen -= 1

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
    def get_enteties_on_screen(self):
        return self.enteties_on_screen
    def get_damage(self):
        return self.damage

class AsteroidSprites():
    def __init__(self):
        # Загрузка изображения, содержащего спрайты
        sprite_sheet = pygame.image.load('asteroids.png')
        # Размеры каждого спрайта
        sprite_width = sprite_sheet.get_width() // 8
        sprite_height = sprite_sheet.get_height() // 8

        # Создание списка поверхностей для каждого спрайта
        self.sprites = [
            sprite_sheet.subsurface(pygame.Rect(x * sprite_width, y * sprite_height, sprite_width, sprite_height))
            for y in range(8) for x in range(8)]
        print("asteroid sprites generated")

    def get_asteroid_sprites_list(self):
        return self.sprites


class Asteroid(pygame.sprite.Sprite):
    enemies_on_screen = 0
    asteroid_sprites = AsteroidSprites().get_asteroid_sprites_list()

    @classmethod
    def get_enemies_on_screen(cls):
        return cls.enemies_on_screen

    def __init__(self):
        super().__init__()

        # Инициализация остальных атрибутов класса
        self.image_temp = random.choice(self.asteroid_sprites).copy()
        self.rect = self.image_temp.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        size = random.randint(self.rect.width - 10, self.rect.height + 100)
        self.image = pygame.transform.scale(self.image_temp, (size, size))
        self.image_original = self.image.copy()
        self.rect.x = random.randint(-100, 1000)
        self.rect.y = -100
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 10)
        self.rot_speed = random.randint(-3, 3)
        self.last_update = pygame.time.get_ticks()
        self.rot = 0
        self.damage = random.randrange(10, 25)

    def update(self):
        self.rotate()
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.left > resolution[0] or self.rect.left > resolution[1] or self.rect.right < 0:
            self.kill()
            Asteroid.enemies_on_screen -= 1

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pygame.transform.rotate(self.image_original, self.rot)
            self.rect = self.image.get_rect(center=self.rect.center)

    def get_damage(self):
        return self.damage


class Bullet(pygame.sprite.Sprite):
    bullet_loss = 0

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.move_ip(0, -40)
        if self.rect.top < 0:
            self.kill()
            Bullet.bullet_loss += 1

    @classmethod
    def get_bullet_loss(cls):
        return cls.bullet_loss

    @classmethod
    def get_accuracy(cls):
        try:
            if hit_count == 0:
                return 0
            acc = 100 - (cls.bullet_loss / hit_count * 100)
            return round(max(acc, 0))
        except ZeroDivisionError:
            return 0




class Player(pygame.sprite.Sprite):
    def __init__(self, use_mouse_control=True):
        self.debug_mode = False
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        # self.image.fill(COLOR["Yellow"])
        self.image = pygame.image.load('player_gamma.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (resolution[0] / 2, resolution[1])
        self.speed = pygame.math.Vector2(0, 0)
        self.last_mouse_pos = pygame.mouse.get_pos()
        self.use_mouse_control = use_mouse_control

    def update(self):
        self.rect.move_ip(self.speed)
        self.move_speed = 10
        if self.use_mouse_control:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos != self.last_mouse_pos:
                move_vector = pygame.math.Vector2(mouse_pos[0] - self.rect.center[0],
                                                  mouse_pos[1] - self.rect.center[1])
                if move_vector.length() != 0:
                    move_vector.normalize_ip()
                    self.speed = move_vector * self.move_speed
            else:
                self.speed = pygame.math.Vector2(0, 0)
                self.move_speed = 0
        else:
            keys = pygame.key.get_pressed()
            self.speed.x = 0
            self.speed.y = 0
            if keys[pygame.K_w]:
                self.speed.y = -10
            elif keys[pygame.K_s]:
                self.speed.y = 10
            if keys[pygame.K_a]:
                self.speed.x = -10
            elif keys[pygame.K_d]:
                self.speed.x = 10

        # проверка на выход за пределы экрана
        if self.rect.bottom > resolution[1]:
            self.rect.bottom = resolution[1]
            self.speed.y = -1
        if self.rect.right > resolution[0]:
            self.speed.x = -1
        if self.rect.left <= 0:
            self.speed.x = 1

        #self.last_mouse_pos = pygame.mouse.get_pos()

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
        score_count += 1

    def toggle_debug(self):
        self.debug_mode = not self.debug_mode





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
pygame.display.set_caption("AsterZoid v0.2 pre-pre-pre-pre-pre-pre-alpha")
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
enemy = Asteroid()
shop = UI_shop()
stats = Stats()
all_sprites.add(player)
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (resolution[0], 1280))
background = pygame.transform.rotate(background, 90)
x = 0
bg_height = background.get_rect().height
while running:
    wave = Wave()
    clock.tick(FPS)
    rel_y = x % bg_height
    DISPLAYSURF.blit(background, (0, rel_y - bg_height))
    x += 1
    if rel_y < resolution[1]:
        DISPLAYSURF.blit(background, (0, rel_y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            player.toggle_debug()

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            shop.stop()
        if random.randint(1, wave.get_spawn_chance()) == 1:
            e = Asteroid()
            all_sprites.add(e)
            enemies.add(e)
            enemy.enemies_on_screen +=1

    hit = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
    if hit:
        hp = hp - enemy.get_damage()
        score_count += 1

    bullet_hit = pygame.sprite.groupcollide(bullets, enemies, True, True, pygame.sprite.collide_circle)
    if bullet_hit:
        score_count +=1
        hit_count += 1
        enemy.enemies_on_screen -= 1
    if hp <= 0:
        print("Game Over")
        running = False

    f1 = pygame.font.Font("font.ttf", 35)
    f2 = pygame.font.Font(None, 30)
    text1 = f1.render(
        'Score: ' + str(score_count) + '       HP: ' + str(hp) + '       Wave: ' + str(wave.get_wave_number()) + '       Wave end: ' , 1,
        (180, 180, 180))
    text2 = f1.render('Misses: ' +
                      str(Bullet.get_bullet_loss()) +
                      '       Accuracy: ' + str(Bullet.get_accuracy())+'%', 1, (180, 0, 0))

    if player.debug_mode:
        debug = f2.render('spawn chance: ' + str(wave.get_spawn_chance()) +
                          '     Enemies: '+ str(enemy.get_enemies_on_screen()) +
                          '     P_speed: ' + str(stats.get_player_speed()) +
                          '     P_bullet_s: ' + str(stats.get_player_bullet_speed()) +
                          '     P_reload_s: ' + str(stats.get_player_reload_speed()),
                          1, (180, 0, 0))
        for sprite in all_sprites:
            pygame.draw.rect(DISPLAYSURF, (0, 255, 0), sprite.rect, 1)
        DISPLAYSURF.blit(debug, (10, 150))

    all_sprites.update()
    #pygame.display.update()
    all_sprites.draw(DISPLAYSURF)
    DISPLAYSURF.blit(text1, (10, 50))
    DISPLAYSURF.blit(text2, (10, 100))

    pygame.display.flip()