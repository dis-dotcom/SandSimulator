class Map:
    def __init__(self, points, size):
        self.__points__ = points
        self.__map__ = []
        self.set_size(size, size)

    def __contains__(self, item):
        x, y = item.x, item.y
        if self.__map__

    def __getitem__(self, item):
        return self.__map__[item]

    def points(self):
        return self.__points__

    def clear(self):
        self.__points__.clear()
        self.__map__.clear()

    def set_size(self, rows, columns):
        [self.__map__.append([None for _ in range(columns)]) for _ in range(rows)]

    def apply_for_point(self, x, y, condition, action):
        point = self.__map__[x][y]
        if condition(point):
            action()
