from pygame import draw, Color


class FrozenPoint:
    color = Color(128, 128, 255)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def paint(self, surface):
        draw.rect(surface, FrozenPoint.color, (self.x, self.y, 1, 1))
