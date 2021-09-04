from pygame import init, display, time, event, QUIT, Color, Surface, mouse, quit
from time import perf_counter
from Point import Point, PointBlock
from random import randint, choice
import pygame


def loop(surface, clock, background_color=Color(255, 255, 255)):
    points = []
    font = get_font(background_color)

    while len(event.get(QUIT)) == 0:
        clock.tick(100)
        begin = perf_counter()
        surface.fill(background_color, surface.get_rect())
        for point in points:
            point.update(surface, points)
        end = perf_counter()
        print_debug_info(surface, font, points, begin, end)
        display.flip()
        mouse_handle(
            on_left_click=lambda x, y: points.append(Point(x, y)),
            on_right_click=points.clear
        )


def print_debug_info(surface, font, points, begin, end):
    elapsed = int(round((end - begin) * 1000, 0))
    info = {
        'Objects': str(len(points)),
        'Frozen': f'{percent_frozen(points)} %',
        'Elapsed': f'{elapsed} ms.'
    }
    surface.blit(debug(info, font), (0, 0))


def debug(info: dict, font: dict):
    y = 0
    size = 500, len(info) * (font['size'] + 5)
    surface = Surface(size)
    surface.fill(font['background_color'])
    for key in info.keys():
        line = f'{key}: {info[key]}'
        surface.blit(font['value'].render(line, True, font['color']), (15, y))
        y += font['size']

    return surface


def mouse_handle(on_left_click, on_right_click):
    buttons = mouse.get_pressed(3)
    if buttons[0]:
        shift = 5
        x, y = mouse.get_pos()
        shift_x, shift_y = randint(-shift, shift), randint(-shift, shift)
        on_left_click(x + shift_x, y + shift_y)
    elif buttons[2]:
        on_right_click()


def configure_display(size=(500, 500)):
    surface = display.set_mode(size)
    display.set_caption('')
    icon = Surface([50, 50])
    icon.fill(Color(255, 255, 255))
    display.set_icon(icon)
    return surface


def percent_frozen(points: list):
    if len(points) > 0:
        count_frozen = len(list(filter(lambda point: point.frozen, points)))
        return round(count_frozen / len(points) * 100, 2)

    return 0.00


def get_font(background_color, size=20):
    return {
        'value': pygame.font.SysFont('Segoe UI', size),
        'color': Color(0, 0, 0),
        'background_color': background_color,
        'size': size
    }


def main():
    init()
    loop(configure_display(), time.Clock())
    quit()


if __name__ == '__main__':
    main()
