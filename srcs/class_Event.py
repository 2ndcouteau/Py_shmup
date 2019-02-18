#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *
from random			import randint

from class_Player		import Player
from class_Enemy		import Enemy
from constants			import (GAME,
								LEVEL_MENU,
								MAIN_MENU,
								UP,
								DOWN,
								RIGHT,
								LEFT)

# func_table = {
# 		1: (truc, (1, 2, 3)),
# 		2: (bidule, (4, 1, 2, 5, 6)),
# 		3: (machin, (5, 8, 9))
# 	}


# [for x in t.values()]
# ['string value', [1, 2]]

# [for x in t.keys()]
# ['first', 'csecond']

# [for x in t.items()]
# [('a', 'string value'), ('b', [1, 2])]




class Event():
	def __init__(self):
		self.timer = 0 # 1seconde

	def game(self, g, keys):

	####
		game_event = {
			K_e: [self.k_e, g],
			K_BACKSPACE: [self.k_backspace, g],	# change to load_menu()
			K_RETURN: [print, "Entrée", "ENTER"],
			K_SPACE: [g.player.shoot, g],
			K_b: [print, "Bomb"],
			K_UP: [g.player.move, UP],
			K_DOWN: [g.player.move, DOWN],
			K_LEFT: [g.player.move, LEFT],
			K_RIGHT: [g.player.move, RIGHT],
			K_w: [g.player.move, UP],
			K_s: [g.player.move, DOWN],
			K_a: [g.player.move, LEFT],
			K_d: [g.player.move, RIGHT],
		}

		if g.player.hp <= 0:
			print("You Died")
			g.mode = LEVEL_MENU	# change to load_menu()
		for input, func in game_event.items():
			if keys[input]:
				func[0](*func[1:])

	def k_backspace(g):
		g.mode = LEVEL_MENU	# change to load_menu()
	def k_e(g):
		if self.timer <= 0:
			Enemy(g)
			# Reset the countdown timer to one second.
			self.timer = 1000

		#
		# if keys[K_BACKSPACE]:
		# 	g.mode = LEVEL_MENU	# change to load_menu()
		# if keys[K_RETURN]:
		# 	print("Entrée")
		# if keys[K_SPACE]:
		# 	g.player.shoot(g)
		# 	print("Espace")
		# if keys[K_b]:
		# 	print("Bomb")
		# if keys[K_UP] or keys[K_w]:
		# 	g.player.move(UP)
		# if keys[K_DOWN] or keys[K_s]:
		# 	g.player.move(DOWN)
		# if keys[K_LEFT] or keys[K_a]:
		# 	g.player.move(LEFT)
		# if keys[K_RIGHT] or keys[K_d]:
		# 	g.player.move(RIGHT)
		# if keys[K_e]:
		# 	if g.timer <= 0:
		# 		Enemy(g)
		# 		# Reset the countdown timer to one second.
		# 		g.timer = 1000

		# def k_return(g):
		# 	print("Entrée")
		# def k_space(g):
		# 	g.player.shoot(g)
		# 	print("Espace")
		# def k_b():
		# 	print("Bomb")
		# def k_up(g):
		# 	g.player.move(UP)
		# def k_down(g):
		# 	g.player.move(DOWN)
		# def k_left(g):
		# 	g.player.move(LEFT)
		# def k_right(g):
		# 	g.player.move(RIGHT)
		# def k_w(g):
		# 	g.player.move(UP)
		# def k_s(g):
		# 	g.player.move(DOWN)
		# def k_a(g):
		# 	g.player.move(LEFT)
		# def k_d(g):
		# 	g.player.move(RIGHT)


	def general(g, keys):
		if keys[K_ESCAPE]:
			exit()
		# if keys[K_S]:
		# 	cut_the_sound

	def main_menu(g, keys):
		if keys[K_RETURN]:
			g.restart_game() ## Init_game() with some differente base value
			g.mode = GAME
			print("Entrée")

	def level_menu(g, keys):
		if (g.player.hp > 0):
			if keys[K_RETURN] or keys[K_SPACE]:
				g.mode = GAME
		if keys[K_r]:
			g.restart_game()
			g.mode = GAME
		if keys[K_q]:
			g.mode = MAIN_MENU


	def manage(self, g):
		# g.timer_event -= g.dt
		# if g.timer_event <= 0:

		pygame.event.pump() ## Good way to manage event
		keys = pygame.key.get_pressed()
		# if event.type == pygame.KEYDOWN:
		# print ("Button pressed !")
		self.general(g, keys)
		if (g.mode is GAME):
			self.game(self, g, keys)
		elif (g.mode is LEVEL_MENU):
			self.level_menu(g, keys)
		else:
			self.main_menu(g, keys)

		pygame.event.clear()
		g.player.rect = g.player.rect.clamp(g.window_rect)
			# g.timer_event = EVENT_FREQUENCY
