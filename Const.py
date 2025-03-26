# C
import pygame

C_ORANGE = (252, 92, 38)
C_WHITE = (255, 255, 255)
C_YELLOW = (252, 202, 38)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 3,
    'Obst1': 3,
    'Obst2': 3,
    'Obst3': 3,
    'Obst4': 3,
}

# M
MENU_OPTION = ('NEW GAME',
               'HIGH SCORE',
               'EXIT')

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
