#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
import time

class Entities(pygame.sprite.Sprite):
	def __init__(self, _hp, _lives, _speed, _type):
		pygame.sprite.Sprite.__init__(self)
		self.hp = _hp
		self.lives = _lives
		self.speed = _speed
		self.type = _type

		self.score = 0
		self.time = time.time()
		self.start_time = time.time()
