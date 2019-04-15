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
from class_Items		import Items
from class_Background	import Level_backgrounds, Level_menu_backgrounds, Main_menu_backgrounds
from class_Text			import Text_main_menu, Text_level_menu, Text_level
from class_Menu			import Main_menu, Level_menu, Death_menu, Gameover_menu, Opt_level_menu

from constants			import (X_WINDOW, Y_WINDOW, NORMAL_SPEED_GAME,
								ENEMIES_SPAWN_FREQUENCY, NEUTRALS_SPAWN_FREQUENCY,
								F_GAME, F_MAIN_MENU, F_LEVEL_MENU,
								IMG_LEVEL1_BACKGROUND, IMG_MAIN_MENU_BACKGROUND,
								IMG_LEVEL_MENU_BACKGROUND_FULL, IMG_LEVEL_MENU_BACKGROUND_TIER,
								IMG_PLAYER, IMG_EXPLOSION1, IMG_EXPLOSION2, IMG_EXPLOSION3,
								HIT_SHOT_ENNEMIES, HIT_SHIP_ENNEMIES, HIT_SHOT_PLAYER,
								TYPE_HP, TYPE_LIFE, TYPE_SHIELD, TYPE_WEAPON, TYPE_SLOWMOTION, TYPE_INVULNERABILITY,
								sounds_folder)

class Game():
	def __init__(self):
		self.dt = 0
		self.timer = 0 # 1seconde
		self.timer_gen_e = 0
		self.timer_event = 0 # 1seconde
		self.menu_timer = 0

		self.last_update = 0

		pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)
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
		self.sprites_items = pygame.sprite.Group()

		self.sprites_allies_shoots = pygame.sprite.Group()
		self.sprites_enemies_shoots = pygame.sprite.Group()
#		self.sprites_neutrals_list = pygame.sprite.Group()

		self.sprites_explosions = pygame.sprite.Group()

		# self.sprites_hitbox = pygame.sprite.Group()


		self.sound_explosion = pygame.mixer.Sound(os.path.join(sounds_folder, 'explosion42.wav'))
		self.sound_shoot = pygame.mixer.Sound(os.path.join(sounds_folder, 'laser51.wav'))

		self.sound_move_cursor = pygame.mixer.Sound(os.path.join(sounds_folder, 'cursor.wav'))
		self.sound_launch_game = pygame.mixer.Sound(os.path.join(sounds_folder, 'launch_game_iceball.wav'))
		self.sound_select = pygame.mixer.Sound(os.path.join(sounds_folder, 'select_flaunch.wav'))
		self.sound_off = pygame.mixer.Sound(os.path.join(sounds_folder, 'off_Close.wav'))
		self.sound_on = pygame.mixer.Sound(os.path.join(sounds_folder, 'on_Open.wav'))
		self.sound_return = pygame.mixer.Sound(os.path.join(sounds_folder, 'back_Wrong_2.wav'))



		# self.music_channel_level = pygame.mixer.Channel(0)
		# self.music_channel_main_menu = pygame.mixer.Channel()
		self.opt_music = False
		self.opt_sfx = True
		self.opt_autoshoot = True

		self.speed_game = NORMAL_SPEED_GAME

		music.load(os.path.join(sounds_folder, 'main_menu_music.wav'))
		music.set_volume(100)
		music.play(-1)
		if (self.opt_music is False):
			music.pause()


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
		self.previous_mode = F_MAIN_MENU



		self.explosion_imgs = []
		self.explosion_imgs.append(self.load_sprites(IMG_EXPLOSION1, width=256, height=256, ratio=1/3))
		self.explosion_imgs.append(self.load_sprites(IMG_EXPLOSION2, width=256, height=256, ratio=1/2))
		self.explosion_imgs.append(self.load_sprites(IMG_EXPLOSION3, width=256, height=256, ratio=1/2))



		# Init Player:
		self.player = Player(self)

		# Init all backgrounds:
		self.level_backgrounds = Level_backgrounds(self)
		self.level_menu_backgrounds = Level_menu_backgrounds(self)
		self.main_menu_backgrounds = Main_menu_backgrounds(self)

		# Init all Menu:
		self.level_text = Text_level(self)
		self.level_menu = Level_menu(self)
		self.main_menu = Main_menu(self)
		self.death_menu = Death_menu(self)
		self.gameover_menu = Gameover_menu(self)
		self.opt_level_menu = Opt_level_menu(self)

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


	## BE reaplace by class_Wave methods
	def generate_enemies(self):
		self.timer_gen_e -= self.dt
		if self.timer_gen_e <= 0:

		### FOR RANDOM CREATION -- OLD METHOD -- SEE WAVES.PY ###
			for i in range(1, 3):
				Enemy(self)
		### REPLACEMENT IN PROGRESS ###
			# for i in range(10):
			# 	enemy = Enemy(self)
			# 	enemy.rect.centerx = ((enemy.size[0] / 2) + 15) * (1 + i)
		### END NEW PART ###
			# Reset the countdown timer to one second.
			self.timer_gen_e = ENEMIES_SPAWN_FREQUENCY + randint(0, 3000)

	def collide_management(self):
		# See if the enemies collide with player
		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies, True, pygame.sprite.collide_mask)
		# Check the list of collisions.
		for x in collide_list:
			self.player.take_dammage(self, HIT_SHIP_ENNEMIES)
			print("Player Collide with Enemies !")

		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies_shoots, True, pygame.sprite.collide_mask)
		for hit in collide_list:
			self.player.take_dammage(self, HIT_SHOT_ENNEMIES)
			print("Enemies shots Collide with player !")
			Explosion(self, hit.rect.center, 0)

		collide_list = pygame.sprite.groupcollide(self.sprites_allies_shoots, self.sprites_enemies, True, True, pygame.sprite.collide_mask)
		# Check the list of collisions.
		for hit in collide_list:
			print("Player Shots Collide with Enemies !")
			self.player.score += HIT_SHOT_PLAYER
			Explosion(self, hit.rect.center, randint(1, 2))
			Items.generate(Items, self, hit.rect.center)

		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_items, True, pygame.sprite.collide_mask)
		# Check the list of collisions.
		for hit in collide_list:
			self.player.get_item(hit)
			print("Player Collide with Items !")


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
		self.sprites_items.empty()

		self.player.init_level(self)
		self.level_backgrounds.reinitialization(self)
		# self.level_backgrounds_reinitialization()

	def restart_game(self):
		# Clear all Useless sprites lists
		self.all_sprites.empty()
		self.sprites_enemies.empty()
		self.sprites_enemies_shoots.empty()
		self.sprites_allies_shoots.empty()
		self.sprites_explosions.empty()
		self.sprites_items.empty()

		self.player.init_game(self)
		self.level_backgrounds.reinitialization(self)
		# self.level_backgrounds_reinitialization()
