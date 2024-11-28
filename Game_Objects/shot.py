import pygame
from pygame import Surface

from Game_Objects.circle_shape import CircleShape
from utilities.constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: int):
        self.position += self.velocity * dt