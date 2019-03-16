#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import os
import sys
import pygame

# from class_Event	import Event
from pygame.mixer	import music

# from class_Layout	import Layout
from class_Text		import Text_main_menu, Text_level_menu, Text_death_menu, Text_gameover_menu, Text_opt_level_menu
from constants		import (X_WINDOW, Y_WINDOW,
							F_GAME, F_LEVEL_MENU, F_MAIN_MENU, F_DEATH_MENU, F_GAMEOVER_MENU, F_OPTIONS_LEVEL,
							PLAY, OPTIONS_MAIN, QUIT,
							RESUME, RESTART, OPTIONS_LEVEL, MAIN_MENU,
							CONTINUE, RESTART_DEATH, OPTIONS_DEATH, MAIN_MENU_DEATH,
							OPTIONS_GAMEOVER, MAIN_MENU_GAMEOVER,
							OPT_MUSIC, OPT_SFX, OPT_AUTOSHOOT, OPT_RETURN_MENU,
							sounds_folder)




class Menu():
	def __init__(self, g):
		self.g = g

	def load_music(self, g, music_name):
		music.load(os.path.join(sounds_folder, music_name))
		music.play(-1)
		if (g.opt_music == False):
			music.pause()


	# def level_menu(self, g): # run
	# 	Event.manage(Event, g)
	# 	g.text_level_menu.update()
	# 	Layout.draw_level_menu_sprites(Layout, g)




class Main_menu(Menu):
	def __init__(self, g):
		Menu.__init__(self, g)
		self.text = Text_main_menu()

		def play_game(g):
			g.restart_game() ## Init_game() with some differente base value
			g.mode = F_GAME
			if (g.opt_sfx is True):
				g.sound_launch_game.play()
			self.load_music(g, 'game_music.wav')

		def options_main(g):
			if (g.opt_sfx is True):
				g.sound_select.play()
			g.previous_mode = F_MAIN_MENU
			g.mode = F_OPTIONS_LEVEL

		def quit(g):
			sys.exit(0)

		self.function = []
		self.function.insert(PLAY, play_game)
		self.function.insert(OPTIONS_MAIN, options_main)
		self.function.insert(QUIT, quit)

	# def run(g): #run
	# 	Event.manage(Event, g)
	# 	g.text_main_menu.update()
	# 	Layout.draw_main_menu_sprites(Layout, g)


class Opt_level_menu(Menu):
	def __init__(self, g):
		Menu.__init__(self, g)
		self.text = Text_opt_level_menu(g)

		def switch_sound(g):
			if (g.opt_music == False):
				g.opt_music = True
				if (g.opt_sfx is True):
					g.sound_on.play()
				if (g.previous_mode == F_MAIN_MENU):
					# music.play(-1)
					music.rewind()
					music.unpause()
				# else :
			else :
				if (g.opt_sfx is True):
					g.sound_off.play()
				g.opt_music = False
				music.pause()

		def switch_sfx(g):
			if (g.opt_sfx == False):
				g.sound_on.play()
				g.opt_sfx = True
			else :
				g.sound_off.play()
				g.opt_sfx = False

		def switch_autoshoot(g):
			if (g.opt_autoshoot == False):
				if (g.opt_sfx is True):
					g.sound_on.play()
				g.opt_autoshoot = True
			else :
				if (g.opt_sfx is True):
					g.sound_off.play()
				g.opt_autoshoot = False

		def return_level_menu(g):
			g.mode = g.previous_mode
			if (g.opt_sfx is True):
				g.sound_return.play()
			g.previous_mode = F_OPTIONS_LEVEL


		self.function = []
		self.function.insert(OPT_MUSIC, switch_sound)
		self.function.insert(OPT_SFX, switch_sfx)
		self.function.insert(OPT_AUTOSHOOT, switch_autoshoot)
		self.function.insert(OPT_RETURN_MENU, return_level_menu)



class Level_menu(Menu):
	def __init__(self, g):
		Menu.__init__(self, g)
		self.text = Text_level_menu()

		def resume_level(g):
			g.mode = F_GAME
			if (g.opt_sfx is True):
				g.sound_select.play()
			if (g.opt_music == True):
				music.unpause()

		def restart_level(g):
			g.restart_level()
			g.mode = F_GAME
			if (g.opt_sfx is True):
				g.sound_select.play()
			music.rewind()
			if (g.opt_music == True):
				music.play(-1)

		def options_level(g):
			g.previous_mode = F_LEVEL_MENU
			g.mode = F_OPTIONS_LEVEL
			if (g.opt_sfx is True):
				g.sound_select.play()


		def main_menu(g):
			g.mode = F_MAIN_MENU
			if (g.opt_sfx is True):
				g.sound_return.play()
			self.load_music(g, 'main_menu_music.wav')

		self.function = []
		self.function.insert(RESUME, resume_level)
		self.function.insert(RESTART, restart_level)
		self.function.insert(OPTIONS_LEVEL, options_level)
		self.function.insert(MAIN_MENU, main_menu)

class Death_menu(Menu):
	def __init__(self, g):
		Menu.__init__(self, g)
		self.text = Text_death_menu(g)

		def continue_level(g):
			g.continue_level()
			g.player.lives -= 1
			g.mode = F_GAME
			if (g.opt_sfx is True):
				g.sound_select.play()
			if (g.opt_music == True):
				music.unpause()

		def restart_level(g):
			g.restart_level()
			g.mode = F_GAME
			music.rewind()
			if (g.opt_sfx is True):
				g.sound_select.play()
			if (g.opt_music == True):
				music.play(-1)


		def options(g):
			g.previous_mode = F_DEATH_MENU
			g.mode = F_OPTIONS_LEVEL
			if (g.opt_sfx is True):
				g.sound_select.play()

		def main_menu(g):
			g.previous_mode = F_DEATH_MENU
			g.mode = F_MAIN_MENU
			if (g.opt_sfx is True):
				g.sound_return.play()
			self.load_music(g, 'main_menu_music.wav')

		self.function = []
		self.function.insert(CONTINUE, continue_level)
		self.function.insert(RESTART_DEATH, restart_level)
		self.function.insert(OPTIONS_DEATH, options)
		self.function.insert(MAIN_MENU_DEATH, main_menu)


class Gameover_menu(Menu):
	def __init__(self, g):
		Menu.__init__(self, g)
		self.text = Text_gameover_menu(g)

		# def continue_level(g):
		# 	g.player.lives -= 1
		# 	g.player.continue_level(g)	# Remove in DEATH_MENU
		# 	g.mode = F_GAME
		# 	music.unpause()

		# def restart_level(g):
		# 	g.restart_level()
		# 	g.mode = F_GAME
		# 	music.rewind()
		# 	music.play(-1)


		def options_gameover(g):
			g.previous_mode = F_GAMEOVER_MENU
			g.mode = F_OPTIONS_LEVEL

		def main_menu(g):
			g.previous_mode = F_GAMEOVER_MENU
			g.mode = F_MAIN_MENU
			if (g.opt_sfx is True):
				g.sound_return.play()
			self.load_music(g, 'main_menu_music.wav')
			g.player.init_game(g)

		self.function = []
		# self.function.insert(CONTINUE, continue_level)
		# self.function.insert(RESTART_DEATH, restart_game)
		self.function.insert(OPTIONS_GAMEOVER, options_gameover)
		self.function.insert(MAIN_MENU_GAMEOVER, main_menu)
