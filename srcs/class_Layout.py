#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *

from class_Background	import Background
from constants			import (Y_WINDOW,
								X_WINDOW)

class Layout():
	def __init__(self):
		self.timer = 0 # 1seconde
		self.dt = 0

	def scroll_background(g):
		g.backgrounds[0].rect.y += 1
		g.backgrounds[1].rect.y += 1

		if g.backgrounds[0].rect.y >= Y_WINDOW:
			g.backgrounds[0].rect.y = -Y_WINDOW
		if g.backgrounds[1].rect.y >= Y_WINDOW:
			g.backgrounds[1].rect.y = -Y_WINDOW

	def draw_sprites(self, g):
		# Draw All Spirte list
		# g.all_sprites_list.draw(g.window)
		g.sprites_backgrounds_list.draw(g.window)
		g.sprites_players_list.draw(g.window)
		g.sprites_enemies_list.draw(g.window)
		g.sprites_enemies_shoots_list.draw(g.window)
		g.sprites_allies_shoots_list.draw(g.window)

		g.sprites_text_list.draw(g.window)

		# g.sprites_neutrals.draw(g.window)

			# Refresh ALL the Display
				# update() is faster than flip()
			# pygame.display.update(g.all_sprites_list)

		pygame.display.flip()

	# def message(g):
	#
	# 	Text(g, "Hello")
