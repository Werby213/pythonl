from pygame import *

WIDTH = 800
HEIGHT = 640

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    @staticmethod
    def camera_conf(camera, target_rect):
        left, top, _, _ = target_rect
        _, _, width, height = camera
        left, top = -left + WIDTH / 2, -top + HEIGHT / 2
        left = min(0, left)
        left = max(-(camera.width - WIDTH), left)

        top = min(0, top)
        top = max(-(camera.height - HEIGHT), top)

        return Rect(left, top, width, height)
