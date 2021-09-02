from pygame import draw, Color


class DoublePoint:
    color = Color(100, 100, 100)

    def __init__(self, first, last):
        self.first, self.last = first, last

    def paint(self, surface):
        draw.line(surface, DoublePoint.color, self.first.pos(), self.last.pos())
