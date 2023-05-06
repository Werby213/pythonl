import pygame
import sys
import random
import tkinter as tk
import time
from pygame.locals import QUIT
import multiprocessing as mp

score_count = 0
score_wave = 0
hp = 100
hit_count = 0
wave_elapsed = 0

# class settings():
#    def __init__(self):
#        self.control_type = "mouse"
#    def get_control_type(self):
#        return self.control_type

class Wave:
    def __init__(self):
        self.wave = 1
        self.base_asteroid_spawn_chance = 7
        self.asteroid_spawn_chance = self.base_asteroid_spawn_chance
        self.wave_time = 60

    def update_wave(self):
        self.asteroid_spawn_chance = max(1, self.base_asteroid_spawn_chance - self.wave)
        self.wave += 0
        self.wave_time -= 1

    def get_spawn_chance(self):
        return self.asteroid_spawn_chance

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


class Space_Dust_Sprites():
    def __init__(self):
        # Загрузка изображения, содержащего спрайты
        sprite_sheet = pygame.image.load('space_dust.png')
        # Размеры каждого спрайта
        sprite_width = sprite_sheet.get_width() // 8
        sprite_height = sprite_sheet.get_height() // 8

        # Создание списка поверхностей для каждого спрайта
        self.sprites = [
            sprite_sheet.subsurface(pygame.Rect(x * sprite_width, y * sprite_height, sprite_width, sprite_height))
            for y in range(8) for x in range(8)]
        print("space dust sprites generated")

    def get_space_dust_sprites_list(self):
        return self.sprites


class Space_dust(pygame.sprite.DirtySprite):
    space_dust_count = 0
    asteroid_sprites = Space_Dust_Sprites().get_space_dust_sprites_list()

    def __init__(self, center):
        super().__init__()
        self.dirty = 8
        self.space_dust_count +=1
        self.image_temp = random.choice(self.asteroid_sprites)
        self.rect = self.image_temp.get_rect()
        self.radius = int(self.rect.width * .75 / 2)
        size = random.randrange(5, 50)
        self.image = pygame.transform.scale(self.image_temp, (size, size))
        self.image_original = self.image.copy()
        self.rect.center = center
        self.rect.x += 50
        self.rect.y += 50
        self.speedx = random.randrange(-20, 20)
        self.speedy = random.randrange(-25, 6)
        self.rot_speed = random.randrange(-6, 6)
        self.last_update = pygame.time.get_ticks()
        self.rot = 0

    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.top > resolution[1] or self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > resolution[0]:

            self.kill()
            Space_dust.space_dust_count -= 1

    def get_space_dust_count(self):
        return self.space_dust_count

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

class Explosion(pygame.sprite.Sprite):
    IMAGES = []

    @classmethod
    def load_small_exlosions_sprites(cls):
        for i in range(1, 12):
            img = pygame.image.load(f"explosion_big/explosion_big{i}-removebg-preview.png")
            img = pygame.transform.scale(img, (250, 250))
            cls.IMAGES.append(img)

    def __init__(self, center):
        super().__init__()
        self.image = self.IMAGES[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.image = pygame.transform.scale(self.image, (random.randrange(10,50), random.randrange(10,50)))
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index == len(self.IMAGES):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.IMAGES[self.frame_index]
                self.rect = self.image.get_rect()
                self.rect.center = center
                self.rect.x = self.rect.x + -(e.get_info()["speed_x"])
                self.rect.y = self.rect.y + -(e.get_info()["speed_y"]) + 15



class Asteroid(pygame.sprite.DirtySprite):
    enemies_count = 0
    asteroid_sprites = AsteroidSprites().get_asteroid_sprites_list()
    MIN_DAMAGE = 10
    MAX_DAMAGE = 25

    @classmethod
    def get_enemies_count(cls):
        return cls.enemies_count

    def __init__(self):
        super().__init__()
        self.dirty = 4
        self.image_temp = random.choice(self.asteroid_sprites).copy()
        self.rect = self.image_temp.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.size = random.randrange(100, 200)
        self.image = pygame.transform.scale(self.image_temp, (self.size, self.size))
        self.image_original = self.image.copy()
        self.rect.x = random.randrange(-100, 1000)
        self.rect.y = -100
        self.speed_x = random.randrange(-3, 3)
        self.speed_y = random.randrange(1, 10)
        self.rot_speed = random.randrange(-3, 3)
        self.last_update = pygame.time.get_ticks()
        self.rot = 0
        self.damage = random.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)

    def update(self):
        self.rotate()
        self.rect.move_ip(self.speed_x, self.speed_y)
        if self.rect.top > resolution[1] or self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > resolution[0]:
            self.kill()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pygame.transform.rotate(self.image_original, self.rot)
            self.rect = self.image.get_rect(center=self.rect.center)

    def get_info(self):
        return {
            "damage": self.damage,
            "pos": self.rect.center,
            "speed_x": self.speed_x,
            "speed_y": self.speed_y,
            "size": self.size
        }



