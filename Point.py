from pygame import draw, Color
from random import randint


class Point:
    color = Color(128, 128, 128)

    def __init__(self, x, y, frozen=False):
        self.x, self.y = x, y
        self.frozen = frozen

    def __contains__(self, item):
        return (item.x, item.y) == (self.x, self.y)

    def paint(self, surface):
        draw.line(surface, Point.color, (self.x, self.y), (self.x, self.y))

    def update(self, surface, points):
        if not self.frozen:
            self.move_down(points)

        self.paint(surface)

    def move_down(self, points: list):
        step = randint(1, 3)
        down_1 = Point(self.x, self.y + 1)
        can_down_1 = Point.can_move_to(down_1, points)
        down_2 = Point(self.x, self.y + 2)
        can_down_2 = Point.can_move_to(down_2, points)
        down_3 = Point(self.x, self.y + 3)
        can_down_3 = Point.can_move_to(down_3, points)
        target = None

        if step == 1 and can_down_1:
            target = down_1
        if step == 2 and can_down_1 and can_down_2:
            target = down_2
        if step == 3 and can_down_1 and can_down_2 and can_down_3:
            target = down_3

        if target:
            self.y = target.y

        if self.y >= 500:
            self.frozen = True

    @staticmethod
    def can_move_to(target, points):
        for point in points:
            if target in point:
                return False
        return True
