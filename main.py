import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
 print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
 print(f"Screen width: {SCREEN_WIDTH}")
 print(f"Screen height: {SCREEN_HEIGHT}")
 pygame.init()
 screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 clock = pygame.time.Clock()
 dt = 0
 updatable = pygame.sprite.Group()
 drawable = pygame.sprite.Group()
 asteroids = pygame.sprite.Group()
 shots = pygame.sprite.Group()
 Player.containers = (updatable, drawable)
 Asteroid.containers = (asteroids, updatable, drawable)
 AsteroidField.containers = (updatable)
 asteroid_field = AsteroidField()
 Shot.containers = (shots, updatable, drawable)
 player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
 while True:
   log_state()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
           return
      screen.fill("black")
      for obj in drawable:
         obj.draw(screen)
      updatable.update(dt)
      for asteroid in asteroids:
         if player.collides_with(asteroid):
             log_event("player_hit")
             print("Game Over!")
             sys.exit()
      for asteroid in asteroids:
         for shot in shots:
             if shot.collides_with(asteroid):
                 log_event("asteroid_shot")
                 asteroid.split()
                 shot.kill()
   dt = (clock.tick(60) /1000)  # Limit to 60 FPS
   pygame.display.flip()  # Update the full display Surface to the screen

if __name__ == "__main__":
    main()
