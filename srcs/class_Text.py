#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *

from constants			import (Y_WINDOW,
								X_WINDOW,
								FONT,
								GAME,
								MAIN_MENU,
								LEVEL_MENU,
								WHITE,
								BLACK,
								RED,
								GREEN,
								BLUE,
								YELLOW)


class Text(pygame.sprite.Sprite):
	def __init__(self, g, msg, pos, cx, cy):
		pygame.sprite.Sprite.__init__(self)

		font = pygame.font.Font(FONT, 16)
		self.image = font.render(msg, True, (255, 255, 255))
		self.rect = self.image.get_rect()
		position_text(self, list(pos), cx, cy)

		g.all_sprites.add(self)

def position_text(self, pos, cx, cy):
	#cx= center_x, cy= center_y
	self.size = self.image.get_size()
	if cx :
		pos[0] -= self.size[0] / 2
	if cy :
		pos[1] -= self.size[1] / 2

	self.rect.x += pos[0]
	self.rect.y += pos[1]

class Level_text(pygame.sprite.Sprite):
	def __init__(self, g, msg, pos, cx=False, cy=False):
		Text.__init__(self, g, msg, pos, cx, cy)

		g.sprites_level_text.add(self)


class Level_menu_text(pygame.sprite.Sprite):
	def __init__(self, g, msg, pos, cx=False, cy=False):
		pos = (g.level_menu_backgrounds[1].rect.x + pos[0], g.level_menu_backgrounds[1].rect.y + pos[1])
		Text.__init__(self, g, msg, pos, cx, cy)

		g.sprites_level_menu_text.add(self)


class Main_menu_text(pygame.sprite.Sprite):
	def __init__(self, g, msg, pos, cx=False, cy=False):
		Text.__init__(self, g, msg, pos, cx , cy)

		g.sprites_main_menu_text.add(self)
