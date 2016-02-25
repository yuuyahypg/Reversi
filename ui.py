import pygame
from pygame.locals import *
from config import BLACK, WHITE, EMPTY, HUMAN, COMPUTER
import os

class GUI():
    """
    othello gui
    """

    def __init__(self):
        """
        initialize pygame and graphics
        """
        pygame.init()
        #colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BACKGROUND = (0, 0, 255)

        # display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20)
        self.BOARD = (120, 40)
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.caption = pygame.display.set_caption("othello")

        #message
        self.BLACK_LAB_POS = (5, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LAB_POS = (560, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Times New Roman", 22)
        self.scoreFont = pygame.font.SysFont("Serif", 58)

        # image files
        self.board_img = pygame.image.load(os.path.join("res", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join("res", "black.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join("res", "white.bmp")).convert()
        self.tip_img = pygame.image.load(os.path.join("res", "empty.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("res", "clear.bmp")).convert()

    def show_options(self):
        """
        show game options
        """
        player1 = HUMAN
        player2 = COMPUTER

        while True:
            break

    def show_winner(self):
        pass

    def decide_player(self):
        pass

    def show_game(self):
        pass

    def put_stone(self, pos, color):
        pass

    def clear_square(self, pos):
        pass

    def get_mouse_input(self):
        while True:
            break

    def update_screen(self, board, blacks, whites):
        pass

    def show_score(self, blackStr, whiteStr):
        pass

    def wait_quit(self):
        """
        wait user to close window
        """
        pass
