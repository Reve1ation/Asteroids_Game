import sys

import pygame

from Game_Objects.asteroid import Asteroid
from Game_Objects.asteroidfield import AsteroidField
from Game_Objects.player import Player
from Game_Objects.shot import Shot
from utilities.constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} px")
    print(f"Screen height: {SCREEN_HEIGHT} px")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group  = pygame.sprite.Group()
    asteroids_group  = pygame.sprite.Group()
    shots_group  = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (shots_group, updatable_group, drawable_group)

    AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for drawable in drawable_group:
            drawable.draw(screen)
        for updatable in updatable_group:
            updatable.update(dt)
        for asteroid in asteroids_group:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots_group:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(120)/1000



if __name__ == "__main__":
    main()