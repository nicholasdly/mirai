
from src.settings import *
from src.board import Board
from src.pieces import Pawn, Knight, Bishop, Rook, Queen, King

import pygame

def load_fen(pieces: pygame.sprite.Group, fen: str):
    """
    Reads a given FEN string, populating a specified sprite group with relevant pieces.
    """
    row, col = 7, 0
    for c in fen:
        if c == '/':
            row -= 1
            col = 0
        elif c.isnumeric():
            col += 1
        else:
            color = 'white' if c.isupper() else 'black'
            match c.lower():
                case 'p':
                    pieces.add(Pawn(color, (col, row)))
                case 'n':
                    pieces.add(Knight(color, (col, row)))
                case 'b':
                    pieces.add(Bishop(color, (col, row)))
                case 'r':
                    pieces.add(Rook(color, (col, row)))
                case 'q':
                    pieces.add(Queen(color, (col, row)))
                case 'k':
                    pieces.add(King(color, (col, row)))
            col += 1

def run():
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    running = True

    board = pygame.sprite.GroupSingle()
    board.add(Board())

    pieces = pygame.sprite.Group()
    load_fen(pieces, FEN_START)

    while running:
        pygame.display.update()
        clock.tick(FPS)

        board.draw(window)
        pieces.draw(window)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    quit()
