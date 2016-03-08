#!/usr/bin/env python
# -*- coding: utf-8 -*-

import board
import ui
import pygame
from pygame.locals import *
import player
from config import BLACK, WHITE, EMPTY, HUMAN, COMPUTER
from copy import deepcopy

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
        self.stack = []

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
        self.stack.append(deepcopy(self.board))
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

            selectable_index = self.board.get_selectable_index(self.now_playing.color)
            if selectable_index != []:

                #人間の番なら置ける場所をガイドする
                #if isinstance(self.now_playing, player.Human):
                #    self.gui.guide_screen(selectable_index)

                score, tmp = self.now_playing.move()
                if tmp != None:
                    self.board = tmp
                    self.stack.append(deepcopy(tmp))
                    self.now_playing, self.other_player = self.other_player, self.now_playing
                else:
                    self.stack.pop()
                    self.stack.pop()
                    self.board = deepcopy(self.stack[len(self.stack)-1])
                stone_lst = self.board.count()
                self.gui.update_screen(self.board.board, stone_lst[0], stone_lst[1])
            else:
                self.now_playing, self.other_player = self.other_player, self.now_playing


        self.wait()
        self.gui.show_winner(winner)
        self.wait()
        self.restart()

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    return

    def restart(self):
        self.board = board.Board()
        self.set_options()
        self.start()

def main():
    game = Othello()
    game.start()

if __name__ == '__main__':
    main()
