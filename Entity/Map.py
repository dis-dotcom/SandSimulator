class Map:
    def __init__(self):
        self.map = []

    def __getitem__(self, item):
        return self.map[item]

    def set_size(self, rows, columns):
        [self.map.append([None for _ in range(columns)]) for _ in range(rows)]

    def set_points(self, points):
        for point in points:
            x, y = point.x, point.y
            self[x][y] = point