class Bullet(pygame.sprite.Sprite):
    bullet_loss = 0
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('plasma_bullet.png')
        self.rect = self.image.get_rect(center=pos)
        self.rect.x += 25
        self.rect.y -= 30
        self.spread = random.randrange(-5,5)


    def update(self):
        self.rect.move_ip(self.spread, -60)
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
    def __init__(self, use_mouse_control=False):
        pygame.sprite.Sprite.__init__(self)
        self.debug_mode = False
        self.images = [pygame.image.load(f'player/p{i}.png') for i in range(1, 5)]
        self.images = [pygame.transform.rotate(image, 90) for image in self.images]
        self.images = [pygame.transform.scale(image, (200, 200)) for image in self.images]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (resolution[0] / 2, resolution[1])
        self.speed = pygame.math.Vector2(0, 0)
        self.last_mouse_pos = pygame.mouse.get_pos()
        self.use_mouse_control = use_mouse_control

    def update(self):
        if hp > 85:
            self.image_index = 0
        elif hp > 50:
            self.image_index = 1
        elif hp > 25:
            self.image_index = 2
        else:
            self.image_index = 3
        self.image = self.images[self.image_index]
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

        # self.last_mouse_pos = pygame.mouse.get_pos()

    def shoot(self):
        Bullet.shoot()

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

p_bullet_sound = pygame.mixer.Sound('sound/bullet.ogg')
p_bullet_sound.set_volume(0.2)
explosion_small = pygame.mixer.Sound('sound/explosion2.ogg')
explosion_small.set_volume(0.2)
explosion_big = pygame.mixer.Sound('sound/explosion3.ogg')
explosion_big.set_volume(0.1)

all_sprites = pygame.sprite.Group()
space_dust = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
asteroid = Asteroid()
shop = UI_shop()
stats = Stats()
wave = Wave()
all_sprites.add(player)

Space_Dust_Sprites()
Explosion.load_small_exlosions_sprites()

background = pygame.image.load('background_2.jpg')
background = pygame.transform.scale(background, (resolution[0], 1280))
background = pygame.transform.rotate(background, 90)
x = 0
bg_height = background.get_rect().height


while running:
    clock.tick(FPS)
    space_dust.update()
    now = pygame.time.get_ticks()
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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            p_bullet_sound.play()
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
            Asteroid.enemies_count += 1

    hit = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
    if hit:
        hp = hp - e.damage
        explosion_small.play()
        score_count += 1
    bullet_hit = pygame.sprite.groupcollide(bullets, enemies, True, True, pygame.sprite.collide_circle)
    if bullet_hit:
        #space_dust.draw(DISPLAYSURF)
        explosion_small.play()
        score_count += 1
        score_wave += 1
        hit_count += 1
        Asteroid.enemies_count -= len(bullet_hit)

        if score_wave >= 10:
            wave.update_wave()
            score_wave = 0
        for asteroid in bullet_hit.values():
            for a in asteroid:
                explosion = Explosion(a.rect.center)
                all_sprites.add(explosion)
                for i in range(1, random.randrange(32,64)):
                    Space_dust.space_dust_count +=1
                    sd = Space_dust(a.rect.center)
                    all_sprites.add(sd)
                    space_dust.add(sd)


    if hp <= 0:
        print("Game Over")
        running = False

    f1 = pygame.font.Font("font.ttf", 35)
    f2 = pygame.font.Font(None, 25)
    text1 = f1.render(
        'Score: ' + str(score_count) + '       HP: ' + str(hp) + '       Wave: ' + str(
            wave.get_wave_number()) + '       Wave end: ', True,
        (180, 180, 180))
    text2 = f1.render('Misses: ' +
                      str(Bullet.get_bullet_loss()) +
                      '       Accuracy: ' + str(Bullet.get_accuracy()) + '%', True, (180, 0, 0))
    debug = f2.render('spawn chance: ' + str(wave.get_spawn_chance()) +
                      '     Enemies: ' + str(Asteroid.enemies_count) +
                      '     P_speed: ' + str(stats.get_player_speed()) +
                      '     P_bullet_s: ' + str(stats.get_player_bullet_speed()) +
                      '     P_reload_s: ' + str(stats.get_player_reload_speed()) +
                      '     Wave_time: ' + str(wave.wave_time) +
                      '     FPS: ' + (str(round(clock.get_fps()))) +
                      '     score_wave: ' + (str(score_wave)) +
                      '     space_dust: ' + str(Space_dust.space_dust_count),
                      True, (180, 0, 0))
    all_sprites.update()
    # pygame.display.update()

    all_sprites.draw(DISPLAYSURF)


    start_color = (0, 0, 0)
    end_color = (100, 0, 0)

    rect_width = resolution[0]
    rect_height = 100
    rect_x = 0
    rect_y = 0

    for i in range(rect_width):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * float(i) / rect_width)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * float(i) / rect_width)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * float(i) / rect_width)
        color = (r, g, b)


        pygame.draw.rect(DISPLAYSURF, color, (rect_x + i, rect_y, 1, rect_height))
        pygame.draw.rect(DISPLAYSURF, color, (rect_x - i, 100, resolution[0], 5))
    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 0, resolution[0], 100))
    DISPLAYSURF.blit(text1, (10, 10))
    DISPLAYSURF.blit(text2, (10, 50))

    if player.debug_mode:
        for sprite in all_sprites:
            pygame.draw.rect(DISPLAYSURF, (0, 255, 0), sprite.rect, 1)
        DISPLAYSURF.blit(debug, (10, 150))

    pygame.display.flip()