#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import os
import pygame
from pygame.locals	import *

# from pygame.sprite import Sprite

from class_Game	import Game
from constants	import (X_WINDOW,
						Y_WINDOW,
						GAME,
						MENU,
						UP,
						DOWN,
						RIGHT,
						LEFT)




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

			# g.sprites_neutrals.draw(g.window)


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
