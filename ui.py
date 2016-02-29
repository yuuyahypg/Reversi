import pygame
from pygame.locals import *
from config import BLACK, WHITE, EMPTY, HUMAN, COMPUTER
import os
import sys
import time

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
        self.BLUE = (0, 0, 255)

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
        self.font = pygame.font.SysFont(None, 22)
        self.scoreFont = pygame.font.SysFont(None, 58)

        # image files
        self.board_img = pygame.image.load(os.path.join("pic", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join("pic", "black.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join("pic", "white.bmp")).convert()
        self.empty_img = pygame.image.load(os.path.join("pic", "empty.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("pic", "clear.bmp")).convert()

    def show_options(self):
        """
        show game options and returns chosen players
        """
        player1 = HUMAN
        player2 = COMPUTER

        while True:
            self.screen.fill(self.BACKGROUND)

            title_fnt = pygame.font.SysFont(None, 34)
            title = title_fnt.render("Othello", True, self.WHITE)
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=60)

            start_txt = self.font.render("Start", True, self.WHITE)
            start_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2, centery=220)

            player1_txt = self.font.render("First Player", True, self.WHITE)
            player1_pos = player1_txt.get_rect(centerx=self.screen.get_width() / 2, centery=260)

            player2_txt = self.font.render("Second Player", True, self.WHITE)
            player2_pos = player2_txt.get_rect(centerx=self.screen.get_width() / 2, centery=300)

            human_txt = self.font.render("Human", True, self.WHITE)
            comp_txt = self.font.render("Computer", True, self.WHITE)

            self.screen.blit(title, title_pos)
            self.screen.blit(start_txt, start_pos)
            self.screen.blit(player1_txt, player1_pos)
            self.screen.blit(player2_txt, player2_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if start_pos.collidepoint(mouse_x, mouse_y):
                        return (player1, player2)
                    elif player1_pos.collidepoint(mouse_x, mouse_y):
                        player1 = self.choose_player()
                    elif player2_pos.collidepoint(mouse_x, mouse_y):
                        player2 = self.choose_player()

                pygame.display.flip()

    def show_winner(self, player_color):
        self.screen.fill(pygame.Color(0, 0, 0, 50))
        font = pygame.font.SysFont(None, 34)
        if player_color == WHITE:
            message = font.render("White player wins", True, self.WHITE)
        elif player_color == BLACK:
            message = font.render("Black player wins", True, self.BLACK)
        else:
            message = font.render("Tie !", True, self.WHITE)
        self.screen.blit(message, message.get_rect(centerx=self.screen.get_width() / 2, centery=120))
        pygame.display.flip()

    def choose_player(self):
        """
        Ask for a player
        """
        while True:
            self.screen.fill(self.BACKGROUND)

            title_fnt = pygame.font.SysFont(None, 34)
            title = title_fnt.render("Othello", True, self.WHITE)
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=60)

            human_txt = self.font.render("Human", True, self.WHITE)
            human_pos = human_txt.get_rect(centerx=self.screen.get_width() / 2, centery=120)

            comp_txt = self.font.render("Computer", True, self.WHITE)
            comp_pos = comp_txt.get_rect(centerx=self.screen.get_width() / 2, centery=360)

            self.screen.blit(title, title_pos)
            self.screen.blit(human_txt, human_pos)
            self.screen.blit(comp_txt, comp_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if human_pos.collidepoint(mouse_x, mouse_y):
                        return HUMAN
                    elif comp_pos.collidepoint(mouse_x, mouse_y):
                        return COMPUTER

            pygame.display.flip()

    def show_game(self):
        """
        draw initial game screen
        """
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.BACKGROUND)
        self.score_size = 50
        self.score1 = pygame.Surface((self.score_size, self.score_size))
        self.score2 = pygame.Surface((self.score_size, self.score_size))
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.board_img, self.BOARD_POS, self.board_img.get_rect())
        self.put_stone((3, 3), WHITE)
        self.put_stone((4, 4), WHITE)
        self.put_stone((3, 4), BLACK)
        self.put_stone((4, 3), BLACK)
        pygame.display.flip()

    def put_stone(self, pos, color):
        """
        draw pieces in the given position
        """
        pos = (pos[1], pos[0])

        if color == BLACK:
            img = self.black_img
        elif color == WHITE:
            img = self.white_img
        else:
            img = self.empty_img

        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]

        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()

    def clear_square(self, pos):
        """
        draw background image in the given position
        """
        pos = (pos[1], pos[0])

        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]
        self.screen.blit(self.clear_img, (x, y), self.clear_img.get_rect())
        pygame.display.flip()

    def get_mouse_input(self):
        """
        get position clicked by mouse
        """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)

                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

                    # click was out of board, ignores
                    if mouse_x > self.BOARD_SIZE + self.BOARD[0] or \
                       mouse_x < self.BOARD[0] or \
                       mouse_y > self.BOARD_SIZE + self.BOARD[1] or \
                       mouse_y < self.BOARD[1]:
                        continue

                    # find place
                    position = int((mouse_x - self.BOARD[0]) / self.SQUARE_SIZE), \
                               int((mouse_y - self.BOARD[1]) / self.SQUARE_SIZE)

                    # flip orientation
                    position = (position[1], position[0])

                    return position

    def update_screen(self, board, blacks, whites):
        """
        update screen figures
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])

        blacks_str = '%02d ' % int(blacks)
        whites_str = '%02d ' % int(whites)
        self.show_score(blacks_str, whites_str)
        pygame.display.flip()

    def show_score(self, blackStr, whiteStr):
        text = self.scoreFont.render(blackStr, True, self.BLACK, self.BACKGROUND)
        text2 = self.scoreFont.render(whiteStr, True, self.WHITE, self.BACKGROUND)
        self.screen.blit(text, (self.BLACK_LAB_POS[0], self.BLACK_LAB_POS[1] + 40))
        self.screen.blit(text2, (self.WHITE_LAB_POS[0], self.WHITE_LAB_POS[1] + 40))

    def wait_quit(self):
        """
        wait user to close window
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
