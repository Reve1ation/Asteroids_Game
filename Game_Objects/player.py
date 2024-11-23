import pygame
from pygame import Surface

from Game_Objects.circle_shape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def update(self, dt: int) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * (-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * (-1))

    def rotate(self, dt: int) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt: int) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


