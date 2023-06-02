from pygame import *

P_WIDTH = 32
P_HEIGHT = 32
P_COLOR = "#b90b30"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((P_HEIGHT, P_HEIGHT))
        self.image = image.load("image/platform.png")
        self.rect = Rect(x, y, P_HEIGHT, P_HEIGHT)
