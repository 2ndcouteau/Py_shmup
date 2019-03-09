#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from random import randint


from class_Entities	import Entities
from class_Shoot	import Shoot

from constants			import (X_WINDOW, Y_WINDOW,
								ENEMIES,
								IMG_PLAYER,
								ENEMIES_SHOOT_FREQUENCY,
								RED,
								DOWN)

class Enemy(Entities):
	def __init__(self, g):
		Entities.__init__(self, _hp = 1, _lives = 0, _speed = 5, _type = ENEMIES)
		self.name = "Enemy"

		self.g = g
		self.timer = 0

		# Load image from media
		self.image = IMG_PLAYER.convert_alpha()

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 3, self.size[1] / 3)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		self.image = pygame.transform.rotate(self.image, 180);
		self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(randint(int(self.size[0]), X_WINDOW) - int(self.size[0]) , -int(self.size[1]))

		while pygame.sprite.spritecollide(self, g.sprites_enemies, False):
			self.rect.centery -= self.size[1] / 2

		self.mask = pygame.mask.from_surface(self.image)

		g.all_sprites.add(self)
		g.sprites_enemies.add(self)


	def shoot(self):
		self.timer -= self.g.dt
		if (self.timer <= 0):
			Shoot(self.g, ENEMIES, self.speed * 2, self.rect.centerx, self.rect.bottom)
			# Reset the countdown shoot timer + salt time
			self.timer = ENEMIES_SHOOT_FREQUENCY + randint(0, 1000)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def update(self):
		self.move(DOWN)
		self.shoot()

		# If the enemy go out the window, unreference it
		if (self.rect.y > Y_WINDOW):
			self.kill()
