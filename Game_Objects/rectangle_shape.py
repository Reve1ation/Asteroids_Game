from abc import ABC, abstractmethod
import pygame
from pygame import Surface


class RectangleShape(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, width, height, color):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color

    @abstractmethod
    def update(self, dt: int) -> None:
        # sub-classes must override
        pass

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)
