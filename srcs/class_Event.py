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

class Event():
	def __init__(self):
		self.timer = 0 # 1seconde
		self.dt = 0

	def game(g, keys):

		if g.player.hp <= 0:
			print("You Died")
			g.mode = LEVEL_MENU	# change to load_menu()
		if keys[K_BACKSPACE]:
			g.mode = LEVEL_MENU	# change to load_menu()
		if keys[K_RETURN]:
			print("Entrée")
		if keys[K_SPACE]:
			g.player.shoot(g)
			print("Espace")
		if keys[K_b]:
			print("Bomb")
		if keys[K_UP] or keys[K_w]:
			g.player.move(UP)
		if keys[K_DOWN] or keys[K_s]:
			g.player.move(DOWN)
		if keys[K_LEFT] or keys[K_a]:
			g.player.move(LEFT)
		if keys[K_RIGHT] or keys[K_d]:
			g.player.move(RIGHT)
		if keys[K_e]:
			if g.timer <= 0:
				Enemy(g)
				# Reset the countdown timer to one second.
				g.timer = 1000

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
		pygame.event.pump() ## Good way to manage event
		keys = pygame.key.get_pressed()
		# if event.type == pygame.KEYDOWN:
		# print ("Button pressed !")
		self.general(g, keys)
		if (g.mode is GAME):
			self.game(g, keys)
		elif (g.mode is LEVEL_MENU):
			self.level_menu(g, keys)
		else:
			self.main_menu(g, keys)

		pygame.event.clear()
		g.player.rect = g.player.rect.clamp(g.window_rect)
