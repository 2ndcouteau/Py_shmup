#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
import time

from random			import randint
from class_Entities	import Entities
from class_Shoot	import Simple_shot, Double_shots, Triple_shots
from constants		import (X_WINDOW, Y_WINDOW,
							LEFT, RIGHT,
							IMG_PLAYER, IMG_PLAYER_SPRITES,
							PLAYER_HP, PLAYER_HP_MAX, PLAYER_LIVES,
							W_SIMPLE, W_DOUBLE, W_TRIPLE,
							TYPE_HP, TYPE_LIFE, TYPE_SHIELD, TYPE_WEAPON, TYPE_SLOWMOTION, TYPE_INVULNERABILITY,
							ALLIES,
							PLAYER_SHOOT_FREQUENCY,
							PLAYER_FRAME_RATE,
							DAMAGE_INVULNERABILITY_TIME, ITEM_DAMAGE_INVULNERABILITY_TIME)

class Player(Entities):

	def __init__(self, g):
		Entities.__init__(self, _hp = PLAYER_HP, _lives = PLAYER_LIVES, _speed = 15, _type = ALLIES)
		self.name = "Player"

		self.timer = 0
		self.timer_shoot = 0
		self.timer_damage = 0
		self.sound_shoot = g.sound_shoot
		self.sound_shoot.set_volume(0.5)
		self.direction = None
		self.frame_rate = PLAYER_FRAME_RATE
		self.sprite_frames = []
		self.sprite_frames_mask = []
		self.range = 0
		self.range_left = -10 # min: -15, max: 0
		self.range_right = 10 # min: 0, max: 15
		# self.weapon = W_SIMPLE
		self.weapon = W_SIMPLE
		self.g = g

		# Load all sprites positions
		self.load_sprites(IMG_PLAYER_SPRITES, width=256, height=256, ratio=1/3)

		# Insert Face ship img
		main_img = IMG_PLAYER.convert_alpha()
		self.size = main_img.get_size()	# Returns tupple
		self.size = (self.size[0] / 3, self.size[1] / 3)
		main_img = pygame.transform.scale(main_img, (int(self.size[0]), int(self.size[1])))
		# self.image = pygame.transform.rotate(self.image, -90);
		self.sprite_frames.insert(0, main_img)
		self.sprite_frames_mask.insert(0, pygame.mask.from_surface(main_img))

		self.image = self.sprite_frames[0]
		self.mask = self.sprite_frames_mask[0]

		# self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect(center=[(X_WINDOW / 2) - self.size[0] / 2, Y_WINDOW - 150])
		# self.rect = self.rect.move((X_WINDOW / 2) - self.size[0] / 2, Y_WINDOW - 150)

		g.all_sprites.add(self)
		g.sprites_players.add(self)

		self.items_fct = []
		self.items_fct.insert(TYPE_HP, self.get_hp)
		self.items_fct.insert(TYPE_LIFE, self.get_life)
		self.items_fct.insert(TYPE_SHIELD, self.get_shield)
		self.items_fct.insert(TYPE_WEAPON, self.get_weapon)
		self.items_fct.insert(TYPE_SLOWMOTION, self.get_slowmotion)
		self.items_fct.insert(TYPE_INVULNERABILITY, self.get_invulnerability)



	def load_sprites(self, img, posx=0, posy=0, width=10, height=10, ratio=(1/2)):
		for index in range(60):
			sub_img = img.subsurface(pygame.Rect((posx + (index * width)), posy, width, height)).convert_alpha()
			sub_img = pygame.transform.scale(sub_img, (int(width * ratio), int(height * ratio)))
			self.sprite_frames.append(sub_img)
			self.sprite_frames_mask.append(pygame.mask.from_surface(sub_img))

	def move(self, direction):
		self.direction = direction
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def shoot(self, g):
		self.timer_shoot -= g.dt
		if self.timer_shoot <= 0:
			if (self.weapon == W_SIMPLE):
				Simple_shot(g, ALLIES, self)
			elif (self.weapon == W_DOUBLE):
				Double_shots(g, ALLIES, self)
			elif (self.weapon == W_TRIPLE):
				Triple_shots(g, ALLIES, self)
			if (g.opt_sfx == True):
				self.sound_shoot.play()
			# self.sound_shoot[randint(0, 5)].play()
			# print("nb_sound == " + str(self.sound_shoot.get_num_channels()))

			# Reset the countdown timer to one second.
			self.timer_shoot = PLAYER_SHOOT_FREQUENCY

	def take_dammage(self, g, dammage):
		if (self.timer_damage <= 0):
			self.hp -= dammage
			self.timer_damage = DAMAGE_INVULNERABILITY_TIME

	def init_game(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP
		self.lives = PLAYER_LIVES
		self.weapon = W_SIMPLE
		self.timer_damage = 0

		# if self.lives < 0:
		self.start_time = time.time()
		self.time = time.time()
		self.score = 0

		g.sprites_players.add(self)
		g.all_sprites.add(self)


	def continue_level(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP
		self.weapon = W_SIMPLE
		self.timer_damage = 0

		g.sprites_players.add(self)
		g.all_sprites.add(self)


	def init_level(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = PLAYER_HP
		self.weapon = W_SIMPLE
		self.timer_damage = 0

		self.start_time = time.time()
		self.time = time.time()
		self.score = 0

		g.sprites_players.add(self)
		g.all_sprites.add(self)

	def update_image(self):
		center = self.rect.center  ## ??
		self.image = self.sprite_frames[self.range]
		self.mask = self.sprite_frames_mask[self.range]
		self.rect = self.image.get_rect()
		self.rect.center = center

	def manage_direction_animation(self):
		self.timer -= self.g.dt
		if (self.direction is not None) : # Animation from player input
			if (self.timer <= 0):
				if (self.direction == RIGHT):
					if ((self.range + 1) < self.range_right):
						self.range += 6 if (self.range < 0) else 1
						self.update_image()
				elif (self.direction == LEFT):
					if ((self.range - 1) > self.range_left):
						self.range -= 6 if (self.range > 0) else 1
						self.update_image()
				self.timer = self.frame_rate
				self.direction = None
		else :		# Animation without player input
			if (self.range != 0):
				self.range += -1 if (self.range > 0) else 1
				self.update_image()

	def get_hp(self):
		if ((self.hp + 50) < PLAYER_HP_MAX):
			self.hp += 50
		else :
			self.hp = PLAYER_HP_MAX

	def get_life(self):
		self.lives += 1

	def get_shield(self):
		print("item shield")

	def get_weapon(self):
		if (self.weapon < W_TRIPLE):
			self.weapon += 1

	def get_slowmotion(self):
		print("item slowmotion")

	def get_invulnerability(self):
		self.timer_damage = ITEM_DAMAGE_INVULNERABILITY_TIME

	def get_item(self, item):
		self.items_fct[item.type]()
		self.score += 25

	def update(self):
		self.time = time.time() - self.start_time
		self.timer_damage -= self.g.dt
		if (self.g.opt_autoshoot == True):
			self.shoot(self.g)
		self.manage_direction_animation()
