#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import os
import pygame
from pygame.locals import *

from random import randint
# from pygame.sprite import Sprite


game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, 'media')

IMG_BACKGROUND = pygame.image.load(os.path.join(image_folder, 'desert.png'))
IMG_PLAYER = pygame.image.load(os.path.join(image_folder, "SF06.png"))

X_WINDOW = 670
Y_WINDOW = 710

ALLIES = 0
ENEMIES = 1
NEUTRAL = 2

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

GAME = 1 << 0
MENU = 1 << 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PLAYER_SHOOT_FREQUENCY = 50
ENEMIES_SHOOT_FREQUENCY = 500
ENEMIES_SPAWN_FREQUENCY = 500

class Entities(pygame.sprite.Sprite):
	def __init__(self, _hp, _life, _speed, _type):
		pygame.sprite.Sprite.__init__(self)
		self.hp = _hp
		self.life = _life
		self.speed = _speed
		self.type = _type

class Background(Entities):
	def __init__(self, g, y_start):
		Entities.__init__(self, _hp = None, _life = None, _speed = 1, _type = NEUTRAL)

		self.image = IMG_BACKGROUND.convert()
		self.size = self.image.get_size()
		scale_x = float(X_WINDOW) / self.size[0]
		scale_y = float(Y_WINDOW) / self.size[1]
		self.size = (self.size[0] * scale_x, self.size[1] * scale_x)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		self.rect = self.image.get_rect()
		self.rect.y = y_start

		g.all_sprites_list.add(self)
		g.sprites_backgrounds_list.add(self)


class Shoot(Entities):
	def __init__(self, g, type, speed, x, y):
		Entities.__init__(self, _hp = 1, _life = 0, _speed = speed, _type = type)
		self.name = "Shoot"

		# Load image from media
		# self.image = IMG_PLAYER.convert_alpha()
		# g.Rect_entities.append(pygame.draw.circle(g.window, [120, 0, 255], (g.player.rect[0], g.player.rect[1] + 15), 5))
		self.image = pygame.Surface((4, 15))

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple

		# Init shoot ship position
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x

		if self.type == ALLIES:
			self.image.fill(BLUE)
			self.direction = UP
			g.sprites_allies_shoots_list.add(self)
		else:
			self.image.fill(RED)
			self.direction = DOWN
			g.sprites_enemies_shoots_list.add(self)

		g.all_sprites_list.add(self)

	def move(self):
		self.rect = self.rect.move(self.direction[0] * self.speed, self.direction[1] * self.speed)

	def update(self):
		self.move()

		# If the shoot go out the window, unreference it
		if self.rect.top > Y_WINDOW and self.type == ENEMIES:
			self.kill()
		elif self.rect.bottom < 0 and self.type == ALLIES:
			self.kill()



class Player(Entities):

	def __init__(self, g):
		Entities.__init__(self, _hp = 3, _life = 3, _speed = 15, _type = ALLIES)
		self.name = "Player"

		self.timer = 0

		# Load image from media
		self.image = IMG_PLAYER.convert_alpha()

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 3, self.size[1] / 3)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		# self.image = pygame.transform.rotate(self.image, -90);
		self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect()
		self.rect = self.rect.move((X_WINDOW / 2) - self.size[0] / 2, Y_WINDOW - 150)

		g.all_sprites_list.add(self)
		g.sprites_players_list.add(self)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def shoot(self, g):
		self.timer -= g.dt
		if self.timer <= 0:
			Shoot(g, ALLIES, self.speed + 1, self.rect.centerx, self.rect.top)
			# Reset the countdown timer to one second.
			self.timer = PLAYER_SHOOT_FREQUENCY

	def reinitialization(self, g):
		# Init player position and spec
		self.rect.x = (X_WINDOW / 2) - self.size[0] / 2
		self.rect.y = Y_WINDOW - 150
		self.hp = 3

		g.sprites_players_list.add(self)
		g.all_sprites_list.add(self)



