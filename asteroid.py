import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2

            asteroid = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid.velocity = pygame.math.Vector2.rotate(self.velocity, (0 - random_angle)) * 1.2

