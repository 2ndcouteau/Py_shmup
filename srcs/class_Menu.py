#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame

# from class_Event	import Event
from constants		import (X_WINDOW,
							Y_WINDOW)




class Menu():
	def __init__(self, g):
		self.toto = 0

	# def main_menu(self, g):
	# def level_menu(self, g): # run
	# 	Event.manage(Event, g)
	# 	g.text_main_menu.update()
	# 	Layout.draw_main_menu_sprites(Layout, g)
	#
	# 	Event.manage(Event, g)
	# 	g.text_level_menu.update()
	# 	Layout.draw_level_menu_sprites(Layout, g)


class Main_menu():
	def __init__(self, g):
		Menu.__init__(self)

		self.main_function = []
		self.main_function.insert(PLAY, play_game)
		self.main_function.insert(OPTIONS_MAIN, options_main)
		self.main_function.insert(QUIT, quit)

	def play_game(self, g):
		g.restart_game() ## Init_game() with some differente base value
		g.mode = F_GAME
		# g.main_menu_music.pause()
		music.load(os.path.join(media_folder, 'game_music.wav'))
		music.play(-1)
		# g.music_level.play(-1)
		print("Play Game")

	def options_main(self, g):
		print("Main options")

	def quit(self, g):
		exit()




#
# class Level_menu(Menu):
# 	def __init__(self, g):
# 		Menu.__init__(self)
#
