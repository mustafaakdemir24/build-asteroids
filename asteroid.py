import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super()__init__(x, y, PLAYER_RADIUS)

        # Add asteroid to relevant groups
        if hasattr(self, "containers"):
            self.add(*self.containers)

    def drwa(self, screen):
        # Draw asteroid as a circle
        pygmae.draw.circle(screen, pygame.Color("White"), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line
        self.position += self.velocity * dt
