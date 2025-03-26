#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Const import WIN_WIDTH, WIN_HEIGHT
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (35, WIN_HEIGHT - 75))
            case 'Obst1':
                return Enemy('Obst1', (WIN_WIDTH + 10, WIN_HEIGHT - 75))
            case 'Obst2':
                return Enemy('Obst2', (WIN_WIDTH + 10, WIN_HEIGHT - 75))
            case 'Obst3':
                return Enemy('Obst3', (WIN_WIDTH + 10, WIN_HEIGHT - 75))
            case 'Obst4':
                return Enemy('Obst4', (WIN_WIDTH + 10, WIN_HEIGHT - 75))



