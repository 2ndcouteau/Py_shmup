import pygame
from random			import randint

from class_Enemy	import Enemy
from constants		import (UP, DOWN, RIGHT, LEFT,
							POS_LEFT, POS_RIGHT,
							WINDOW_X
							)



class Waves():
	def __init__(self, g):
		self.g = g

	def h_line(self, nb_enemies, position=POS_LEFT):
		for i in range(nb_enemies) :
			enemy = Enemy(self)
			self.align(enemy, position, i, nb_enemies)

	def align(self, enemy, position, i, nb_enemies):
		if (position == LEFT):
			landmark = 0
		elif (position == RIGHT):
			landmark = WINDOW_X

		enemy.rect.centerx = ((enemy.size[0] / 2) + 15) * (1 + i)
