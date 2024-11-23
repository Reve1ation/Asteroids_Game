from abc import abstractmethod, ABC

import pygame
from pygame import Surface


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @abstractmethod
    def draw(self, screen: Surface):
        # sub-classes must override
        pass

    @abstractmethod
    def update(self, dt: int):
        # sub-classes must override
        pass