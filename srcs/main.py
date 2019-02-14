#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import os

import pygame
# from pygame.locals	import *

from class_Game		import Game
from class_Event	import Event
from class_Layout	import Layout
from constants		import (GAME,
							MENU)

def game_loop(g):
	while 42:
		# dt = time in milliseconds that passed since last tick.
		g.dt = pygame.time.Clock().tick(60)
		g.timer -= g.dt

		if (g.mode is GAME):
			# g.window.fill((0,0,0))
			g.generate_enemies()
			Event.manage(Event, g)
			Layout.scroll_background(g)

			g.sprites_enemies_list.update()
			g.sprites_enemies_shoots_list.update()
			g.sprites_allies_shoots_list.update()

			g.collide_management()

			Layout.draw_sprites(Layout, g)

		else:
			Event.manage(Event, g)

def main():

	g = Game()
	game_loop(g)


if __name__ == '__main__':
	print ("Welcome in PyShmup !")
	main()
