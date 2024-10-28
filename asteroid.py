import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Add asteroid to relevant groups
        #if hasattr(self, "containers"):
        #    self.add(*self.containers)

    def draw(self, screen):
        # Draw asteroid as a circle
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2
