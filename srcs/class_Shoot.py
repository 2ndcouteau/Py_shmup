#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from math			import degrees, atan

from class_Entities	import Entities
from constants		import (X_WINDOW,
							Y_WINDOW,
							UP, RIGHT_SHOT, LEFT_SHOT,
							ALLIES,
							ENEMIES,
							IMG_LASER_PLAYER,
							IMG_LASER_ENEMY)
							# SOUND_SHOOT_PLAYER,
							# SOUND_SHOOT_ENNEMIES)

class Shoot(Entities):
	def __init__(self, g, type, speed, x, y, direction=UP):
		Entities.__init__(self, _hp = 1, _lives = 0, _speed = speed, _type = type)

		# Load image from media
		# self.image = IMG_PLAYER.convert_alpha()
		# g.Rect_entities.append(pygame.draw.circle(g.window, [120, 0, 255], (g.player.rect[0], g.player.rect[1] + 15), 5))
		if (self.type == ALLIES):
			self.image = IMG_LASER_ENEMY.convert_alpha()
		else :
			self.image = IMG_LASER_PLAYER.convert_alpha()
			self.sound = None

		self.g = g

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 2, self.size[1] / 2)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))

		self.mask = pygame.mask.from_surface(self.image)

		# Init shoot ship position
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x

		if (self.type == ALLIES):
			self.set_direction(g, direction)
			g.sprites_allies_shoots.add(self)
		else:
			self.target_player(g)
			g.sprites_enemies_shoots.add(self)

		# if self.sound:
		# 	self.sound.play()
		g.all_sprites.add(self)

	def set_direction(self, g, direction):
		self.direction = direction
		if (self.direction[1] != 0) :
			angle = degrees(atan(self.direction[0] / self.direction[1]))
			self.image = pygame.transform.rotate(self.image, angle);


	def target_player(self, g):
		self.direction = g.player.rect.centerx - self.rect.centerx, g.player.rect.top - self.rect.centery

		if (self.direction[1] != 0) :
			angle = degrees(atan(self.direction[0] / self.direction[1]))
		else :
			angle = 0

		if abs(self.direction[0]) > abs(self.direction[1]):
			if (self.direction[0] != 0):
				self.direction = self.direction[0] / abs(self.direction[0]), self.direction[1] / abs(self.direction[0])
		else :
			if (self.direction[1] != 0):
				self.direction = self.direction[0] / abs(self.direction[1]), self.direction[1] / abs(self.direction[1])

		self.image = pygame.transform.rotate(self.image, angle);


	def move(self):
		self.rect = self.rect.move(self.direction[0] * self.speed, self.direction[1] * (self.speed * self.g.speed_game))

	def update(self):
		self.move()

		# If the shoot go out the window, unreference it
		if (self.type == ENEMIES):
			if (self.rect.top > Y_WINDOW or self.rect.bottom < -20 or self.rect.left > X_WINDOW or self.rect.right < 0):
				self.kill()
		elif (self.rect.bottom < 0 and self.type == ALLIES):
			self.kill()

class Simple_shot():
	def __init__(self, g, type, shooter):
		self.name = "Simple shot"
		Shoot(g, type, shooter.speed + 1, shooter.rect.centerx, shooter.rect.top)

class Double_shots():
	def __init__(self, g, type, shooter):
		self.name = "Double shots"
		Shoot(g, type, shooter.speed + 1, shooter.rect.centerx + 7, shooter.rect.top)
		Shoot(g, type, shooter.speed + 1, shooter.rect.centerx - 7, shooter.rect.top)

class Triple_shots():
	def __init__(self, g, type, shooter):
		self.name = "Triple shots"
		Shoot(g, type, shooter.speed + 10, shooter.rect.centerx + 10, shooter.rect.top + 15, direction=RIGHT_SHOT)
		Shoot(g, type, shooter.speed + 10, shooter.rect.centerx - 12, shooter.rect.top + 15, direction=LEFT_SHOT)
		Shoot(g, type, shooter.speed + 1, shooter.rect.centerx, shooter.rect.top + 20)
