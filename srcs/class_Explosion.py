#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *
from random			import randint

from constants			import (X_WINDOW,
								Y_WINDOW,
								EXPLOSION_FRAME_RATE)




class Explosion(pygame.sprite.Sprite):
	def __init__(self, g, center, explosion_style):
		pygame.sprite.Sprite.__init__(self)

		self.explosion_style = explosion_style
		self.image = g.explosion_imgs[self.explosion_style][0]
		self.sound = g.sound_explosion
		self.sound.set_volume(0.5)
		if (g.opt_sfx == True):
			self.sound.play()

		self.rect = self.image.get_rect()
		self.rect.center = center

		self.timer = 0
		self.frame = 0
		self.frame_rate = EXPLOSION_FRAME_RATE

		self.len = len(g.explosion_imgs[self.explosion_style])

		g.all_sprites.add(self)
		g.sprites_explosions.add(self)

		self.g = g

	def update(self):
		self.timer -= self.g.dt
		if (self.timer <= 0):
			self.frame += 1
			if (self.frame == self.len):
				self.kill()
			else:
				center = self.rect.center  ## ??
				self.image = self.g.explosion_imgs[self.explosion_style][self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

			# Reset the countdown shoot timer + salt time
			self.timer = self.frame_rate
