import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
	pygame.init()
	fps_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	player = Player(x, y)

	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = updatable
	asteroidfield = AsteroidField()

	Shot.containers = (shots, updatable, drawable)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


		for obj in updatable:
			obj.update(dt)
		
		for asteroid in asteroids:
			if asteroid.is_colliding(player):
				print("Game over!")
				sys.exit(0)
			for bullet in shots:
				if asteroid.is_colliding(bullet):
					asteroid.split()
					bullet.kill()
			
			

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()


	
		dt = fps_clock.tick(60)/1000


	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	print("Starting asteroids!")

if __name__ == "__main__":
	main()
