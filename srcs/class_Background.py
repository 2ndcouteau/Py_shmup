#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame

from class_Entities	import Entities
from constants		import (X_WINDOW,
							Y_WINDOW,
							IMG_LEVEL1_BACKGROUND,
							IMG_MAIN_MENU_BACKGROUND,
							IMG_LEVEL_MENU_BACKGROUND_FULL,
							IMG_LEVEL_MENU_BACKGROUND_TIER,
							GAME,
							MAIN_MENU,
							LEVEL_MENU,
							NEUTRAL,
							BLUE)

class Background(Entities):
	def __init__(self, g, pos, image_file, mode):
		Entities.__init__(self, _hp = None, _life = None, _speed = 1, _type = NEUTRAL)

		if (mode is LEVEL_MENU):
			self.image = image_file
		else :
			self.image = image_file.convert()

		self.size = self.image.get_size()
		if (mode is LEVEL_MENU):
			self.rect = self.image.fill(BLUE)
			self.image.set_alpha(50)
		elif (mode is GAME) :
			scale_x = float(X_WINDOW) / self.size[0]
			scale_y = float(Y_WINDOW) / self.size[1]
			self.size = (self.size[0] * scale_x, self.size[1] * scale_x)
			self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
			self.rect = self.image.get_rect()
		else :
			self.rect = self.image.get_rect()


		self.rect.x = pos[0]
		self.rect.y = pos[1]

		g.all_sprites.add(self)

		if mode is GAME :
			g.sprites_level_backgrounds.add(self)
		elif mode is MAIN_MENU :
			g.sprites_main_menu_backgrounds.add(self)
		else :
			g.sprites_level_menu_backgrounds.add(self)
