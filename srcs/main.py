#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import os

import pygame
# from pygame.locals	import *

from class_Game		import Game
from class_Event	import Event
from class_Layout	import Layout
from constants		import (GAME,
							LEVEL_MENU,
							MAIN_MENU)

def main_loop(g):
	clock = pygame.time.Clock()

	while 42:
		# dt = time in milliseconds that passed since last tick.
		g.dt = clock.tick(60)
		g.timer -= g.dt

		if (g.mode is GAME):
			# g.window.fill((0,0,0))
			g.generate_enemies()
			Event.manage(Event, g)
			Layout.scroll_level_background(g)

			print("nb_shoot == " + str(len(g.sprites_allies_shoots)))
			g.sprites_allies_shoots.update()
			g.sprites_enemies_shoots.update()
			g.sprites_enemies.update()

			g.collide_management()

			g.sprites_explosions.update()
			Layout.draw_game_sprites(Layout, g)

		elif (g.mode is LEVEL_MENU):

			Layout.draw_level_menu_sprites(Layout, g)
			Event.manage(Event, g)

		else :
			Event.manage(Event, g)
			g.text_main_menu.update()

			Layout.draw_main_menu_sprites(Layout, g)


def main():

	g = Game()
	main_loop(g)


if __name__ == '__main__':
	print ("Welcome in PyShmup !")
	main()
