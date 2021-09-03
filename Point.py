from pygame import draw, Color
from random import randint


class Point:
    color = Color(128, 128, 128)

    def __init__(self, x, y, frozen=False):
        self.x, self.y = x, y
        self.frozen = frozen
        self.value = 0

    def __contains__(self, item):
        return (item.x, item.y) == (self.x, self.y)

    def paint(self, surface):
        draw.rect(surface, Point.color, (self.x, self.y, 1, 1))

    def update(self, surface, points):
        if not self.frozen:
            if not self.move_down(points):
                self.move_to_side(points)

        self.paint(surface)

    def move_to_side(self, points: list):
        left, right = Point(self.x - 1, self.y + 1), Point(self.x + 1, self.y + 1)
        can_left = len([point for point in points if left in point]) == 0
        can_right = len([point for point in points if right in point]) == 0
        if can_left and can_right:
            self.x = left.x if randint(0, 1) == 0 else right.x
        elif can_left:
            self.x = left.x
        elif can_right:
            self.x = right.x

    def move_down(self, points: list):
        target = Point(self.x, self.y + 1)
        if len([point for point in points if target in point]) == 0:
            self.y = target.y

            if self.y >= 499:
                self.frozen = True

            return True
        else:
            self.value += 1
            if self.value == 250:
                self.frozen = True
            return False
