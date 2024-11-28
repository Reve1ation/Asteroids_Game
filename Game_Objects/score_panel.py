import pygame
from pygame import Surface

from Game_Objects.rectangle_shape import RectangleShape


class ScorePanel(RectangleShape):
    def __init__(self, x, y, width, height, color, font, font_size, text_color):
        super().__init__(x, y, width, height, color)
        self.font = pygame.font.Font(font, font_size)
        self.text_color = text_color
        self.score = 0

    def update(self, dt: int):
        pass

    def draw(self, screen: Surface):
        super().draw(screen)
        score_text = self.font.render(f"Score: {self.score}", True, self.text_color)
        screen.blit(score_text, (self.rect.x + 10, self.rect.y + 10))
