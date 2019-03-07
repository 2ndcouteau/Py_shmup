#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
import os
from pygame.locals	import *
from pygame.mixer	import music
from random			import randint

from class_Explosion	import Explosion
from class_Player		import Player
from class_Enemy		import Enemy
from class_Background	import Level_background, Level_menu_background, Main_menu_background
from class_Text			import Text_main_menu, Text_level_menu, Text_level
from class_Menu			import Main_menu, Level_menu, Death_menu, Gameover_menu, Opt_level_menu

from constants			import (X_WINDOW, Y_WINDOW,
								ENEMIES_SPAWN_FREQUENCY, NEUTRALS_SPAWN_FREQUENCY,
								F_GAME, F_MAIN_MENU, F_LEVEL_MENU,
								IMG_LEVEL1_BACKGROUND, IMG_MAIN_MENU_BACKGROUND,
								IMG_LEVEL_MENU_BACKGROUND_FULL, IMG_LEVEL_MENU_BACKGROUND_TIER,
								IMG_PLAYER, IMG_EXPLOSION1, IMG_EXPLOSION2, IMG_EXPLOSION3,
								HIT_SHOT_ENNEMIES, HIT_SHIP_ENNEMIES, HIT_SHOT_PLAYER,
								media_folder)

class Game():
	def __init__(self):
		self.dt = 0
		self.timer = 0 # 1seconde
		self.timer_gen_e = 0
		self.timer_event = 0 # 1seconde
		self.menu_timer = 0

		self.last_update = 0

		pygame.init()
		pygame.mixer.set_num_channels(64)
		pygame.mixer.init()

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

		self.sprites_explosions = pygame.sprite.Group()


		self.sound_explosion = pygame.mixer.Sound(os.path.join(media_folder, 'explosion42.wav'))
		self.sound_shoot = pygame.mixer.Sound(os.path.join(media_folder, 'laser51.wav'))

		# self.music_channel_level = pygame.mixer.Channel(0)
		# self.music_channel_main_menu = pygame.mixer.Channel()
		self.opt_music = True
		self.opt_sfx = True

		music.load(os.path.join(media_folder, 'main_menu_music.wav'))
		music.set_volume(100)
		music.play(-1)


		# self.music_level = pygame.mixer.Sound(os.path.join(media_folder, 'game_music.wav'))
		# self.music_main_menu = pygame.mixer.music.load(os.path.join(media_folder, 'main_menu_music.wav'))

		# self.music_channel_level.load(self.music_level)
		# self.music_main_menu.play(-1)

		# self.sound_shoot = []
		# self.sound_shoot.append(pygame.mixer.Sound(os.path.join(media_folder, 'laser42.wav')))
		# self.sound_shoot.append(pygame.mixer.Sound(os.path.join(media_folder, 'laser43.wav')))
		# self.sound_shoot.append(pygame.mixer.Sound(os.path.join(media_folder, 'laser44.wav')))
		# self.sound_shoot.append(pygame.mixer.Sound(os.path.join(media_folder, 'laser45.wav')))
		# self.sound_shoot.append(pygame.mixer.Sound(os.path.join(media_folder, 'laser46.wav')))
		# self.sound_shoot.append(pygame.mixer.Sound(os.path.join(media_folder, 'laser47.wav')))



		self.window = pygame.display.set_mode((X_WINDOW, Y_WINDOW), HWSURFACE | DOUBLEBUF) # | RESIZABLE)
		self.window_rect = self.window.get_rect()
		self.icone = IMG_PLAYER.convert_alpha()
		self.title = pygame.display.set_caption("BEST GAME EVER -- Py_SHMUP")

		self.mode = F_MAIN_MENU

		# Init all backgrounds:
		self.level_backgrounds = []
		self.level_backgrounds.append(Level_background(self, (0, 0), IMG_LEVEL1_BACKGROUND, F_GAME))
		self.level_backgrounds.append(Level_background(self, (0, -Y_WINDOW), IMG_LEVEL1_BACKGROUND, F_GAME))

		self.main_menu_backgrounds = []
		self.main_menu_backgrounds.append(Main_menu_background(self, (0, 0), IMG_MAIN_MENU_BACKGROUND, F_MAIN_MENU))

		self.level_menu_backgrounds = []
		self.level_menu_backgrounds.append(Level_menu_background(self, (0, 0), IMG_LEVEL_MENU_BACKGROUND_FULL, F_LEVEL_MENU, opacity=100))
		self.level_menu_backgrounds.append(Level_menu_background(self, (X_WINDOW / 4, Y_WINDOW / 4), IMG_LEVEL_MENU_BACKGROUND_TIER, F_LEVEL_MENU, opacity=150))

		self.explosion_imgs = []
		self.explosion_imgs.append(self.load_sprites(IMG_EXPLOSION1, width=256, height=256, ratio=1/3))
		self.explosion_imgs.append(self.load_sprites(IMG_EXPLOSION2, width=256, height=256, ratio=1/2))
		self.explosion_imgs.append(self.load_sprites(IMG_EXPLOSION3, width=256, height=256, ratio=1/2))



		self.player = Player(self)

		# Level_text(self, "Hello  Game  !!", (0, 0))
		# Level_menu_text(self, "** Main menu **", (self.level_menu_backgrounds[1].rect.x, 0), cx=True)
		# self.text_main_menu = Text_main_menu()
		# self.text_level_menu = Text_level_menu()
		# self.text_game_level = Text_game_level(self)

		self.level_text = Text_level(self)
		self.level_menu = Level_menu(self)
		self.main_menu = Main_menu(self)
		self.death_menu = Death_menu(self)
		self.gameover_menu = Gameover_menu(self)
		self.opt_level_menu = Opt_level_menu(self)

		# Main_menu_text(self, "* Menu *", (X_WINDOW / 2, Y_WINDOW /2), cx=True)

		# self.neutrals = []

	# def generate_neutrals(self):
		# if self.timer <= 0:
		# 	for i in range(1, 3):
		# 		Neutrals(self)
		# 	# Reset the countdown timer to one second.
		# 	self.timer = NEUTRALS_SPAWN_FREQUENCY + randint(0, 1000)

	def load_sprites(self, img, posx=0, posy=0, width=10, height=10, ratio=(1/2)):
		sprite_frames = []
		for line in range(8):
			for column in range(8):
				# print(line, column)
				sub_img = img.subsurface(pygame.Rect((posx +(column * width)),  (posy + (line * height)), width, height)).convert_alpha()
				sub_img = pygame.transform.scale(sub_img, (int(width * ratio), int(height * ratio)))
				sprite_frames.append(sub_img)

		return sprite_frames


	def generate_enemies(self):
		self.timer_gen_e -= self.dt
		if self.timer_gen_e <= 0:
			for i in range(1, 3):
				Enemy(self)
			# Reset the countdown timer to one second.
			self.timer_gen_e = ENEMIES_SPAWN_FREQUENCY + randint(0, 3000)

	def collide_management(self):
		# See if the enemies collide with player
		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies, True)
		# Check the list of collisions.
		for x in collide_list:
			self.player.take_dammage(self, HIT_SHIP_ENNEMIES)
			print("Player Collide with Enemies !")

		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies_shoots, True)
		for hit in collide_list:
			self.player.take_dammage(self, HIT_SHOT_ENNEMIES)
			print("Enemies shots Collide with player !")
			Explosion(self, hit.rect.center, 0)

		collide_list = pygame.sprite.groupcollide(self.sprites_allies_shoots, self.sprites_enemies, True, True)
		# Check the list of collisions.
		for hit in collide_list:
			print("Player Shots Collide with Enemies !")
			self.player.score += HIT_SHOT_PLAYER
			Explosion(self, hit.rect.center, randint(1, 2))


	def level_backgrounds_reinitialization(self):
		self.all_sprites.add(self.level_backgrounds[0])
		self.all_sprites.add(self.level_backgrounds[1])
		self.level_backgrounds[0].rect.y = 0
		self.level_backgrounds[1].rect.y = -Y_WINDOW

	def continue_level(self):
		self.player.continue_level(self)
		self.sprites_enemies_shoots.empty()
		self.sprites_allies_shoots.empty()

	def restart_level(self):
		# Clear all Useless sprites lists
		self.all_sprites.empty()
		self.sprites_enemies.empty()
		self.sprites_enemies_shoots.empty()
		self.sprites_allies_shoots.empty()
		self.sprites_explosions.empty()

		self.player.init_level(self)
		self.level_backgrounds_reinitialization()

	def restart_game(self):
		# Clear all Useless sprites lists
		self.all_sprites.empty()
		self.sprites_enemies.empty()
		self.sprites_enemies_shoots.empty()
		self.sprites_allies_shoots.empty()
		self.sprites_explosions.empty()

		self.player.init_game(self)
		self.level_backgrounds_reinitialization()
