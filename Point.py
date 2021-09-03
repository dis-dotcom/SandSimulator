from pygame import draw, Color
from random import randint


class Point:
    color = Color(128, 128, 128)

    def __init__(self, x, y, frozen=False):
        self.x, self.y = x, y
        self.frozen = frozen

    def __contains__(self, item):
        if isinstance(item, Point):
            return (item.x, item.y) == (self.x, self.y)

    def paint(self, surface):
        draw.line(surface, Point.color, (self.x, self.y), (self.x, self.y))

    def update(self, surface, points):
        if not self.frozen:
            self.down(points)

        self.paint(surface)

    def down(self, points: list):
        left, down, right = self.get_targets()
        can_down = Point.can_move(down, points)
        can_left = Point.can_move(left, points)
        can_right = Point.can_move(right, points)

        if can_down and down.y <= 499:
            self.y = down.y
            return
        if can_left and left.y <= 499:
            self.y = left.y
            return
        if can_right and right.y <= 499:
            self.y = right.y
            return

        if not can_down and not can_left and not can_right:
            self.frozen = True

    @staticmethod
    def is_busy(target, points):
        for point in points:
            if (point.x, point.y) == (target.x, target.y):
                return True, point
        return False, None

    @staticmethod
    def can_move(target, points):
        busy, point = Point.is_busy(target, points)
        return not busy

    def get_targets(self):
        return Point(self.x - 1, self.y + 1), Point(self.x, self.y + randint(1, 3)), Point(self.x + 1, self.y + 1)
