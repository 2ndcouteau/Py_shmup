#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import os
import pygame

#########################
## COLORS				#
WHITE = (255, 255, 255)	#
BLACK = (0, 0, 0)		#
RED = (255, 0, 0)		#
GREEN = (0, 255, 0)		#
BLUE = (0, 0, 255)		#
YELLOW = (255, 255, 0)	#
#########################

## WINDOW GAME SIZE
X_WINDOW = 670
Y_WINDOW = 710

################################################################################
## LOADING MEDIAS
game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, '../media')

FONT = os.path.join(media_folder, 'kenvector_future_thin.ttf')

IMG_LEVEL1_BACKGROUND = pygame.image.load(os.path.join(media_folder, 'level1_desert.png'))
IMG_MAIN_MENU_BACKGROUND = pygame.image.load(os.path.join(media_folder, 'menu_space.jpg'))

IMG_LEVEL_MENU_BACKGROUND_FULL = pygame.Surface((X_WINDOW, Y_WINDOW))
IMG_LEVEL_MENU_BACKGROUND_TIER = pygame.Surface((int(X_WINDOW / 2), int(Y_WINDOW / 2)))


IMG_PLAYER = pygame.image.load(os.path.join(media_folder, "SF06.png"))
IMG_LASER_PLAYER = pygame.image.load(os.path.join(media_folder, "laserBlue.png"))
IMG_LASER_ENEMY = pygame.image.load(os.path.join(media_folder, "laserRed.png"))

IMG_EXPLOSION1 = pygame.image.load(os.path.join(media_folder, "explosion01.png"))
IMG_EXPLOSION2 = pygame.image.load(os.path.join(media_folder, "explosion02.png"))
IMG_EXPLOSION3 = pygame.image.load(os.path.join(media_folder, "explosion03.png"))
################################################################################


## TYPE ENTITIES
ALLIES = 0
ENEMIES = 1
NEUTRAL = 2

## DIRECTION PLAYER SHIP
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

## FLAG STATE PROG
F_GAME = 1 << 0
F_MAIN_MENU = 1 << 1
F_LEVEL_MENU = 1 << 2

## EVENT FREQUENCY
PLAYER_SHOOT_FREQUENCY = 1000 / 20
ENEMIES_SHOOT_FREQUENCY = 1000 / 10
ENEMIES_SPAWN_FREQUENCY = 1000 / 10

NEUTRALS_SPAWN_FREQUENCY = 1000

MENU_INPUT_DELAY = 125

EXPLOSION_FRAME_RATE = 1000 / 60


## DEFAULT CARACTERISTICS
PLAYER_HP = 100
PLAYER_LIVES = 1
HIT_SHOT_ENNEMIES = 25
HIT_SHIP_ENNEMIES = 33
HIT_SHOT_PLAYER = 17


#############################
## ARRAY GAME LINE POSITION #
							#
POS_HP = 0
POS_LIVES = 1
POS_SCORE = 2
POS_TIME = 3
							#
#############################
## ARRAY MENU LINE POSITION##
							#
TITLE_MENU = 0

## MAIN MENU				#
PLAY = 1
OPTIONS_MAIN = 2
QUIT = 3
## LEVEL MENU				#
RESUME = 1
RESTART = 2
OPTIONS_LEVEL = 3
MAIN_MENU = 4
							#
#############################
