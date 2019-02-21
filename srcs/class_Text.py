#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import pygame
from pygame.locals	import *

from constants			import (Y_WINDOW,
								X_WINDOW,
								FONT,
								GAME,
								MAIN_MENU,
								LEVEL_MENU,
								WHITE,
								BLACK,
								RED,
								GREEN,
								BLUE,
								YELLOW)


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

		print (text.rect_low)
		print (text.rect_big)
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

#
# class Level_text(Text):
# 	def __init__(self, g, msg, pos, cx=False, cy=False):
# 		Text.__init__(self, g, msg, pos, cx, cy)
#
# 		g.sprites_level_text.add(self)
#
#
# class Level_menu_text(Text):
# 	def __init__(self, g, msg, pos, cx=False, cy=False):
# 		pos = (g.level_menu_backgrounds[1].rect.x + pos[0], g.level_menu_backgrounds[1].rect.y + pos[1])
# 		Text.__init__(self, g, msg, pos, cx, cy)
#
# 		g.sprites_level_menu_text.add(self)

#
# class Main_menu_text_elem(Text):
# 	def __init__(self, g, msg, pos, cx=False, cy=False):
# 		Text.__init__(self, g, msg, pos, cx , cy)

		# g.sprites_main_menu_text.add(self)
class Text():
	def __init__(self):
		self.all_text = []

	def draw_text(self, window):
		for text in self.all_text:
			window.blit(text.image, text.rect)

	#
	# font = pygame.font.Font(font_name, size)
	# text_surface = font.render(text, True, WHITE)
	# text_rect = text_surface.get_rect()
	# text_rect.midtop = (x, y)
	# surf.blit(text_surface, text_rect)


class Text_level_menu(Text):
	def __init__(self):
		Text.__init__(self)

		self.y_offset_pos = 75
		self.prev_pos = 1
		self.new_pos = 1
		self.title_font_size = 24
		self.font_size = 12

		self.all_text.append(Text_line(self.title_font_size, "- Menu -", ((X_WINDOW / 2), Y_WINDOW / 4), cx=True, cy=False))
		self.all_text.append(Text_line(self.font_size, "* Resume *", ((X_WINDOW / 2), (Y_WINDOW / 2) - (self.y_offset_pos * 1) - 15), cx=True, selected=True))
		self.all_text.append(Text_line(self.font_size, "* Restart *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 0) - 15), cx=True, selected=False))
		self.all_text.append(Text_line(self.font_size, "* Options *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 1) - 15), cx=True, selected=False))
		self.all_text.append(Text_line(self.font_size, "* Main Menu *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 2) - 15), cx=True, selected=False))

		self.len_all_text = len(self.all_text)

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

	# def update_position_text(self, text):
	#
	# 	text.size = text.image.get_size()
	# 	text.rect.centerx = (X_WINDOW / 2)
	# 	print ("rect X center == ", str(text.rect.centerx))
		# if size_up :
		# 	text.pos[0] -= text.size[0] / 2
		# 	text.pos[1] -= text.size[1] / 2
		# else :
		# 	text.pos[0] += text.size[0] / 2
		# 	text.pos[1] += text.size[1] / 2
		#
		# 	text.rect.x = text.pos[0]
		# 	text.rect.y = text.pos[1]

		# tmp = text.new_size
		# text.new_size = text.old_size
		# text.old_size = tmp

	def update(self):
		# self.draw_text()

		if self.prev_pos != self.new_pos:
			self.all_text[self.prev_pos].image = self.all_text[self.prev_pos].image_low
			self.all_text[self.prev_pos].rect = self.all_text[self.prev_pos].rect_low

			self.all_text[self.new_pos].image = self.all_text[self.new_pos].image_big
			self.all_text[self.new_pos].rect = self.all_text[self.new_pos].rect_big

			self.prev_pos = self.new_pos

			# self.all_text[self.prev_pos].image = self.all_text[self.prev_pos].font_low.render(self.all_text[self.prev_pos].text, True, WHITE)
			# self.update_position_text(self.all_text[self.prev_pos])#, size_up=False)
			# self.position_text(list(self.all_text[self.prev_pos].pos), self.all_text[self.prev_pos].cx, self.all_text[self.prev_pos].cy)

			# self.all_text[self.new_pos].image = self.all_text[self.new_pos].font_big.render(self.all_text[self.new_pos].text, True, WHITE)
			# self.update_position_text(self.all_text[self.new_pos])#, size_up=True)
			# self.position_text(list(self.all_text[self.new_pos].pos), self.all_text[self.new_pos].cx, self.all_text[self.new_pos].cy)




class Text_main_menu(Text):
	def __init__(self):
		Text.__init__(self)

		self.y_offset_pos = 75
		self.prev_pos = 1
		self.new_pos = 1
		self.title_font_size = 32
		self.font_size = 16

		self.all_text.append(Text_line(self.title_font_size, "* Menu *", ((X_WINDOW / 2), Y_WINDOW / 4), cx=True))
		self.all_text.append(Text_line(self.font_size, "* Play *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 0)), cx=True, selected=True))
		self.all_text.append(Text_line(self.font_size, "* Options *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 1)), cx=True, selected=False))
		self.all_text.append(Text_line(self.font_size, "* Quit *", ((X_WINDOW / 2), (Y_WINDOW / 2) + (self.y_offset_pos * 2)), cx=True, selected=False))

		self.len_all_text = len(self.all_text)

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

	def update_position_text(self, text):#, size_up):
		#cx= center_x, cy= center_y
		print (text.text, str(text.pos))
		print(text.size)

		print ("WINDOW X Center == ", str(X_WINDOW / 2))
		text.size = text.image.get_size()
		text.rect.centerx = (X_WINDOW / 2)# - (text.size[0] / 2)
		print ("rect X center == ", str(text.rect.centerx))
		# if size_up :
		# 	text.pos[0] -= text.size[0] / 2
		# 	text.pos[1] -= text.size[1] / 2
		# else :
		# 	text.pos[0] += text.size[0] / 2
		# 	text.pos[1] += text.size[1] / 2
		#
		# 	text.rect.x = text.pos[0]
		# 	text.rect.y = text.pos[1]

		# tmp = text.new_size
		# text.new_size = text.old_size
		# text.old_size = tmp

	def update(self):
		# self.draw_text()

		if self.prev_pos != self.new_pos:
			self.all_text[self.prev_pos].image = self.all_text[self.prev_pos].image_low
			self.all_text[self.prev_pos].rect = self.all_text[self.prev_pos].rect_low

			self.all_text[self.new_pos].image = self.all_text[self.new_pos].image_big
			self.all_text[self.new_pos].rect = self.all_text[self.new_pos].rect_big

			# self.all_text[self.prev_pos].image = self.all_text[self.prev_pos].font_low.render(self.all_text[self.prev_pos].text, True, WHITE)
			# self.update_position_text(self.all_text[self.prev_pos])#, size_up=False)
			# self.position_text(list(self.all_text[self.prev_pos].pos), self.all_text[self.prev_pos].cx, self.all_text[self.prev_pos].cy)

			# self.all_text[self.new_pos].image = self.all_text[self.new_pos].font_big.render(self.all_text[self.new_pos].text, True, WHITE)
			# self.update_position_text(self.all_text[self.new_pos])#, size_up=True)
			# self.position_text(list(self.all_text[self.new_pos].pos), self.all_text[self.new_pos].cx, self.all_text[self.new_pos].cy)

			self.prev_pos = self.new_pos
