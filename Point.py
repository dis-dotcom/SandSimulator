from pygame import draw, Color
from random import randint


class Point:
    color = Color(128, 128, 128)
    frozen_color = Color(128, 128, 255)

    def __init__(self, x, y, frozen=False):
        self.x, self.y = x, y
        self.frozen = frozen
        self.value = 0
        self.active = True

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __contains__(self, item):
        if isinstance(item, PointBlock):
            return self in item
        return self == item

    def paint(self, surface):
        color = Point.color if not self.frozen else Point.frozen_color
        draw.rect(surface, color, (self.x, self.y, 1, 1))

    def update(self, surface, points):
        if not self.frozen:
            if self.move_down(points) or self.move_to_side(points):
                self.try_deactivate()
            self.try_freeze()

        self.paint(surface)

    def move_to_side(self, points: list):
        left, right = Point(self.x - 1, self.y + 1), Point(self.x + 1, self.y + 1)
        can_left, can_right = True, True
        for point in points:
            if not can_left and not can_right:
                break
            if can_left and left == point:
                can_left = False
            if can_right and right == point:
                can_right = False

        target = None
        if can_left and can_right:
            target = left if randint(0, 1) == 0 else right
        elif can_left:
            target = left
        elif can_right:
            target = right

        if target is not None:
            self.x, self.y = target.x, target.y
            return True

        self.value += 1
        return False

    def move_down(self, points: list):
        target = Point(self.x, self.y + 1)
        for point in points:
            if target == point:
                return False

        self.y = target.y
        return True

    def try_freeze(self):
        if self.y == 499 or self.value >= 100:
            self.frozen = True

    def try_deactivate(self):
        if self.y >= 500:
            self.frozen = True
            self.active = False

    def merge(self, points: list):
        left = Point.left_side(self, points)
        if left and self.frozen and left.frozen:
            points.remove(left)
            points.remove(self)
            point = PointBlock(left.x, left.y, frozen=True)
            point.last = self
            points.append(point)

    @staticmethod
    def left_side(target, points):
        left = Point(target.x - 1, target.y)
        result = [point for point in points if left in point]
        if result is not None and len(result) > 0:
            return result[0]
        return None

    @staticmethod
    def right_side(target, points):
        right = Point(target.x + 1, target.y)
        result = [point for point in points if right in point]
        if result is not None and len(result) > 0:
            return result[0]
        return None


class PointBlock(Point):
    color = (0, 0, 0)

    def __init__(self, x, y, frozen=False):
        super().__init__(x, y, frozen)
        self.first = self
        self.last = None

    def __eq__(self, other):
        eq_first = self.first.x == other.x and self.first.y == other.y
        eq_last = False
        if self.last:
            eq_last = self.last.x == other.x and self.last.y == other.y
        return eq_first or eq_last

    def __contains__(self, item):
        return item == self.first or item == self.last

    def paint(self, surface):
        draw.rect(surface, PointBlock.color, (self.x, self.y, 2, 1))
