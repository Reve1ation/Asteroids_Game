import pygame

from Game_Objects.circle_shape import CircleShape
from Game_Objects.player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

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

    Player.containers = (updatable_group, drawable_group)

    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for drawable in drawable_group:
            drawable.draw(screen)
        for updatable in updatable_group:
            updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(120)/1000



if __name__ == "__main__":
    main()