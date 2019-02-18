#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *
from random			import randint


from class_Player		import Player
from class_Enemy		import Enemy
from class_Background	import Level_background, Level_menu_background, Main_menu_background
from class_Text			import Level_text, Level_menu_text, Main_menu_text

from constants			import (X_WINDOW,
								Y_WINDOW,
								ENEMIES_SPAWN_FREQUENCY,
								NEUTRALS_SPAWN_FREQUENCY,
								GAME,
								MAIN_MENU,
								LEVEL_MENU,
								IMG_LEVEL1_BACKGROUND,
								IMG_MAIN_MENU_BACKGROUND,
								IMG_LEVEL_MENU_BACKGROUND_FULL,
								IMG_LEVEL_MENU_BACKGROUND_TIER,
								IMG_PLAYER)

class Game():
	def __init__(self):
		self.timer = 0 # 1seconde
		self.dt = 0

		pygame.init()
		# Set input frequency
		pygame.key.set_repeat(1, 1)

		# This is a list of every sprite.
		self.all_sprites = pygame.sprite.Group()

		self.sprites_level_backgrounds = pygame.sprite.Group()
		self.sprites_level_menu_backgrounds = pygame.sprite.Group()
		self.sprites_main_menu_backgrounds = pygame.sprite.Group()

		self.sprites_level_text = pygame.sprite.Group()
		self.sprites_level_menu_text = pygame.sprite.Group()
		self.sprites_main_menu_text = pygame.sprite.Group()

		self.sprites_players = pygame.sprite.Group()
		self.sprites_enemies = pygame.sprite.Group()

		self.sprites_allies_shoots = pygame.sprite.Group()
		self.sprites_enemies_shoots = pygame.sprite.Group()
#		self.sprites_neutrals_list = pygame.sprite.Group()



		self.window = pygame.display.set_mode((X_WINDOW, Y_WINDOW), HWSURFACE | DOUBLEBUF) # | RESIZABLE)
		self.window_rect = self.window.get_rect()
		self.icone = IMG_PLAYER.convert_alpha()
		self.title = pygame.display.set_caption("BEST GAME EVER -- Py_SHMUP")

		self.mode = MAIN_MENU

		# Init all backgrounds:
		self.level_backgrounds = []
		self.level_backgrounds.append(Level_background(self, (0, 0), IMG_LEVEL1_BACKGROUND, GAME))
		self.level_backgrounds.append(Level_background(self, (0, -Y_WINDOW), IMG_LEVEL1_BACKGROUND, GAME))

		self.main_menu_backgrounds = []
		self.main_menu_backgrounds.append(Main_menu_background(self, (0, 0), IMG_MAIN_MENU_BACKGROUND, MAIN_MENU))

		self.level_menu_backgrounds = []
		self.level_menu_backgrounds.append(Level_menu_background(self, (0, 0), IMG_LEVEL_MENU_BACKGROUND_FULL, LEVEL_MENU, opacity=100))
		self.level_menu_backgrounds.append(Level_menu_background(self, (X_WINDOW / 4, Y_WINDOW / 4), IMG_LEVEL_MENU_BACKGROUND_TIER, LEVEL_MENU, opacity=150))


		self.player = Player(self)

		Level_text(self, "Hello  Game  !!", (0, 0))
		Level_menu_text(self, "** Main menu **", (self.level_menu_backgrounds[1].rect.x, 0), cx=True)
		Main_menu_text(self, "* Menu *", (X_WINDOW / 2, Y_WINDOW /2), cx=True)

		# self.neutrals = []

	# def generate_neutrals(self):
		# if self.timer <= 0:
		# 	for i in range(1, 3):
		# 		Neutrals(self)
		# 	# Reset the countdown timer to one second.
		# 	self.timer = NEUTRALS_SPAWN_FREQUENCY + randint(0, 1000)


	def generate_enemies(self):
		if self.timer <= 0:
			for i in range(1, 3):
				Enemy(self)
			# Reset the countdown timer to one second.
			self.timer = ENEMIES_SPAWN_FREQUENCY + randint(0, 1000)

	def collide_management(self):
		# See if the enemies collide with player
		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies, True)
		# Check the list of collisions.
		for x in collide_list:
			self.player.hp -= 1
			print("Collide Player with Enemies !")

		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies_shoots, True)
		for x in collide_list:
			self.player.hp -= 1
			print("Collide Enemies shoots with player !")

		collide_list = pygame.sprite.groupcollide(self.sprites_allies_shoots, self.sprites_enemies, True, True)
		# Check the list of collisions.
		for x in collide_list:
			print("Collide Player Shoots with Enemies !")

	def level_backgrounds_reinitialization(self):
		self.all_sprites.add(self.level_backgrounds[0])
		self.all_sprites.add(self.level_backgrounds[1])
		self.level_backgrounds[0].rect.y = 0
		self.level_backgrounds[1].rect.y = -Y_WINDOW

	def restart_game(self):
		# Clear all Useless sprites lists
		self.all_sprites.empty()
		self.sprites_enemies.empty()
		self.sprites_enemies_shoots.empty()
		self.sprites_allies_shoots.empty()

		self.player.reinitialization(self)
		self.level_backgrounds_reinitialization()
