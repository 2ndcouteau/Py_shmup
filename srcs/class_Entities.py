#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame

class Entities(pygame.sprite.Sprite):
	def __init__(self, _hp, _life, _speed, _type):
		pygame.sprite.Sprite.__init__(self)
		self.hp = _hp
		self.life = _life
		self.speed = _speed
		self.type = _type

		self.score = 0
		self.time = 0
