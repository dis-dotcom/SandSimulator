from FrozenPoint import FrozenPoint


class Scene:
    def __init__(self, surface):
        self.surface = surface
        self.frozen_points = {}

    def add_frozen_point(self, point: FrozenPoint):
        dicts = self.frozen_points.get(point.x)

    def paint(self):
        for dicts in self.frozen_points:
            for point in dicts:
                point.paint(self.surface)
