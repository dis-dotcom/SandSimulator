from pygame import init, display, time, event, QUIT, mouse, quit
from time import perf_counter
from Point import Point
from random import randint
from Entity.Map import Map
from vector import Vector
from GUI import GUI
from config import Config


def loop(clock):
    config = Config()
    gui = GUI(config)
    canvas = gui.configure()

    Point.MAP = Map([], 501)
    points = Point.MAP.points()

    vector_map = [[Vector(250, 250), Vector(500 - 5, 500 - 5)]]

    while len(event.get(QUIT)) == 0:
        clock.tick(100)
        begin = perf_counter()

        canvas.fill()
        for row in vector_map:
            for vector in row:
                canvas.paint(vector)

        for point in points:
            point.update(canvas.surface)
        gc(points)

        end = perf_counter()
        gui.info(points, begin, end)

        display.flip()
        mouse_handle(
            on_left_click=lambda x, y: create_point(x, y, points, Point.MAP),
            on_right_click=lambda: clear_points(points)
        )


def create_point(x, y, points, array):
    if 0 <= x < 500 and 0 <= y < 500:
        point = Point(x, y)
        point.MAP = array
        points.append(point)
        array[x][y] = point


def clear_points(points):
    if len(points) > 0:
        points[0].MAP.clear()
    points.clear()


def gc(points):
    if len(points) > 0:
        index = 0
        while index < len(points):
            if points[index].active and points[index].y <= 499:
                index += 1
                continue
            del points[index]


def mouse_handle(on_left_click, on_right_click):
    left, _, right = mouse.get_pressed()
    if left:
        shift = 5
        x, y = mouse.get_pos()
        shift_x, shift_y = randint(-shift, shift), randint(-shift, shift)
        on_left_click(x + shift_x, y + shift_y)
    elif right:
        on_right_click()


def main():
    init()
    loop(time.Clock())
    quit()


if __name__ == '__main__':
    main()
