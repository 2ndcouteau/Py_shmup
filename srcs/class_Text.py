#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
import time

from pygame.locals	import *

from constants			import (Y_WINDOW, X_WINDOW,
								FONT,
								GAME, MAIN_MENU, LEVEL_MENU,
								WHITE, BLACK, RED, GREEN, BLUE, YELLOW,
								POS_HP, POS_LIFES, POS_SCORE, POS_TIME
								)


class Text_line(pygame.sprite.Sprite):
	def __init__(self, font_size, text, pos, cx=False, cy=True, selected=False):
		pygame.sprite.Sprite.__init__(self)

		self.font_size = font_size
		self.text = text
		self.cx = cx
		self.cy = cy
		self.pos = list(pos)
		self.selected = selected

		self.font_low = pygame.font.Font(FONT, font_size)
		self.font_big = pygame.font.Font(FONT, font_size * 2)

		self.image_low = self.font_low.render(self.text, True, WHITE)
		self.image_big = self.font_big.render(self.text, True, WHITE)

		self.rect_low = self.image_low.get_rect()
		self.size_low = self.image_low.get_size()

		self.rect_big = self.image_big.get_rect()
		self.size_big = self.image_big.get_size()

		if selected:
			self.image = self.image_big
			self.rect = self.rect_big
		else:
			self.image = self.image_low
			self.rect = self.rect_low

		# self.old_size = self.new_size * 2
		self.position_text(self)


	def position_text(self, text):
		#cx= center_x, cy= center_y
		text.pos_low = text.pos
		text.pos_big = text.pos

		if text.cx :
			text.rect_low.centerx = X_WINDOW / 2
			text.rect_big.centerx = X_WINDOW / 2
			# text.pos_low[0] -= text.size_low[0] / 2
			# text.pos_big[0] -= text.size_big[0] / 2
		else:
			text.rect_low.x += text.pos_low[0]
			text.rect_big.x += text.pos_big[0]

		if text.cy :
			text.rect_low.centery = text.pos_low[1] - text.size_low[1] / 2
			text.rect_big.centery = text.pos_big[1] - text.size_big[1] / 2
			# text.rect_low.y += text.pos_low[1]
			# text.rect_big.y += text.pos_big[1]
			# text.rect_low.centery = Y_WINDOW / 2
			# text.rect_big.centery = Y_WINDOW / 2
		else:
			text.rect_low.y += text.pos_low[1]
			text.rect_big.y += text.pos_big[1]

class Text():
	def __init__(self):
		self.all_text = []

	def draw_text(self, window):
		for text in self.all_text:
			window.blit(text.image, text.rect)

class Text_menu():
	def __init__(self):
		self.y_offset_pos = 50
		self.prev_pos = 1
		self.new_pos = 1

	def move_up(self):
		if (self.new_pos > 1):
			self.new_pos -= 1
		else:
			self.new_pos = self.len_all_text - 1

	def move_down(self):
		if (self.new_pos < self.len_all_text - 1):
			self.new_pos += 1
		else:
			self.new_pos = 1

	def update(self):
		# self.draw_text()

		if self.prev_pos != self.new_pos:
			self.all_text[self.prev_pos].image = self.all_text[self.prev_pos].image_low
			self.all_text[self.prev_pos].rect = self.all_text[self.prev_pos].rect_low

			self.all_text[self.new_pos].image = self.all_text[self.new_pos].image_big
			self.all_text[self.new_pos].rect = self.all_text[self.new_pos].rect_big

			self.prev_pos = self.new_pos

