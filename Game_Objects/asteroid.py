import pygame
from pygame import Surface

from Game_Objects.circle_shape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt