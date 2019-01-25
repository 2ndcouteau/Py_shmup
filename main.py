

import pygame
from pygame.locals import *


pygame.init();

window = pygame.display.set_mode((1000, 720), RESIZABLE) ## FULLSCREEN
fond = pygame.image.load("media/background.jpg").convert()
player = pygame.image.load("media/SF06.png").convert_alpha()
window.blit(fond, (0,0))
window.blit(player, (470, 500))

#Rafraîchissement de l'écran
pygame.display.flip()


input = 1

while 1:
	continue
#	input = int(input())
