#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame

from class_Entities	import Entities
from constants		import (X_WINDOW,
							Y_WINDOW,
							IMG_BACKGROUND,
							NEUTRAL)

class Background(Entities):
	def __init__(self, g, y_start):
		Entities.__init__(self, _hp = None, _life = None, _speed = 1, _type = NEUTRAL)

		self.image = IMG_BACKGROUND.convert()
		self.size = self.image.get_size()
		scale_x = float(X_WINDOW) / self.size[0]
		scale_y = float(Y_WINDOW) / self.size[1]
		self.size = (self.size[0] * scale_x, self.size[1] * scale_x)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		self.rect = self.image.get_rect()
		self.rect.y = y_start

		g.all_sprites_list.add(self)
		g.sprites_backgrounds_list.add(self)
