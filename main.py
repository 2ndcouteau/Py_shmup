#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals import *

class Target:
	hp = 100
	speed = 100

class Player(Target):
	name = "Player1"

class Game:
	# Constant
	window = 0
	window_x = 670
	window_y = 720

	backgrounds = []
	y0 = 0
	y1 = -window_y

	player = Player
	ennemies = ()
	entities = ()

def scroll_background(g):
	g.y0 += 1
	g.y1 += 1
	g.window.blit(g.backgrounds[0], (0 ,g.y0))
	g.window.blit(g.backgrounds[1], (0 ,g.y1))

	if g.y0 > g.window_y:
		g.y0 = -g.window_y
	if g.y1 > g.window_y:
		g.y1 = -g.window_y



def main():

	g = Game

	pygame.init()

	# INIT window
	g.window = pygame.display.set_mode((g.window_x, g.window_y), HWSURFACE | DOUBLEBUF | RESIZABLE) ## FULLSCREEN
	icone = pygame.image.load("media/SF06.png")
	title = pygame.display.set_caption("BEST GAME EVER -- Py_SHMUP")

	# Display Background
	g.backgrounds.append(pygame.image.load("media/desert.png").convert())
	g.backgrounds.append(pygame.image.load("media/desert.png").convert())

	s_background = g.backgrounds[0].get_size()
	scale_x = float(g.window_x) / s_background[0]
	scale_y = float(g.window_y) / s_background[1]
	s_background = (s_background[0] * scale_x, s_background[1] * scale_x)
	g.backgrounds[0] = pygame.transform.scale(g.backgrounds[0], (int(s_background[0]), int(s_background[1])))
	g.backgrounds[1] = pygame.transform.scale(g.backgrounds[1], (int(s_background[0]), int(s_background[1])))
	g.window.blit(g.backgrounds[0], (0 ,g.y0))
	g.window.blit(g.backgrounds[1], (0 ,g.y1))

	# Display Player
	player = pygame.image.load("media/SF06.png").convert_alpha()
	# Scale player ship
	s_player = player.get_size()	# Returns tupple
	s_player = (s_player[0] / 3, s_player[1] / 3)
	player = pygame.transform.scale(player, (int(s_player[0]), int(s_player[1])))
	hit_box_player = pygame.transform.scale(player, (int(s_player[0]) - 10, int(s_player[1]) - 10))

	# Init player ship position
	player_pos = player.get_rect()
	player_pos = player_pos.move((s_background[0] / 2) - s_player[0] / 2, s_background[1] - 150)
	#player = pygame.transform.rotate(player, -90);


	# print ("high == " + str(s_player[0]) + " Width == "  + str(s_player[1]))
	g.window.blit(player, player_pos)

	# Rafraîchissement de l'écran
	pygame.display.flip()
	# Set input frequency
	pygame.key.set_repeat(1, 1)


	# Game loop
	while 42:
		## BAD # for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
		pygame.event.pump() ## Good way to manage event

		keys = pygame.key.get_pressed()
		if keys[K_q]:  # Si un de ces événements est de type QUIT
			exit()
		if keys[K_RETURN]:
			print("Entrée")
		if keys[K_SPACE]:
			print("Espace")
		if keys[K_b]:
			print("Bomb")
		if keys[K_UP] or keys[K_w]:
			player_pos = player_pos.move(0,-15)
		if keys[K_DOWN] or keys[K_s]:
			player_pos = player_pos.move(0,15)
		if keys[K_LEFT] or keys[K_a]:
			player_pos = player_pos.move(-15,0)
		if keys[K_RIGHT] or keys[K_d]:
			player_pos = player_pos.move(15,0)

		pygame.event.clear()


		player_pos = player_pos.clamp(g.window.get_rect())
		scroll_background(g)


#		g.window.blit(background, (0,0))
		g.window.blit(player, player_pos)

	#	pygame.display.update((player_pos, g.backgrounds[0], g.backgrounds[1]))
		# Refresh ALL the Display
		pygame.display.flip()
		# Set frame frequency
		pygame.time.Clock().tick(60)



if __name__ == '__main__':
	print ("Welcome in PyShmup !")
	main()
