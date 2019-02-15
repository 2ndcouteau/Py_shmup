#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from math			import degrees, atan

from class_Entities	import Entities
from constants		import (X_WINDOW,
							Y_WINDOW,
							UP,
							ALLIES,
							ENEMIES,
							IMG_LASER_PLAYER,
							IMG_LASER_ENEMY)

class Shoot(Entities):
	def __init__(self, g, type, speed, x, y):
		Entities.__init__(self, _hp = 1, _life = 0, _speed = speed, _type = type)
		self.name = "Shoot"

		# Load image from media
		# self.image = IMG_PLAYER.convert_alpha()
		# g.Rect_entities.append(pygame.draw.circle(g.window, [120, 0, 255], (g.player.rect[0], g.player.rect[1] + 15), 5))
		if self.type == ALLIES:
			self.image = IMG_LASER_PLAYER.convert_alpha()
		else :
			self.image = IMG_LASER_ENEMY.convert_alpha()
			# self.image = pygame.Surface((4, 15))


		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 2, self.size[1] / 2)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))


		# Init shoot ship position
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x

		if self.type == ALLIES:
			# self.image.fill(BLUE)
			self.direction = UP
			g.sprites_allies_shoots.add(self)
		else:
			# self.image.fill(RED)
			# self.direction = DOWN
			self.target_player(g)
			g.sprites_enemies_shoots.add(self)

		g.all_sprites.add(self)

	def target_player(self, g):
		self.direction = g.player.rect.centerx - self.rect.centerx, g.player.rect.top - self.rect.centery

		angle = degrees(atan(self.direction[0] / self.direction[1]))

		print (self.direction)
		if abs(self.direction[0]) > abs(self.direction[1]):
			if self.direction[0] != 0:
				self.direction = self.direction[0] / abs(self.direction[0]), self.direction[1] / abs(self.direction[0])
		else :
			if self.direction[1] != 0:
				self.direction = self.direction[0] / abs(self.direction[1]), self.direction[1] / abs(self.direction[1])
		print (self.direction)

		self.image = pygame.transform.rotate(self.image, angle);


	def move(self):
		self.rect = self.rect.move(self.direction[0] * self.speed, self.direction[1] * self.speed)

	def update(self):
		self.move()

		# If the shoot go out the window, unreference it
		if self.rect.top > Y_WINDOW and self.type == ENEMIES:
			self.kill()
		elif self.rect.bottom < 0 and self.type == ALLIES:
			self.kill()
