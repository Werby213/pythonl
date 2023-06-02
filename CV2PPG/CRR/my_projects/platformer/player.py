from pygame import *
import pyganim

speed = 3
WIDTH = 22
HEIGHT = 32
player_COLOR = "#000000"
COLOR = "#000000"
player_JUMP_POWER = 8
GRAVITY = 0.35
ANIMATION_DELAY = 1

ANIMATION_RIGHT = [('image/player/r2.png'),
                  ('image/player/r3.png'),
                  ('image/player/r4.png'),
                  ('image/player/r5.png')]

ANIMATION_LEFT = [('image/player/l1.png'),
                  ('image/player/l2.png'),
                  ('image/player/l3.png'),
                  ('image/player/l4.png'),
                  ('image/player/l5.png')]

ANIMATION_JUMP_LEFT = [('image/player/jl.png', 1)]
ANIMATION_JUMP_RIGHT = [('image/player/jr.png', 1)]
ANIMATION_JUMP = [('image/player/j.png', 1)]
ANIMATION_STAY = [('image/player/0.png', 1)]
ANIMATION_FALL = [('image/player/d.png', 1)]

class Player(sprite.Sprite):
  def __init__(self, x, y):
    sprite.Sprite.__init__(self)
    self.xvel = 0
    self.yvel = 0
    self.onGround = False
    self.start_x = x
    self.start_y = y
    self.image = Surface((WIDTH, HEIGHT))
    self.image.fill(COLOR)
    self.rect = Rect(x, y, WIDTH, HEIGHT)
    self.image.set_colorkey(Color(player_COLOR))

    boltAnim = []
    for anim in ANIMATION_RIGHT:
      boltAnim.append((anim, ANIMATION_DELAY))
    self.boltAnimRight = pyganim.PygAnimation(boltAnim)
    self.boltAnimRight.play()

    boltAnim = []
    for anim in ANIMATION_LEFT:
      boltAnim.append((anim, ANIMATION_DELAY))
    self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
    self.boltAnimLeft.play()

    self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
    self.boltAnimStay.play()
    self.boltAnimStay.blit(self.image, (0, 0))

    self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
    self.boltAnimJumpLeft.play()

    self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
    self.boltAnimJumpRight.play()

    self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
    self.boltAnimJump.play()

    self.boltAnimFall = pyganim.PygAnimation(ANIMATION_FALL)
    self.boltAnimFall.play()
  def update(self, left, right, up, platform):
    if up:
      self.image.fill(player_COLOR)
      self.boltAnimJump.blit(self.image, (0, 0))
      if self.onGround:
        self.yvel -= player_JUMP_POWER
    if not self.onGround:
      self.image.fill(player_COLOR)
      if self.yvel < 15:
        self.yvel += GRAVITY
        self.boltAnimJump.blit(self.image, (0, 0))
    if left:
      self.image.fill(player_COLOR)
      if up:
        self.boltAnimJumpLeft.blit(self.image, (0,0))
      else:
        self.boltAnimLeft.blit(self.image, (0, 0))
      self.xvel = -speed
    if right:
      self.image.fill(player_COLOR)
      if up:
        self.boltAnimJumpRight.blit(self.image, (0,0))
      else:
        self.boltAnimRight.blit(self.image, (0, 0))
      self.xvel = speed
    if not(right or left):
      self.xvel = 0
      if not up:
        self.image.fill(player_COLOR)
        self.boltAnimStay.blit(self.image, (0, 0))
    self.rect.x +=self.xvel
    self.collide(self.xvel, 0, platform)
    self.onGround = False
    self.rect.y += self.yvel
    self.collide(0, self.yvel, platform)

    if self.yvel > 1 and not self.onGround:
      self.image.fill(player_COLOR)
      self.boltAnimFall.blit(self.image, (0, 0))

  def draw(self, DISPLAYSURF):
    DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))

  def collide(self, xvel, yvel, platform):
    def detect_collision(block):
      if sprite.collide_rect(self, block):
        if xvel > 0:
          self.rect.right = block.rect.left
        if xvel < 0:
          self.rect.left = block.rect.right
        if yvel > 0:
          self.rect.bottom = block.rect.top
          self.onGround = True
          self.yvel = 0
        if yvel < 0:
          self.rect.top = block.rect.bottom
          self.yvel = 0
    any(detect_collision(block) for block in platform)
