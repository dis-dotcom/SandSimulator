from pygame.surface import Surface
from pygame.font import SysFont
from pygame import display
from config import Config
from vector import Canvas


class GUI:
    def __init__(self, config: Config):
        self.config = config
        self.font = self.__get_default_font__()
        self.surface = None
        self.canvas = None

    def configure(self) -> Canvas:
        self.surface = display.set_mode(self.config.canvas_size)
        self.canvas = Canvas(self.surface)
        self.canvas.background_color = self.config.background_color
        display.set_caption('')
        icon = Surface([50, 50])
        icon.fill(self.config.background_color)
        display.set_icon(icon)
        return self.canvas

    def info(self, points: list, begin: float, end: float):
        elapsed = int((end - begin) * 1000)
        info = {
            'Objects': str(len(points)),
            'Frozen': f'{self.percent_frozen(points)} %',
            'Elapsed': f'{elapsed} ms.'
        }
        self.surface.blit(self.get_debug_surface(info), (0, 0))

    def get_debug_surface(self, info: dict) -> Surface:
        y = 0
        size = 500, len(info) * (self.font['size'] + 5)
        surface = Surface(size)
        surface.fill(self.font['background_color'])
        for key in info.keys():
            line = f'{key}: {info[key]}'
            surface.blit(self.font['value'].render(line, True, self.font['color']), (15, y))
            y += self.font['size']

        return surface

    def __get_default_font__(self):
        return {
            'value': SysFont('Segoe UI', self.config.text_size),
            'color': self.config.text_color,
            'background_color': self.config.background_color,
            'size': self.config.text_size
        }

    def percent_frozen(self, points: list) -> float:
        return self.get_formatted_value(self.count_frozen(points), len(points)) if len(points) > 0 else 0.00

    def get_formatted_value(self, a, b) -> float:
        return round((a / b) * 100, 2)

    def count_frozen(self, points: list) -> int:
        count = 0
        for point in points:
            if point.frozen:
                count += 1
        return count
