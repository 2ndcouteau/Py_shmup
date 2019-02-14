#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *

from constants			import (Y_WINDOW,
								X_WINDOW,
								FONT)


class Text(pygame.sprite.Sprite):
	def __init__(self, g, msg):
		pygame.sprite.Sprite.__init__(self)

		font = pygame.font.Font(FONT, 16)
		print(font)
		self.image = font.render(msg, True, (255, 255, 255), (X_WINDOW / 2, Y_WINDOW / 2))
		print(self.image)
		self.rect = self.image.get_rect()
		print(self.rect)

		g.sprites_text_list.add(self)
