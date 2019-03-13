#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *

from class_Background	import Background
from constants			import (Y_WINDOW, X_WINDOW,
								F_MAIN_MENU, F_GAMEOVER_MENU,
								FONT)

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

	def draw_level_sprites(self, g):
		# Draw All Spirte list
		# g.all_sprites.draw(g.window)
		g.sprites_level_backgrounds.draw(g.window)
		g.sprites_players.draw(g.window)
		g.sprites_enemies.draw(g.window)
		g.sprites_enemies_shoots.draw(g.window)
		g.sprites_allies_shoots.draw(g.window)
		g.sprites_items.draw(g.window)
		# g.sprites_level_text.draw(g.window)

		# print(g.sprites_explosions)
		g.sprites_explosions.draw(g.window)

		# g.sprites_hitbox.draw(g.window)
		# g.sprites_neutrals.draw(g.window)

			# Refresh ALL the Display
				# update() is faster than flip()
			# pygame.display.update(g.all_sprites_list)

		g.level_text.draw_text(g.window)
		pygame.display.flip()

	def draw_level_menu_sprites(self, g):

		g.sprites_level_backgrounds.draw(g.window)
		g.sprites_players.draw(g.window)
		g.sprites_enemies.draw(g.window)
		g.sprites_items.draw(g.window)

		# g.sprites_level_text.draw(g.window)

		g.sprites_level_menu_backgrounds.draw(g.window)
		# g.sprites_level_menu_text.draw(g.window)

		g.level_menu.text.draw_text(g.window)
		pygame.display.flip()


	def draw_opt_level_menu_sprites(self, g):

		if (g.previous_mode == F_MAIN_MENU) :
			g.sprites_main_menu_backgrounds.draw(g.window)
		else :
			g.sprites_level_backgrounds.draw(g.window)
			g.sprites_level_menu_backgrounds.draw(g.window)
			if (g.previous_mode != F_GAMEOVER_MENU):
				g.sprites_players.draw(g.window)
				g.sprites_enemies.draw(g.window)
				g.sprites_items.draw(g.window)

		g.opt_level_menu.text.draw_text(g.window)
		pygame.display.flip()


	def draw_death_menu_sprites(self, g):

		g.sprites_level_backgrounds.draw(g.window)
		g.sprites_players.draw(g.window)
		g.sprites_enemies.draw(g.window)

		g.sprites_level_menu_backgrounds.draw(g.window)
		# g.sprites_level_menu_text.draw(g.window)

		g.death_menu.text.draw_text(g.window)
		pygame.display.flip()

	def draw_gameover_menu_sprites(self, g):

		g.sprites_level_backgrounds.draw(g.window)

		g.sprites_level_menu_backgrounds.draw(g.window)

		g.gameover_menu.text.draw_text(g.window)
		pygame.display.flip()

	def draw_main_menu_sprites(self, g):


		g.sprites_main_menu_backgrounds.draw(g.window)
		# g.sprites_main_menu_text.draw(g.window)

		g.main_menu.text.draw_text(g.window)

		pygame.display.flip()
