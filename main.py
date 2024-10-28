# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create two groups: one for objects that ned to be updated, one for objects that need to be drawn

    # Create groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers for each class
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable,)

    # Instantiate the player in the center of the screen and automatically add to groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for bullet in shots:
            for asteroid in asteroids:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        # Fill the screen with black
        screen.fill("black")

        # Manually draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()
        
        # limit the framerate o 60 FPS
        # Limit the frame rate to 60 FPS and calculate dt
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
   main()
