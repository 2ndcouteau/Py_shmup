#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import os
import pygame

# from class_Event	import Event
from pygame.mixer	import music

# from class_Layout	import Layout
from class_Text		import Text_main_menu, Text_level_menu, Text_game_level, Text_death_menu
from constants		import (X_WINDOW, Y_WINDOW,
							F_GAME, F_MAIN_MENU, F_LEVEL_MENU,
							PLAY, OPTIONS_MAIN, QUIT,
							RESUME, RESTART, OPTIONS_LEVEL, MAIN_MENU,
							CONTINUE, RESTART_DEATH, OPTIONS_DEATH, MAIN_MENU_DEATH,
							media_folder)




class Menu():
	def __init__(self, g):
		self.toto = 0


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
			# g.main_menu_music.pause()
			music.load(os.path.join(media_folder, 'game_music.wav'))
			music.play(-1)
			# g.music_level.play(-1)
			print("Play Game")

		def options_main(g):
			print("Main options")

		def quit(g):
			exit()

		self.function = []
		self.function.insert(PLAY, play_game)
		self.function.insert(OPTIONS_MAIN, options_main)
		self.function.insert(QUIT, quit)

	# def run(g): #run
	# 	Event.manage(Event, g)
	# 	g.text_main_menu.update()
	# 	Layout.draw_main_menu_sprites(Layout, g)




class Level_menu(Menu):
	def __init__(self, g):
		Menu.__init__(self, g)
		self.text = Text_level_menu()

		def resume_level(g):
			g.mode = F_GAME
			music.unpause()

		def restart_level(g):
			g.restart_level()
			g.mode = F_GAME
			music.rewind()
			music.play(-1)

		def options_level(g):
			print("Level options")

		def main_menu(g):
			g.mode = F_MAIN_MENU
			music.load(os.path.join(media_folder, 'main_menu_music.wav'))
			music.play(-1)

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
			g.player.lives -= 1
			g.player.continue_level(g)	# Remove in DEATH_MENU
			g.mode = F_GAME
			music.unpause()

		def restart_level(g):
			g.restart_level()
			g.mode = F_GAME
			music.rewind()
			music.play(-1)


		def options(g):
			print("Main options")


		def main_menu(g):
			g.mode = F_MAIN_MENU
			music.load(os.path.join(media_folder, 'main_menu_music.wav'))
			music.play(-1)

		self.function = []
		self.function.insert(CONTINUE, continue_level)
		self.function.insert(RESTART_DEATH, restart_level)
		self.function.insert(OPTIONS_DEATH, options)
		self.function.insert(MAIN_MENU_DEATH, main_menu)


# class Game_over_menu(Menu):
# 	def __init__(self, g):
# 		Menu.__init__(self, g)
# 		self.text = Text_game_over_menu()
#
# 		def continue_level(g):
# 			g.player.lives -= 1
# 			g.player.continue_level(g)	# Remove in DEATH_MENU
# 			g.mode = F_GAME
# 			music.unpause()
#
# 		def restart_level(g):
# 			g.restart_level()
# 			g.mode = F_GAME
# 			music.rewind()
# 			music.play(-1)
#
#
# 		def options_main(g):
# 			print("Main options")
#
# 		def quit(g):
# 			exit()
#
# 		self.function = []
# 		self.function.insert(CONTINUE, continue_level)
# 		self.function.insert(RESTART_DEATH, restart_game)
# 		self.function.insert(OPTIONS_DEATH, options_death)
# 		self.function.insert(MAIN_MENU_DEATH, main_menu)
