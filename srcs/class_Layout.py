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

	def scroll_level_background(g):
		g.level_backgrounds[0].rect.y += 1
		g.level_backgrounds[1].rect.y += 1

		if g.level_backgrounds[0].rect.y >= Y_WINDOW:
			g.level_backgrounds[0].rect.y = -Y_WINDOW
		if g.level_backgrounds[1].rect.y >= Y_WINDOW:
			g.level_backgrounds[1].rect.y = -Y_WINDOW

	def draw_game_sprites(self, g):
		# Draw All Spirte list
		# g.all_sprites.draw(g.window)
		g.sprites_level_backgrounds.draw(g.window)
		g.sprites_players.draw(g.window)
		g.sprites_enemies.draw(g.window)
		g.sprites_enemies_shoots.draw(g.window)
		g.sprites_allies_shoots.draw(g.window)

		g.sprites_level_text.draw(g.window)

		# print(g.sprites_explosions)
		g.sprites_explosions.draw(g.window)

		# g.sprites_neutrals.draw(g.window)

			# Refresh ALL the Display
				# update() is faster than flip()
			# pygame.display.update(g.all_sprites_list)

		pygame.display.flip()

	def draw_level_menu_sprites(self, g):

		g.sprites_level_backgrounds.draw(g.window)
		g.sprites_players.draw(g.window)
		g.sprites_enemies.draw(g.window)

		# g.sprites_level_text.draw(g.window)

		g.sprites_level_menu_backgrounds.draw(g.window)
		g.sprites_level_menu_text.draw(g.window)

		pygame.display.flip()

	def draw_main_menu_sprites(self, g):

		g.sprites_main_menu_backgrounds.draw(g.window)
		g.sprites_main_menu_text.draw(g.window)

		pygame.display.flip()
