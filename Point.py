from pygame import draw, Color
from random import randint


class Point:
    color = Color(128, 128, 128)

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frozen = False

    def __contains__(self, item):
        if isinstance(item, Point):
            return (item.x, item.y) == (self.x, self.y)

    def update(self, surface, points):
        if not self.frozen:
            self.down(points)

        self.paint(surface)

    def paint(self, surface):
        draw.line(surface, Point.color, (self.x, self.y), (self.x, self.y))

    def down(self, points):
        left, down, right = self.get_targets()
        can_down, can_left, can_right = True, True, True

        for point in points:
            if can_down and down in point: can_down = False
            if can_left and left in point: can_left = False
            if can_right and right in point: can_right = False

        target = Point.get_target(can_down, can_left, can_right, down, left, right)

        if target:
            if target.y >= 499:
                self.frozen = True

            self.x, self.y = target.x, target.y

    def get_targets(self):
        step = randint(1, 3)
        return Point(self.x - 1, self.y), Point(self.x, self.y + step), Point(self.x + 1, self.y)

    @staticmethod
    def get_target(can_down, can_left, can_right, down, left, right):
        if can_down: return down
        if can_left and can_right: return left if randint(0, 1) == 0 else right
        if can_left: return left
        if can_right: return right
        return None
