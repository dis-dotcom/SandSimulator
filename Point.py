from pygame import draw, Color
from random import randint


class Point:
    MAP = None
    color = Color(128, 128, 128)
    frozen_color = Color(128, 128, 255)

    def __init__(self, x, y, frozen=False):
        self.x, self.y = x, y
        self.frozen = frozen
        self.value = 0
        self.active = True

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y, self.active))

    def __contains__(self, item):
        if isinstance(item, PointBlock):
            return self in item
        return self == item

    def paint(self, surface):
        color = Point.color if not self.frozen else Point.frozen_color
        draw.rect(surface, color, (self.x, self.y, 1, 1))

    def update(self, surface):
        if not self.frozen:
            if self.move_down() or self.move_to_side():
                self.try_deactivate()
            self.try_freeze()

        self.paint(surface)

    def move_to_side(self):
        x, y, i, target, result = self.x, self.y, 0, None, False

        if 0 < x < 500 and 0 < y < 500:
            can_left_1 = Point.MAP[x - 1][y + 1] is None
            can_left_2 = Point.MAP[x - 2][y + 1] is None and randint(1, 2) == 2
            can_right_1 = Point.MAP[x + 1][y + 1] is None
            can_right_2 = Point.MAP[x + 2][y + 1] is None and randint(1, 2) == 2
            can_left = can_left_1 or can_left_2
            can_right = can_right_1 or can_right_2
            if can_left and can_right:
                target = i = -1 if randint(0, 1) == 0 else 1
            elif can_left:
                target = i = -2 if can_left_2 else -1
            elif can_right:
                target = i = 2 if can_right_2 else 1

        if target:
            Point.MAP[x + i][y + 1] = Point.MAP[x][y + 1]
            Point.MAP[x][y] = None
            self.x, self.y = x + i, y + 1
            result = True

        self.value += 1
        return result

    def move_down(self):
        x, y, i, result = self.x, self.y, randint(1, 2), False
        if Point.MAP.has_index(x, y + i):
            if Point.MAP[x][y + i] is None:
                Point.MAP[x][y + i] = Point.MAP[x][y]
                Point.MAP[x][y] = None
                self.y += i
                result = True

        return result

    def try_freeze(self):
        if self.y >= 499 or self.value >= 150:
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
