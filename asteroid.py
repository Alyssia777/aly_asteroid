import pygame
import circleshape
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20,50)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = 1.2* self.velocity.rotate(angle)
            asteroid2.velocity = 1.2* self.velocity.rotate(-angle)

            return [asteroid1, asteroid2]
