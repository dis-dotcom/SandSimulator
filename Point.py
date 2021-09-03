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
        target = self.can_move(points)
        if target:
            self.y = target.y

        if self.y >= 500:
            self.frozen = True

    def can_move(self, points):
        step, can_left, can_down, can_right = randint(1, 3), True, True, True
        left, right = Point(self.x - 1, self.y + 1), Point(self.x + 1, self.y + 1)
        down = self.get_down_point(step)

        for point in points:
            if can_down and down in point:
                can_down = False
            if can_left and left in point:
                can_left = False
            if can_right and right in point:
                can_right = False

        if can_down:
            return down
        elif can_left and can_right:
            return left if randint(0, 1) == 0 else right
        elif can_left:
            return left
        elif can_right:
            return right
        else:
            return None

    def get_down_point(self, step):
        return Point(self.x, self.y + step)
        if step == 1:
            return {
                1: Point(self.x, self.y + 1)
            }
        if step == 2:
            return {
                1: Point(self.x, self.y + 1),
                2: Point(self.x, self.y + 2)
            }
        if step == 3:
            return {
                1: Point(self.x, self.y + 1),
                2: Point(self.x, self.y + 2),
                3: Point(self.x, self.y + 3)
            }
