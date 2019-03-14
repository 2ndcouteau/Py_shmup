import pygame
from random import randint


from class_Entities	import Entities

from constants			import (X_WINDOW, Y_WINDOW,
								NEUTRAL,
								IMG_HP, IMG_LIFE, IMG_SHIELD, IMG_WEAPON, IMG_SLOWMOTION, IMG_INVULNERABILITY,
								TYPE_HP, TYPE_LIFE, TYPE_SHIELD, TYPE_WEAPON, TYPE_SLOWMOTION, TYPE_INVULNERABILITY,
								DOWN)

items = [
	[TYPE_HP, IMG_HP],
	[TYPE_LIFE, IMG_LIFE],
	[TYPE_SHIELD, IMG_SHIELD],
	[TYPE_WEAPON, IMG_WEAPON],
	[TYPE_SLOWMOTION, IMG_SLOWMOTION],
	[TYPE_INVULNERABILITY, IMG_INVULNERABILITY]
]

class Items(Entities):
	def __init__(self, g, position):
		Entities.__init__(self, _hp = 0, _lives = 0, _speed = 2, _type = NEUTRAL)
		self.name = "Item"

		self.g = g

		# Load image from media
		self.type = items[randint(0, len(items) - 1)][0]
		self.image = items[self.type][1].convert_alpha()

		self.size = self.image.get_size()
		# self.size = (self.size[0] / 3, self.size[1] / 3)
		# self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))

		# Init item position
		self.rect = self.image.get_rect(center=position)

		self.mask = pygame.mask.from_surface(self.image)


		g.all_sprites.add(self)
		g.sprites_items.add(self)


	def generate(self, g, position):
		if (randint(0, 20) == 0):
			Items(g, position)

	def move(self, direction):
		self.rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed * self.g.speed_game)

	def update(self):
		self.move(DOWN)
		if (self.rect.top > Y_WINDOW):
			self.kill()
