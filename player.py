import ai

class Human():
    """
    human class

    Members:

        color   --human's color(black or white)
        currentBoard    --current board data
    """
    def __init__(self, color="black"):
        self.color = color

    def set_current_board(self, board):
        self.currentBoard = board

class Computer():
    """
    computer class

    Members:

        color   --computer's color(black or white)
        ai      --ai module (select the best position to put)
        currentBoard    --current board data
    """
    def __init__(self, color="white"):
        self.color = color
        self.ai = ai.Ai()

    def set_current_board(self, board):
        self.currentBoard = board
