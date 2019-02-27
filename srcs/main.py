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

from constants		import (F_GAME, F_LEVEL_MENU, F_MAIN_MENU)

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
			g.player.update()

			g.collide_management()

			g.sprites_explosions.update()
			g.text_game_level.update()
			Layout.draw_game_sprites(Layout, g)


		elif (g.mode is F_LEVEL_MENU):
			# Menu.level_menu(Menu, g)
			Event.manage(Event, g)
			g.level_menu.text.update()
			Layout.draw_level_menu_sprites(Layout, g)
		elif (g.mode is F_MAIN_MENU):
			# Menu.main_menu(Menu, g)
			Event.manage(Event, g)
			g.main_menu.text.update()
			Layout.draw_main_menu_sprites(Layout, g)




def main():

	g = Game()
	main_loop(g)


if __name__ == '__main__':
	print ("Welcome in PyShmup !")
	main()
