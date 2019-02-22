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
							BLACK)

class Background(Entities):
	def __init__(self):
		Entities.__init__(self, _hp = None, _lives = None, _speed = 1, _type = NEUTRAL)


class Level_background(Background):
	def __init__(self, g, pos, image_file, mode):
		Background.__init__(self)
		self.image = image_file.convert()
		self.size = self.image.get_size()

		scale_x = float(X_WINDOW) / self.size[0]
		scale_y = float(Y_WINDOW) / self.size[1]
		self.size = (self.size[0] * scale_x, self.size[1] * scale_x)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		self.rect = self.image.get_rect()

		self.rect.x = pos[0]
		self.rect.y = pos[1]

		g.all_sprites.add(self)
		g.sprites_level_backgrounds.add(self)

class Main_menu_background(Background):
	def __init__(self, g, pos, image_file, mode):
		Background.__init__(self)


		self.image = image_file.convert()

		self.size = self.image.get_size()
		scale_y = float(Y_WINDOW) / self.size[1]
		self.size = (self.size[0] * scale_y, self.size[1] * scale_y)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))

		self.rect = self.image.get_rect()
		self.rect.x = pos[0] - 80
		self.rect.y = pos[1]

		g.all_sprites.add(self)
		g.sprites_main_menu_backgrounds.add(self)

class Level_menu_background(Background):
	def __init__(self, g, pos, image_file, mode, opacity=255):
		Background.__init__(self)

		self.image = image_file

		self.size = self.image.get_size()

		self.rect = self.image.fill(BLACK)
		self.image.set_alpha(opacity)

		self.rect.x = pos[0]
		self.rect.y = pos[1]

		g.all_sprites.add(self)
		g.sprites_level_menu_backgrounds.add(self)
