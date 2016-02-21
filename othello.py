#!/usr/bin/env python

import board
import ui

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
        pass

    def restart(self):
        pass

def main():
    game = Othello()
    game.start()

if __name__ == '__main__':
    main()
