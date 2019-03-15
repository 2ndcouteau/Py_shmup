#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame

from class_Entities	import Entities
from constants		import (X_WINDOW, Y_WINDOW,
							DOWN, RIGHT, LEFT,
							BACKGROUND_DELAY,
							IMG_LEVEL1_BACKGROUND,
							IMG_MAIN_MENU_BACKGROUND,
							IMG_LEVEL_MENU_BACKGROUND_FULL,
							IMG_LEVEL_MENU_BACKGROUND_TIER,
							NEUTRAL,
							BLACK)

class Background(Entities):
	def __init__(self, g):
		Entities.__init__(self, _hp = None, _lives = None, _speed = 1, _type = NEUTRAL)
		self.g = g

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed * self.g.speed_game)

class Backgrounds():
	def __init__(self):
		self.backgrounds = []

class Level_background(Background):
	def __init__(self, g, pos=(0, 0), image_file=IMG_LEVEL1_BACKGROUND):
		Background.__init__(self, g)

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

	def update(self):
		self.move(DOWN)

		if (self.rect.top >= Y_WINDOW):
			self.rect.top = -Y_WINDOW


class Main_menu_background(Background):
	def __init__(self, g, pos=(0, 0), image_file=IMG_MAIN_MENU_BACKGROUND):
		Background.__init__(self, g)
		self.timer_move = BACKGROUND_DELAY
		self.image = image_file.convert()

		self.direction = LEFT
		self.size = self.image.get_size()
		scale_y = float(Y_WINDOW) / self.size[1]
		self.size = (self.size[0] * scale_y, self.size[1] * scale_y)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))

		self.rect = self.image.get_rect()
		self.rect.x = pos[0] - 80
		self.rect.y = pos[1]

		g.all_sprites.add(self)
		g.sprites_main_menu_backgrounds.add(self)

	def update(self):
		if (self.rect.left >= 0):
			self.direction = LEFT
		elif (self.rect.right <= X_WINDOW):
			self.direction = RIGHT

		self.timer_move -= self.g.dt
		if (self.timer_move <- 0):
			self.move(self.direction)
			self.timer_move = BACKGROUND_DELAY


class Level_menu_background(Background):
	def __init__(self, g, pos, image_file, opacity=255):
		Background.__init__(self, g)

		self.image = image_file

		self.size = self.image.get_size()

		self.rect = self.image.fill(BLACK)
		self.image.set_alpha(opacity)

		self.rect.x = pos[0]
		self.rect.y = pos[1]

		g.all_sprites.add(self)
		g.sprites_level_menu_backgrounds.add(self)

class Main_menu_backgrounds():
	def __init__(self, g):
		Backgrounds.__init__(self)

		self.backgrounds.insert(0, Main_menu_background(g, (0, 0), IMG_MAIN_MENU_BACKGROUND))

class Level_backgrounds(Backgrounds):
	def __init__(self, g):
		Backgrounds.__init__(self)

		self.backgrounds.insert(0, Level_background(g, (0, 0), IMG_LEVEL1_BACKGROUND))
		self.backgrounds.insert(1, Level_background(g, (0, -Y_WINDOW), IMG_LEVEL1_BACKGROUND))

	def reinitialization(self, g):
		g.all_sprites.add(g.sprites_level_backgrounds)

		g.level_backgrounds.backgrounds[0].rect.top = 0
		g.level_backgrounds.backgrounds[1].rect.top = -Y_WINDOW

class Level_menu_backgrounds(Backgrounds):
	def __init__(self, g):
		Backgrounds.__init__(self)

		self.backgrounds.insert(0, Level_menu_background(g, (0, 0), IMG_LEVEL_MENU_BACKGROUND_FULL, opacity=100))
		self.backgrounds.insert(1, Level_menu_background(g, (X_WINDOW / 4, Y_WINDOW / 4), IMG_LEVEL_MENU_BACKGROUND_TIER, opacity=150))
