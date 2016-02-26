from config import BLACK, WHITE, EMPTY

class Board():
    """
    board class

    Members:

        board    --board data (white:2, black:1, empty:0)
    """
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.board[3][3] = self.board[4][4] = WHITE
        self.board[3][4] = self.board[4][3] = BLACK

    def check_reversible(self, index):
        pass

    def get_selectable_index(self, color):
        pass

    def count(self):
        black = 0
        white = 0

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == BLACK:
                    black += 1
                elif self.board[i][j] == WHITE:
                    white += 1

        return [black, white]

    def is_ended(self):
        num_list = self.count()
        if num_list[0] == 0 or num_list[1] == 0 or num_list[0] + num_list[1] == 64:
            return True:

        if self.get_selectable_index(BLACK) == [] and self.get_selectable_index(WHITE) == []
            return True:

        return False

    def select(self, index):
        pass

    def undo(self):
        pass

    def print(self):
        for i in range(8):
            print(self.board[i])
