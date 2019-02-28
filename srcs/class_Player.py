#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
import time

from random			import randint
from class_Entities	import Entities
from class_Shoot	import Shoot
from constants		import (X_WINDOW,
							Y_WINDOW,
							IMG_PLAYER,
							PLAYER_HP,
							PLAYER_LIVES,
							ALLIES,
							PLAYER_SHOOT_FREQUENCY)

class Player(Entities):

	def __init__(self, g):
		Entities.__init__(self, _hp = PLAYER_HP, _lives = PLAYER_LIVES, _speed = 15, _type = ALLIES)
		self.name = "Player"

		self.timer = 0
		self.sound_shoot = g.sound_shoot
		self.sound_shoot.set_volume(0.5)


		# Load image from media
		self.image = IMG_PLAYER.convert_alpha()

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 3, self.size[1] / 3)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		# self.image = pygame.transform.rotate(self.image, -90);
		self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect(center=[(X_WINDOW / 2) - self.size[0] / 2, Y_WINDOW - 150])
		# self.rect = self.rect.move((X_WINDOW / 2) - self.size[0] / 2, Y_WINDOW - 150)

		g.all_sprites.add(self)
		g.sprites_players.add(self)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def shoot(self, g):
		self.timer -= g.dt
		if self.timer <= 0:
			Shoot(g, ALLIES, self.speed + 1, self.rect.centerx, self.rect.top)

			self.sound_shoot.play()
			# self.sound_shoot[randint(0, 5)].play()
			# print("nb_sound == " + str(self.sound_shoot.get_num_channels()))

			# Reset the countdown timer to one second.
			self.timer = PLAYER_SHOOT_FREQUENCY

	def init_game(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP

		if self.lives < 0:
			self.start_time = time.time()
			self.time = time.time()
			self.score = 0
			self.lives = PLAYER_LIVES

		g.sprites_players.add(self)
		g.all_sprites.add(self)


	def continue_level(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP

		g.sprites_players.add(self)
		g.all_sprites.add(self)


	def init_level(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP

		self.start_time = time.time()
		self.time = time.time()
		self.score = 0

		g.sprites_players.add(self)
		g.all_sprites.add(self)

	def update(self):
		self.time = time.time() - self.start_time
