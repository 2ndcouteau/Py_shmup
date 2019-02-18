#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame

from class_Entities	import Entities
from class_Shoot	import Shoot
from constants		import (X_WINDOW,
							Y_WINDOW,
							IMG_PLAYER,
							PLAYER_HP,
							ALLIES,
							PLAYER_SHOOT_FREQUENCY)

class Player(Entities):

	def __init__(self, g):
		Entities.__init__(self, _hp = PLAYER_HP, _life = 3, _speed = 15, _type = ALLIES)
		self.name = "Player"

		self.timer = 0

		# Load image from media
		self.image = IMG_PLAYER.convert_alpha()

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 3, self.size[1] / 3)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		# self.image = pygame.transform.rotate(self.image, -90);
		self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect()
		self.rect = self.rect.move((X_WINDOW / 2) - self.size[0] / 2, Y_WINDOW - 150)

		g.all_sprites.add(self)
		g.sprites_players.add(self)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def shoot(self, g):
		self.timer -= g.dt
		if self.timer <= 0:
			Shoot(g, ALLIES, self.speed + 1, self.rect.centerx, self.rect.top)
			# Reset the countdown timer to one second.
			print (self.timer)
			self.timer = PLAYER_SHOOT_FREQUENCY
			print (self.timer)

	def reinitialization(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP

		g.sprites_players.add(self)
		g.all_sprites.add(self)
