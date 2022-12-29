
from src.settings import *

import pygame

class Piece(pygame.sprite.Sprite):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__()
        self.image = None
        self.rect = None

        if color != 'white' and color != 'black':
            raise AttributeError('Invalid piece color!')
        self.color = color
        
        if not 0 <= pos[0] < 8 or not 0 <= pos[1] < 8:
            raise AttributeError('Invalid piece position!')
        self.pos = pos

    def pos_to_pixel(self) -> tuple[int]:
        """
        Converts board coordinates of piece into pixel coordinates.
        """
        x = SQUARE_SIZE + self.pos[0] * SQUARE_SIZE
        y = SQUARE_SIZE + BOARD_SIZE - self.pos[1] * SQUARE_SIZE
        return x, y

class Pawn(Piece):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__(color, pos)
        
        images = {
            'white' : pygame.image.load('graphics/pawn_white.png').convert_alpha(),
            'black' : pygame.image.load('graphics/pawn_black.png').convert_alpha()
        }

        self.image = images[self.color]
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(bottomleft=self.pos_to_pixel())

class Knight(Piece):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__(color, pos)
        
        images = {
            'white' : pygame.image.load('graphics/knight_white.png').convert_alpha(),
            'black' : pygame.image.load('graphics/knight_black.png').convert_alpha()
        }

        self.image = images[self.color]
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(bottomleft=self.pos_to_pixel())

class Bishop(Piece):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__(color, pos)
        
        images = {
            'white' : pygame.image.load('graphics/bishop_white.png').convert_alpha(),
            'black' : pygame.image.load('graphics/bishop_black.png').convert_alpha()
        }

        self.image = images[self.color]
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(bottomleft=self.pos_to_pixel())

class Rook(Piece):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__(color, pos)
        
        images = {
            'white' : pygame.image.load('graphics/rook_white.png').convert_alpha(),
            'black' : pygame.image.load('graphics/rook_black.png').convert_alpha()
        }

        self.image = images[self.color]
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(bottomleft=self.pos_to_pixel())

class Queen(Piece):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__(color, pos)
        
        images = {
            'white' : pygame.image.load('graphics/queen_white.png').convert_alpha(),
            'black' : pygame.image.load('graphics/queen_black.png').convert_alpha()
        }

        self.image = images[self.color]
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(bottomleft=self.pos_to_pixel())

class King(Piece):

    def __init__(self, color: str, pos: tuple[int]):
        super().__init__(color, pos)
        
        images = {
            'white' : pygame.image.load('graphics/king_white.png').convert_alpha(),
            'black' : pygame.image.load('graphics/king_black.png').convert_alpha()
        }

        self.image = images[self.color]
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect(bottomleft=self.pos_to_pixel())
