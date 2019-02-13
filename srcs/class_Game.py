#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *
from random			import randint


from class_Player		import Player
from class_Enemy		import Enemy
from class_Background	import Background
from constants			import (X_WINDOW,
								Y_WINDOW,
								ENEMIES_SPAWN_FREQUENCY,
								GAME,
								IMG_PLAYER)

class Game():
	def __init__(self):
		self.timer = 0 # 1seconde
		self.dt = 0

		pygame.init()
		# Set input frequency
		pygame.key.set_repeat(1, 1)

		# This is a list of every sprite.
		self.all_sprites_list = pygame.sprite.Group()
		self.sprites_backgrounds_list = pygame.sprite.Group()
		self.sprites_players_list = pygame.sprite.Group()
		self.sprites_enemies_list = pygame.sprite.Group()
		self.sprites_allies_shoots_list = pygame.sprite.Group()
		self.sprites_enemies_shoots_list = pygame.sprite.Group()
#		self.sprites_shoots_list = pygame.sprite.Group()
#		self.sprites_neutrals_list = pygame.sprite.Group()

		self.window = pygame.display.set_mode((X_WINDOW, Y_WINDOW), HWSURFACE | DOUBLEBUF | RESIZABLE)
		self.window_rect = self.window.get_rect()
		self.icone = IMG_PLAYER.convert_alpha()
		self.title = pygame.display.set_caption("BEST GAME EVER -- Py_SHMUP")

		self.mode = GAME

		# Set 2 backgrounds for infinite loop display
		self.backgrounds = []
		self.backgrounds.append(Background(self, 0))
		self.backgrounds.append(Background(self, -Y_WINDOW))

		self.player = Player(self)

		# self.ennemies = []
		# self.shoots = []
		# self.neutrals = []

	def generate_enemies(self):
		if self.timer <= 0:
			for i in range(1, 3):
				Enemy(self)
			# Reset the countdown timer to one second.
			self.timer = ENEMIES_SPAWN_FREQUENCY + randint(0, 1000)

	def collide_management(self):
		# See if the enemies collide with player
		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies_list, True)
		# Check the list of collisions.
		for x in collide_list:
			self.player.hp -= 1
			print("Collide Player with Enemies !")

		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies_shoots_list, True)
		for x in collide_list:
			self.player.hp -= 1
			print("Collide Enemies shoots with player !")

		collide_list = pygame.sprite.groupcollide(self.sprites_allies_shoots_list, self.sprites_enemies_list, True, True)
		# Check the list of collisions.
		for x in collide_list:
			print("Collide Player Shoots with Enemies !")

	def backgrounds_reinitialization(self):
		self.all_sprites_list.add(self.backgrounds[0])
		self.all_sprites_list.add(self.backgrounds[1])
		self.backgrounds[0].rect.y = 0
		self.backgrounds[1].rect.y = -Y_WINDOW

	def restart_game(self):
		# Clear all Useless sprites lists
		self.all_sprites_list.empty()
		self.sprites_enemies_list.empty()
		self.sprites_enemies_shoots_list.empty()
		self.sprites_allies_shoots_list.empty()

		self.player.reinitialization(self)
		self.backgrounds_reinitialization()
