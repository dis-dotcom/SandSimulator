from pygame import draw, Color


class DoublePoint:
    color = Color(100, 100, 100)

    def __init__(self, first, last):
        self.first, self.last = first, last
        self.frozen = False

    def paint(self, surface):
        draw.line(surface, DoublePoint.color, self.first.pos(), self.last.pos())

    @staticmethod
    def merge_points(first, last):
        if first.frozen and last.frozen:
            abs_x, abs_y = abs(first.x - last.x), abs(first.y - last.y)
            on_y = first.x == last.x and abs_y == 1
            on_x = first.y == last.y and abs_x == 1
            if on_x or on_y:
                return DoublePoint(first, last)