class Enemy(Entities):
	def __init__(self, g):
		Entities.__init__(self, _hp = 1, _life = 0, _speed = 5, _type = ENEMIES)
		self.name = "Enemy"

		self.timer = 0

		# Load image from media
		self.image = IMG_PLAYER.convert_alpha()

		# Scale player ship
		self.size = self.image.get_size()	# Returns tupple
		self.size = (self.size[0] / 4, self.size[1] / 4)
		self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
		self.image = pygame.transform.rotate(self.image, 180);
		self.hit_box_player = pygame.transform.scale(self.image, (int(self.size[0]) - 10, int(self.size[1]) - 10))

		# Init player ship position
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(randint(self.size[0], X_WINDOW) - self.size[0] , -self.size[1])

		# self.g = g
		g.all_sprites_list.add(self)
		g.sprites_enemies_list.add(self)

		self.g = g

	def shoot(self):
		self.timer -= self.g.dt
		if self.timer <= 0:
			Shoot(self.g, ENEMIES, self.speed * 2, self.rect.centerx, self.rect.bottom)
			# Reset the countdown shoot timer + salt time
			self.timer = ENEMIES_SHOOT_FREQUENCY + randint(0, 1000)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def update(self):
		self.move(DOWN)
		self.shoot()

		# If the enemy go out the window, unreference it
		if self.rect.y > Y_WINDOW:
			self.kill()

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


def scroll_background(g):
	g.backgrounds[0].rect.y += 1
	g.backgrounds[1].rect.y += 1

	if g.backgrounds[0].rect.y >= Y_WINDOW:
		g.backgrounds[0].rect.y = -Y_WINDOW
	if g.backgrounds[1].rect.y >= Y_WINDOW:
		g.backgrounds[1].rect.y = -Y_WINDOW


def game_event(g, keys):

	if g.player.hp <= 0:
		print("You Died")
		g.mode = MENU	# change to load_menu()
	if keys[K_BACKSPACE]:
		g.mode = MENU	# change to load_menu()
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

def global_envent(g, keys):
	if keys[K_ESCAPE]:
		exit()
	# if keys[K_S]:
	# 	cut_the_sound


def menu_envent(g, keys):
	if (g.player.hp > 0):
		if keys[K_RETURN] or keys[K_SPACE]:
			g.mode = GAME
	if keys[K_r]:
		g.restart_game()
		g.mode = GAME

def event_manage(g):
	pygame.event.pump() ## Good way to manage event
	keys = pygame.key.get_pressed()
	# if event.type == pygame.KEYDOWN:
	# print ("Button pressed !")
	global_envent(g, keys)
	if (g.mode is GAME):
		game_event(g, keys)
	else:
		menu_envent(g, keys)

	pygame.event.clear()
	g.player.rect = g.player.rect.clamp(g.window_rect)


def game_loop(g):
	while 42:
		# dt = time in milliseconds that passed since last tick.
		g.dt = pygame.time.Clock().tick(60)
		g.timer -= g.dt

		if (g.mode is GAME):
			# g.window.fill((0,0,0))
			g.generate_enemies()
			event_manage(g)
			scroll_background(g)

			g.sprites_enemies_list.update()
			g.sprites_enemies_shoots_list.update()
			g.sprites_allies_shoots_list.update()


			g.collide_management()


			# Draw All Spirte list
			# g.all_sprites_list.draw(g.window)
			g.sprites_backgrounds_list.draw(g.window)
			g.sprites_players_list.draw(g.window)
			g.sprites_enemies_list.draw(g.window)
			g.sprites_enemies_shoots_list.draw(g.window)
			g.sprites_allies_shoots_list.draw(g.window)

			# self.shoots = []
			# self.neutrals = []


			# Refresh ALL the Display
				# update() is faster than flip()
			# pygame.display.update(g.all_sprites_list)

			pygame.display.flip()

		else:
			event_manage(g)

def main():

	g = Game()
	game_loop(g)




if __name__ == '__main__':
	print ("Welcome in PyShmup !")
	main()
