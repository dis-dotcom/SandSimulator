from Point import Point


class EventBus:
    @staticmethod
    def create_point(x: int, y: int):
        if 0 <= x < 500 and 0 <= y < 500:
            point = Point(x, y)
            point.MAP = Point.MAP
            Point.MAP.points().append(point)
            Point.MAP[x][y] = point
