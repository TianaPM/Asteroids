import pygame
from constants import *
import player

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)

    p1 = player.Player(SCREEN_WIDTH/2, SCREEN_WIDTH/2)

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for drawables in drawable:
            drawables.draw(screen)

        updatable.update(dt)

        pygame.display.flip()    

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
