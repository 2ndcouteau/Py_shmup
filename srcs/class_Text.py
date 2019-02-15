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
	def __init__(self, g, msg, mode):
		pygame.sprite.Sprite.__init__(self)

		font = pygame.font.Font(FONT, 16)
		print(font)
		self.image = font.render(msg, True, (255, 255, 255), (X_WINDOW / 2, Y_WINDOW / 2))
		print(self.image)
		self.rect = self.image.get_rect()
		print(self.rect)


		g.all_sprites.add(self)
		if mode is GAME :
			g.sprites_level_text.add(self)
		elif mode is MAIN_MENU :
			g.sprites_main_menu_text.add(self)
		else :
			g.sprites_level_menu_text.add(self)
