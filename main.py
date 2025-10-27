import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (updatable,drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        updatable.update(dt)
        for object in asteroids:
            if object.collide(player):
                print("Game over!")
                sys.exit()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = game_clock.tick(60) / 1000

    pygame.quit()
       

if __name__ == "__main__":
    main()
