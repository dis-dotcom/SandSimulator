import pygame
from pygame.surface import Surface


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.updated = False
        self.location = x, y

    def set(self, x, y):
        self.x, self.y = x, y
        self.updated = True
        self.location = x, y

    def reset(self):
        self.updated = False


class Canvas:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.common_color = (255, 0, 0)
        self.background_color = None
        self.surface_rect = surface.get_rect()

    def fill(self):
        self.surface.fill(self.background_color, self.surface_rect)

    def paint(self, vector: Vector):
        pygame.draw.line(self.surface, self.common_color, vector.location, vector.location)
