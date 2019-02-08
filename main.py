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


class Player(Entities):

	def __init__(self, g):
		Entities.__init__(self, _hp = 2, _life = 3, _speed = 15, _type = ALLIES)
		self.name = "Player"

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

class Enemy(Entities):
	def __init__(self, g):
		Entities.__init__(self, _hp = 1, _life = 0, _speed = 5, _type = ENEMIES)
		self.name = "Enemy"

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
		self.rect = self.rect.move(randint(self.size[0], X_WINDOW) - self.size[0] , 0)

		self.g = g
		self.g.all_sprites_list.add(self)
		self.g.sprites_enemies_list.add(self)

	def delete(self):
		self.g.all_sprites_list.remove(self)
		self.g.sprites_enemies_list.remove(self)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)

	def update(self):
		self.move(DOWN)

		# If the enemy go out the window, unreference it
		if self.rect.y > Y_WINDOW:
			self.delete()







class Game():
	def __init__(self):
		# Constant

		pygame.init()
		# Set input frequency
		pygame.key.set_repeat(1, 1)

		# This is a list of every sprite.
		self.all_sprites_list = pygame.sprite.Group()
		self.sprites_backgrounds_list = pygame.sprite.Group()
		self.sprites_players_list = pygame.sprite.Group()
		self.sprites_enemies_list = pygame.sprite.Group()
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

	def collide_management(self):
		# See if the enemies collide with player
		collide_list = pygame.sprite.spritecollide(self.player, self.sprites_enemies_list, True)

		# Check the list of collisions.
		for x in collide_list:
			print("Collide !")


def scroll_background(g):
	g.backgrounds[0].rect.y += 1
	g.backgrounds[1].rect.y += 1

	if g.backgrounds[0].rect.y >= Y_WINDOW:
		g.backgrounds[0].rect.y = -Y_WINDOW
	if g.backgrounds[1].rect.y >= Y_WINDOW:
		g.backgrounds[1].rect.y = -Y_WINDOW



# def shoot(g):
# 	# now = pygame.time.get_ticks()
# 	# if now - self.last_shot > self.shoot_delay:
# 	# self.last_shot = now
# 	g.Rect_entities.append(pygame.draw.circle(g.window, [120, 0, 255], (g.player.rect[0], g.player.rect[1] + 15), 5))
# 	# g.window.blit(g.shoots, g.player.rect)
# 	# g.Rect_entities.append(g.shoots[-1].get_rect())
# 	#pygame.draw.circle(screen, YELLOW, (24,24), 7)


def game_event(g, keys):

	if keys[K_BACKSPACE]:
		g.mode = MENU	# change to load_menu()
	if keys[K_RETURN]:
		print("Entrée")
	if keys[K_SPACE]:
#		g.player.shoot(g)
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
		Enemy(g)

def global_envent(g, keys):
	if keys[K_ESCAPE]:
		exit()
	# if keys[K_S]:
	# 	cut_the_sound


def menu_envent(g, keys):
	if keys[K_RETURN] or keys[K_SPACE]:
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
	# Game loop
	while 42:
		pygame.time.Clock().tick(60)

		if (g.mode is GAME):
			# g.window.fill((0,0,0))
			event_manage(g)
			scroll_background(g)

			g.sprites_enemies_list.update()

			g.collide_management()


			# Draw All Spirte list
			# g.all_sprites_list.draw(g.window)
			g.sprites_backgrounds_list.draw(g.window)
			g.sprites_players_list.draw(g.window)
			g.sprites_enemies_list.draw(g.window)

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
