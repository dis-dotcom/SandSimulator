from pygame import draw, Color


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
            self.move_down(points)

        self.paint(surface)

    def move_down(self, points: list):
        target = Point(self.x, self.y + 1)
        if len([point for point in points if target in point]) == 0:
            self.y = target.y

            if self.y >= 499:
                self.frozen = True
        else:
            self.value += 1
            if self.value == 250:
                self.frozen = True
