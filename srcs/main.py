#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import os

import pygame
# from pygame.locals	import *

from datetime import datetime
import time
from class_Game		import Game
from class_Event	import Event
from class_Layout	import Layout
from class_Menu		import Menu #, Level_menu

from constants		import F_GAME, F_LEVEL_MENU, F_MAIN_MENU, F_DEATH_MENU, F_GAMEOVER_MENU, F_OPTIONS_LEVEL

def main_loop(g):
	clock = pygame.time.Clock()
	while 42:
		# dt = time in milliseconds that passed since last tick.
		g.dt = clock.tick(60)
		g.timer -= g.dt

		if (g.mode is F_GAME):
			# g.window.fill((0,0,0))
			g.generate_enemies()
			Event.manage(Event, g)
			Layout.scroll_level_background(g)

			print("nb_shoot == " + str(len(g.sprites_allies_shoots)))
			g.sprites_allies_shoots.update()
			g.sprites_enemies_shoots.update()
			g.sprites_enemies.update()
			g.sprites_items.update()
			g.player.update()

			g.collide_management()

			g.sprites_explosions.update()
			# g.text_game_level.update()
			g.level_text.update()
			Layout.draw_level_sprites(Layout, g)

			## DEBUG
			print("nb all sprites == {0}".format(str(len(g.all_sprites))))
			print("FPS : {0}".format(str(clock.get_fps())))

		elif (g.mode is F_DEATH_MENU):
			Layout.draw_death_menu_sprites(Layout, g)
			Event.manage(Event, g)
			g.death_menu.text.update()

		elif (g.mode is F_GAMEOVER_MENU):
			Layout.draw_gameover_menu_sprites(Layout, g)
			Event.manage(Event, g)
			g.gameover_menu.text.update()

		elif (g.mode is F_LEVEL_MENU):
			Layout.draw_level_menu_sprites(Layout, g)
			Event.manage(Event, g)
			g.level_menu.text.update()

		elif (g.mode is F_MAIN_MENU):
			Layout.draw_main_menu_sprites(Layout, g)
			Event.manage(Event, g)
			g.main_menu.text.update()

		elif (g.mode is F_OPTIONS_LEVEL):
			Layout.draw_opt_level_menu_sprites(Layout, g)
			Event.manage(Event, g)
			g.opt_level_menu.text.update()




def main():

	g = Game()
	main_loop(g)


if __name__ == '__main__':
	print ("Welcome in PyShmup !")
	main()
