#!/usr/bin/env python3.7
# _*_ coding: Utf-8 -*

import os
import pygame

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, '../media')

FONT = os.path.join(media_folder, 'kenvector_future_thin.ttf')


IMG_BACKGROUND = pygame.image.load(os.path.join(media_folder, 'desert.png'))
IMG_PLAYER = pygame.image.load(os.path.join(media_folder, "SF06.png"))
IMG_LASER_PLAYER = pygame.image.load(os.path.join(media_folder, "laserBlue.png"))
IMG_LASER_ENEMY = pygame.image.load(os.path.join(media_folder, "laserRed.png"))

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

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PLAYER_SHOOT_FREQUENCY = 50
ENEMIES_SHOOT_FREQUENCY = 500
ENEMIES_SPAWN_FREQUENCY = 500

NEUTRALS_SPAWN_FREQUENCY = 1000

PLAYER_HP = 30
