#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from random import randint


from class_Entities	import Entities
from class_Shoot	import Shoot

from constants			import (X_WINDOW, Y_WINDOW,
								ENEMIES,
								IMG_PLAYER,
								IMG_ENEMY_1, IMG_ENEMY_2, IMG_ENEMY_3, IMG_ENEMY_4,
								ENEMIES_SHOOT_FREQUENCY,
								RED_ENEMY, WHITE, BLUE,
								DOWN)

class Enemy(Entities):
	def __init__(self, g):
		Entities.__init__(self, _hp = 1, _lives = 0, _speed = 5, _type = ENEMIES)
		self.name = "Enemy"

		self.g = g
		self.timer = 0

		# Load image from media
		self.image = IMG_ENEMY_4.convert_alpha()

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 3, self.size[1] / 3)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		# self.image = pygame.transform.rotate(self.image, 180);
		self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(randint(int(self.size[0]), X_WINDOW) - int(self.size[0]) , -int(self.size[1]))

		while pygame.sprite.spritecollide(self, g.sprites_enemies, False):
			self.rect.centery -= self.size[1] / 2

		self.mask = pygame.mask.from_surface(self.image)


		# self.pixels_1 = pygame.transform.threshold(
		# 			dest_surf=None,
		# 			surf=self.image,
		# 			search_color=WHITE,
		# 			threshold=(20, 20, 20, 0), # rgba
		# 			set_color=None,
		# 			set_behavior=0,
		# 			search_surf=None,
		# 			inverse_set=True
		# 		)
		#
		#
		# self.pixels_within_threshold = pygame.transform.threshold(
		# 			dest_surf=self.image,
		# 			surf=self.image,
		# 			search_color=None,
		# 			threshold=(255, 255, 255, 0), # rgba
		# 			set_color=RED_ENEMY,
		# 			set_behavior=1,
		# 			search_surf=self.pixels_1,
		# 			inverse_set=False
		# 		)
		# self.image_pixel_array = pygame.PixelArray(self.image)
		# self.image_pixel_array.replace(WHITE, RED)
		# self.image_pixel_array = None
		# del self.image_pixel_array


		g.all_sprites.add(self)
		g.sprites_enemies.add(self)


	def shoot(self):
		self.timer -= self.g.dt
		if (self.timer <= 0):
			Shoot(self.g, ENEMIES, self.speed * 2, self.rect.centerx, self.rect.bottom)
			# Reset the countdown shoot timer + salt time
			self.timer = (ENEMIES_SHOOT_FREQUENCY + randint(0, 1000)) / self.g.speed_game

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed * self.g.speed_game, direction[1] * self.speed * self.g.speed_game)

	def update(self):
		self.move(DOWN)
		self.shoot()

		# If the enemy go out the window, unreference it
		if (self.rect.y > Y_WINDOW):
			self.kill()
