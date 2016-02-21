import pygame
from pygame.locals import *
from config import BLACK, WHITE, EMPTY, HUMAN, COMPUTER

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
