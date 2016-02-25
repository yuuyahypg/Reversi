#!/usr/bin/env python

import board
import ui
import pygame

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

    def start(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(100)
            break
        pygame.time.wait(1000)
        self.restart()

    def restart(self):
        self.board = board.Board()
        self.start()

def main():
    game = Othello()
    game.start()

if __name__ == '__main__':
    main()
