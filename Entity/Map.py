class Map:
    def __init__(self, points, size):
        self.__points__ = points
        self.__map__ = []
        self.__columns__ = 0
        self.__rows__ = 0
        self.set_size(size, size)

    def has_index(self, x, y):
        return y < self.__rows__ and x < self.__columns__

    def __contains__(self, item):
        return self.has_index(item.x, item.y) and self.__map__[item.x][item.y] is not None

    def __getitem__(self, item):
        return self.__map__[item]

    def points(self):
        return self.__points__

    def clear(self):
        self.__points__.clear()
        self.__map__.clear()

    def set_size(self, rows, columns):
        self.__rows__ = rows
        self.__columns__ = columns
        [self.__map__.append([None for _ in range(columns)]) for _ in range(rows)]

    def apply_for_point(self, x, y, condition, action):
        point = self.__map__[x][y]
        if condition(point):
            action()
