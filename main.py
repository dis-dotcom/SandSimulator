from pygame import init, display, time, event, QUIT, Color, Surface, mouse, quit
from time import perf_counter
from Point import Point
from random import randint
import pygame


def loop(surface, clock, background_color=Color(255, 255, 255)):
    points = []
    font = get_font(background_color)

    while len(event.get(QUIT)) == 0:
        clock.tick(100)
        begin_frame_time = perf_counter()
        surface.fill(background_color, surface.get_rect())
        [point.update(surface, points) for point in points]
        end_frame_time = perf_counter()
        print_debug_info(surface, font, points, begin_frame_time, end_frame_time)
        display.flip()
        mouse_handle(
            on_left_click=lambda pos: points.append(Point(pos)),
            on_right_click=points.clear
        )


def print_debug_info(surface, font, points, begin_frame_time, end_frame_time):
    info = {
        'Objects': str(len(points)),
        'Frozen': f'{percent_frozen(points)} %',
        'Elapsed': f'{elapsed(begin_frame_time, end_frame_time)} ms.'
    }
    surface.blit(debug(info, font), (0, 0))


def debug(info: dict, font: dict):
    y, shift = 0, 20
    size = 500, len(info) * (shift + 5)
    surface = Surface(size)
    surface.fill(font['background_color'])
    for key in info.keys():
        line = f'{key}: {info[key]}'
        surface.blit(font['value'].render(line, True, font['color']), (15, y))
        y += shift

    return surface


def mouse_handle(on_left_click, on_right_click):
    buttons = mouse.get_pressed(3)
    if buttons[0]:
        shift = 5
        x, y = mouse.get_pos()
        shift_x, shift_y = randint(-shift, shift), randint(-shift, shift)
        on_left_click((x + shift_x, y + shift_y))
    elif buttons[2]:
        on_right_click()


def configure_display(size=(500, 500)):
    surface = display.set_mode(size)
    display.set_caption('')
    icon = Surface([50, 50])
    icon.fill(Color(255, 255, 255))
    display.set_icon(icon)
    return surface


def elapsed(begin, end):
    return round((end - begin) * 1000, 3)


def percent_frozen(points: list):
    if len(points) > 0:
        count_frozen = len(list(filter(lambda point: point.frozen, points)))
        return round(count_frozen / len(points) * 100, 2)

    return 0.00


def get_font(background_color):
    return {
        'value': pygame.font.SysFont('Segoe UI', 20),
        'color': Color(0, 0, 0),
        'background_color': background_color
    }


def main():
    init()
    loop(configure_display(), time.Clock())
    quit()


if __name__ == '__main__':
    main()
