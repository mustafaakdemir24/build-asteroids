import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-class must override
        pass

    def update(self, dt):
        # sub-class must override
        pass

    def collides_with(self, obj):
        return self.position.distance_to(obj.position) <= self.radius + obj.radius