class Text_game():
	def __init__(self):
		self.x_right_time_offset = 170
		self.x_right_life_offset = 100
		self.x_left_offset = 5
		self.y_bottom_offset = 25

	def update(self):
		self.str_time = time.strftime("%M:%S.", time.gmtime(self.g.player.time)) + str(repr(self.g.player.time).split('.')[1][:3])

		self.all_text[POS_HP] = Text_line(self.font_size, ' '.join(["Hp: ", str(self.g.player.hp)]), (self.x_left_offset, Y_WINDOW - self.y_bottom_offset), cx=False, cy=False)
		self.all_text[POS_LIFES] = Text_line(self.font_size, ' '.join(["Lifes: ", str(self.g.player.life)]), ((X_WINDOW - self.x_right_life_offset), Y_WINDOW - self.y_bottom_offset), cx=False, cy=False)
		self.all_text[POS_SCORE] = Text_line(self.font_size, ' '.join(["Score: ", str(self.g.player.score)]), (self.x_left_offset, 0), cx=False, cy=False)
		self.all_text[POS_TIME] = Text_line(self.font_size, "Time: {0}".format(self.str_time), (X_WINDOW - self.x_right_time_offset, 0), cx=False, cy=False)


class Text_game_level(Text, Text_game):
	def __init__(self, g):
		Text.__init__(self)
		Text_game.__init__(self)

		self.title_font_size = 24
		self.font_size = 18
		self.g = g

		self.str_time = time.strftime("%M:%S.", time.gmtime(self.g.player.time)) + str(repr(self.g.player.time).split('.')[1][:3])
		self.all_text.insert(POS_HP, Text_line(self.font_size, ' '.join(["Hp:", str(g.player.hp)]), (self.x_left_offset, Y_WINDOW - self.y_bottom_offset), cx=False, cy=False))
		self.all_text.insert(POS_LIFES, Text_line(self.font_size, ' '.join(["Lifes:", str(g.player.life)]), ((X_WINDOW - 100), Y_WINDOW - self.y_bottom_offset), cx=False, cy=False))
		self.all_text.insert(POS_SCORE, Text_line(self.font_size, ' '.join(["Score:", str(g.player.score)]), (self.x_left_offset, 0), cx=False, cy=False))
		self.all_text.insert(POS_TIME, Text_line(self.font_size, "Time: {0}".format(self.str_time), ((X_WINDOW - self.x_right_time_offset), 0), cx=False, cy=False))

		# self.all_text.append(Text_line(self.title_font_size, "- Menu -", ((X_WINDOW / 2), Y_WINDOW / 4), cx=True, cy=False))
		self.len_all_text = len(self.all_text)


class Text_level_menu(Text, Text_menu):
	def __init__(self):
		Text.__init__(self)
		Text_menu.__init__(self)

		self.title_font_size = 24
		self.font_size = 12

		self.all_text.append(Text_line(self.title_font_size, "- Menu -", ((X_WINDOW / 2), Y_WINDOW / 4), cx=True, cy=False))
		self.all_text.append(Text_line(self.font_size, "* Resume *", ((X_WINDOW / 2), (Y_WINDOW / 2) - (self.y_offset_pos * 1) - 15), cx=True, selected=True))
		self.all_text.append(Text_line(self.font_size, "* Restart *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 0) - 15), cx=True, selected=False))
		self.all_text.append(Text_line(self.font_size, "* Options *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 1) - 15), cx=True, selected=False))
		self.all_text.append(Text_line(self.font_size, "* Main Menu *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 2) - 15), cx=True, selected=False))

		self.len_all_text = len(self.all_text)


class Text_main_menu(Text, Text_menu):
	def __init__(self):
		Text.__init__(self)
		Text_menu.__init__(self)

		self.title_font_size = 32
		self.font_size = 16

		self.all_text.append(Text_line(self.title_font_size, "Hard SHMUP 42", ((X_WINDOW / 2), Y_WINDOW / 4), cx=True))
		self.all_text.append(Text_line(self.font_size, "* Play *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 0)), cx=True, selected=True))
		self.all_text.append(Text_line(self.font_size, "* Options *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 1)), cx=True, selected=False))
		self.all_text.append(Text_line(self.font_size, "* Quit *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 2)), cx=True, selected=False))


		self.len_all_text = len(self.all_text)
