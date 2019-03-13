# _*_ coding: Utf-8 -*

#!/usr/bin/env python3.7
import os
import pygame
from pygame.locals	import *
from pygame.mixer	import music
from random			import randint

from class_Player		import Player
from class_Enemy		import Enemy
from class_Menu			import Main_menu

from constants			import (F_GAME, F_LEVEL_MENU, F_MAIN_MENU, F_DEATH_MENU, F_GAMEOVER_MENU, F_OPTIONS_LEVEL,
								UP, DOWN, RIGHT, LEFT,
								MENU_INPUT_DELAY,
								OPT_SFX, OPT_MUSIC,
								media_folder)

class Event():
	def __init__(self):
		self.timer = 0 # 1seconde

	def game(self, g, keys):

	####
		game_event = {
			K_e: [self.k_e, g],
			K_BACKSPACE: [self.k_backspace, g],	# change to load_menu()
			K_RETURN: [print, "Entrée", "ENTER"],
			K_SPACE: [self.shoot, g],
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
			if (g.opt_music == True):
				music.pause()
			if g.player.lives == 0:
				print("GAME_OVER")

				g.mode = F_GAMEOVER_MENU
			else:
				print("You Died")
				g.mode = F_DEATH_MENU

		for input, func in game_event.items():
			if keys[input]:
				func[0](*func[1:])

	def	shoot(g):
		if (g.opt_autoshoot == False):
			g.player.shoot(g)

	def k_backspace(g):
		g.mode = F_LEVEL_MENU	# change to load_menu()
		if (g.opt_music == True):
			music.pause()
	def k_e(g):
		if g.timer <= 0:
			Enemy(g)
			# Reset the countdown timer to one second.
			g.timer = 50

		#
		# if keys[K_BACKSPACE]:
		# 	g.mode = F_LEVEL_MENU	# change to load_menu()
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

		if (g.mode == F_GAME):
			g.menu_timer -= g.dt
		if (g.menu_timer <= 0):
			if keys[K_m]:
				if (g.opt_music == False):
					g.opt_music = True
					if (g.opt_sfx is True):
						g.sound_on.play()
					if ((g.mode != F_GAME and g.previous_mode == F_MAIN_MENU) or g.mode == F_GAME):
						# music.play(-1)
						music.rewind()
						music.unpause()
				else :
					if (g.opt_sfx is True):
						g.sound_off.play()
					g.opt_music = False
					music.pause()
				g.menu_timer = MENU_INPUT_DELAY

	def main_menu(g, keys):

		g.menu_timer -= g.dt
		if (g.menu_timer <= 0):
			if keys[K_RETURN]:
				g.main_menu.function[g.main_menu.text.new_pos - g.main_menu.text.offset_title_select](g)
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_UP]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.main_menu.text.move_up()
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_DOWN]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.main_menu.text.move_down()
				g.menu_timer = MENU_INPUT_DELAY


	def death_menu(g, keys):
		g.menu_timer -= g.dt
		if g.menu_timer <= 0:
			if keys[K_RETURN]:
				g.death_menu.function[g.death_menu.text.new_pos - g.death_menu.text.offset_title_select](g)
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_UP]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.death_menu.text.move_up()
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_DOWN]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.death_menu.text.move_down()
				g.menu_timer = MENU_INPUT_DELAY


	def gameover_menu(g, keys):
		g.menu_timer -= g.dt
		if g.menu_timer <= 0:
			if keys[K_RETURN]:
				g.gameover_menu.function[g.gameover_menu.text.new_pos - g.gameover_menu.text.offset_title_select](g)
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_UP]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.gameover_menu.text.move_up()
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_DOWN]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.gameover_menu.text.move_down()
				g.menu_timer = MENU_INPUT_DELAY


	def level_menu(g, keys):

		if keys[K_r]:
			g.restart_game()
			g.mode = F_GAME
			if (g.opt_music == True):
				music.rewind()
				music.play(-1)
		if keys[K_q]:
			g.mode = F_MAIN_MENU
			if (g.opt_music == True):
				music.load(os.path.join(media_folder, 'main_menu_music.wav'))
				music.play(-1)

		g.menu_timer -= g.dt
		if g.menu_timer <= 0:
			if keys[K_RETURN]:
				g.level_menu.function[g.level_menu.text.new_pos - g.level_menu.text.offset_title_select](g)
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_UP]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.level_menu.text.move_up()
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_DOWN]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.level_menu.text.move_down()
				g.menu_timer = MENU_INPUT_DELAY


	def opt_level_menu(g, keys):

		g.menu_timer -= g.dt
		if g.menu_timer <= 0:

			if keys[K_BACKSPACE]:
				if (g.opt_sfx is True):
					g.sound_return.play()
				g.mode = g.previous_mode
				g.previous_mode = F_OPTIONS_LEVEL
				g.menu_timer = MENU_INPUT_DELAY

			if keys[K_LEFT] or keys[K_RIGHT]:

				if g.opt_level_menu.text.new_pos == OPT_SFX or g.opt_level_menu.text.new_pos == OPT_MUSIC :

					g.opt_level_menu.function[g.opt_level_menu.text.new_pos - g.opt_level_menu.text.offset_title_select](g)
					g.menu_timer = MENU_INPUT_DELAY

			if keys[K_RETURN] or keys[K_SPACE]:
				g.opt_level_menu.function[g.opt_level_menu.text.new_pos - g.opt_level_menu.text.offset_title_select](g)
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_UP]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.opt_level_menu.text.move_up()
				g.menu_timer = MENU_INPUT_DELAY
			if keys[K_DOWN]:
				if (g.opt_sfx is True):
					g.sound_move_cursor.play()
				g.opt_level_menu.text.move_down()
				g.menu_timer = MENU_INPUT_DELAY


	def manage(self, g):
		# g.timer_event -= g.dt
		# if g.timer_event <= 0:

		pygame.event.pump() ## Good way to manage event
		keys = pygame.key.get_pressed()
		# if event.type == pygame.KEYDOWN:
		# print ("Button pressed !")
		self.general(g, keys)
		if (g.mode is F_GAME):
			self.game(self, g, keys)
		elif (g.mode is F_GAMEOVER_MENU):
			self.gameover_menu(g, keys)
		elif (g.mode is F_DEATH_MENU):
			self.death_menu(g, keys)
		elif (g.mode is F_LEVEL_MENU):
			self.level_menu(g, keys)
		elif (g.mode is F_OPTIONS_LEVEL):
			self.opt_level_menu(g, keys)
		elif (g.mode is F_MAIN_MENU):
			self.main_menu(g, keys)
		else :
			print ("error input Event")

		pygame.event.clear()
		g.player.rect = g.player.rect.clamp(g.window_rect)
			# g.timer_event = EVENT_FREQUENCY
