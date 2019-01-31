#!/usr/bin/python3
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals import *


pygame.init()

## CONSTANT
window_x = 1280
window_y = 720

# INIT window
window = pygame.display.set_mode((window_x, window_y), HWSURFACE | DOUBLEBUF | RESIZABLE) ## FULLSCREEN
icone = pygame.image.load("media/SF06.png")
title = pygame.display.set_caption("BEST GAME EVER -- Py_SHMUP")

# Display Background
background = pygame.image.load("media/desert.png").convert()
s_background = background.get_size()
scale_x = float(window_y) / s_background[0]
scale_y = float(window_y) / s_background[1]
s_background = (s_background[0] * scale_x, s_background[1] * scale_x)
background = pygame.transform.scale(background, (int(s_background[0]), int(s_background[1])))
window.blit(background, (0 ,0))


# Display Player
player = pygame.image.load("media/SF06.png").convert_alpha()
player_pos = player.get_rect()
s_player = player.get_size()
s_player = (s_player[0] / 3, s_player[1] / 3)
player = pygame.transform.scale(player, (int(s_player[0]), int(s_player[1])))
player_pos = player_pos.move((s_background[0] / 2) - s_player[0] / 2, s_background[1] - 150)
#player = pygame.transform.rotate(player, -90);

# print ("high == " + str(s_player[0]) + " Width == "  + str(s_player[1]))
window.blit(player, player_pos)

# Rafraîchissement de l'écran
pygame.display.flip()


pygame.key.set_repeat(1, 1)

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

	window.blit(background, (0,0))
	window.blit(player, player_pos)
	#Rafraichissement
	pygame.display.flip()

	pygame.time.Clock().tick(60)
