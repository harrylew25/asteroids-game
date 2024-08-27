
import pygame
import random
from circleshape import CircleShape
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        positive_angle = self.velocity.rotate(random_angle)
        negative_angle = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        positive_angle_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        positive_angle_asteroid.velocity = positive_angle * ASTEROID_POST_SPLIT_SPEED

        negative_angle_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        negative_angle_asteroid.velocity = negative_angle * ASTEROID_POST_SPLIT_SPEED