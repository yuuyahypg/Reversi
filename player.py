import ai

class Human():
    """
    human class

    Members:

        color   --human's color(black or white)
        currentBoard    --current board data
    """
    def __init__(self, gui, color="black"):
        self.gui = gui
        self.color = color

    def set_current_board(self, board):
        self.currentBoard = board

    def move(self):
        """
        get move using gui to handle mouse
        """
        valid_moves = self.currentBoard.get_selectable_index(self.color)
        while True:
            move = self.gui.get_mouse_input()
            if move in valid_moves:
                break
            elif move == (-1, -1):
                return 0, None
        self.currentBoard.select(move, self.color)
        return 0, self.currentBoard

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

    def move(self):
        return self.ai.eval(self.currentBoard, self.color)
