
from src.settings import *

import pygame

class Board(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/board.png').convert()
        self.image = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect = self.image.get_rect()
