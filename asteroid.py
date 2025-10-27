import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_angle1, new_angle_2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        smaller_1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_1.velocity = new_angle1 * 1.2
        smaller_2 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_2.velocity = new_angle_2 * 1.2