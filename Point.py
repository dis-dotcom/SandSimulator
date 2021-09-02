from pygame import draw
from random import randint


class Point:
    color = [128, 128, 128]

    def __init__(self, pos):
        self.x, self.y = pos
        self.frozen = False
        self.counter = 0

    def pos(self):
        return self.x, self.y

    def paint(self, surface):
        draw.line(surface, Point.color, self.pos(), self.pos())

    def update(self, surface, points):
        if self.frozen:
            self.paint(surface)
        else:
            self.down(points)
            self.paint(surface)

    def down(self, points):
        down_step = + randint(1, 3)
        target_down = self.x, self.y + down_step
        target_left = self.x - 1, self.y + 1
        target_right = self.x + 1, self.y + 1

        can_down, can_left, can_right = True, True, True

        for point in points:
            if can_down and (point.x, point.y) == target_down:
                can_down = False
            if can_left and (point.x, point.y) == target_left:
                can_left = False
            if can_right and (point.x, point.y) == target_right:
                can_right = False

        target = Point.get_target(can_down, can_left, can_right, target_down, target_left, target_right)

        if target:
            self.counter = 0
            if target[1] >= 499:
                self.x, self.y = target
                self.frozen = True
            else:
                self.x, self.y = target
        else:
            self.counter += 1
            if self.counter == 1000:
                self.frozen = True

    @staticmethod
    def get_target(can_down, can_left, can_right, target_down, target_left, target_right):
        if can_down:
            return target_down
        if can_left and can_right:
            return target_left if randint(0, 1) == 0 else target_right
        if can_left:
            return target_left
        if can_right:
            return target_right
        return None
