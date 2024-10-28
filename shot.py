import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        # Add bullet to relevant groups
        #if hasattr(self, "containers"):
        #    self.add(*self.containers)

    def draw(self, screen):
        # Draw bullet as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the bullet in a straight line
        self.position += self.velocity * dt
