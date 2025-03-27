# C
import pygame

C_ORANGE = (252, 92, 38)
C_WHITE = (255, 255, 255)
C_YELLOW = (252, 202, 38)
C_GREEN = (0, 128, 0)

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
    'PlayerShot': 2,
    'Obst1': 3,
    'Obst2': 3,
    'Obst3': 3,
    'Obst4': 3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player': 3,
    'PlayerShot': 1,
    'Obst1': 1,
    'Obst2': 2,
    'Obst3': 1,
    'Obst4': 2,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player': 0,
    'PlayerShot': 1,
    'Obst1': 20,
    'Obst2': 25,
    'Obst3': 20,
    'Obst4': 25,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player': 0,
    'PlayerShot': 0,
    'Obst1': 100,
    'Obst2': 125,
    'Obst3': 100,
    'Obst4': 125,
}

ENTITY_SHOT_DELAY = {'Player': 20}

# M
MENU_OPTION = ('NEW GAME',
               'HIGH SCORE',
               'EXIT')

# P
PLAYER_KEY_SHOOT = {'Player': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }