#!/usr/bin/env python

import board
import ui
import pygame
import player
from config import BLACK, WHITE, EMPTY, HUMAN, COMPUTER

class Othello():
    """
    brain class of othello game

    Members:

        board   --othello board module
        gui     --gui module
    """
    def __init__(self):
        self.board = board.Board()
        self.gui = ui.GUI()
        self.set_options()

    def set_options(self):
        """
        set up playres
        """
        player1, player2 = self.gui.show_options()
        if player1 == HUMAN:
            self.now_playing = player.Human(self.gui, BLACK)
        else:
            self.now_playing = player.Computer(BLACK)
        if player2 == HUMAN:
            self.other_player = player.Human(self.gui, WHITE)
        else:
            self.other_player = player.Computer(WHITE)

        self.gui.show_game()
        self.gui.update_screen(self.board.board, 2, 2)

    def start(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(100)
            if self.board.is_ended():
                stone_lst = self.board.count()
                if stone_lst[0] > stone_lst[1]:
                    winner = BLACK
                elif stone_lst[1] > stone_lst[0]:
                    winner = WHITE
                else:
                    winner = None
                break
            self.now_playing.set_current_board(self.board)

            if self.board.get_selectable_index(self.now_playing.color) != []:
                score, self.board = self.now_playing.move()
                stone_lst = self.board.count()
                self.gui.update_screen(self.board.board, stone_lst[0], stone_lst[1])

            self.now_playing, self.other_player = self.other_player, self.now_playing
        self.gui.show_winner(winner)
        pygame.time.wait(1000)
        self.restart()

    def restart(self):
        self.board = board.Board()
        self.set_options()
        self.start()

def main():
    game = Othello()
    game.start()

if __name__ == '__main__':
    main()
