from config import BLACK, WHITE, EMPTY
from copy import deepcopy

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
        self.valid_pos = []

    def __getitem__(self, i, j):
        return self.board[i][j]

    def check_reversible(self, index):
        pass

    def lookup(self, row, column, color):
        """
        search for possible positions for each direction
        """
        if color == BLACK:
            other = WHITE
        else:
            other = BLACK

        places = []

        if (row < 0 or row > 7 or column < 0 or column > 7):
            return places

        # For each direction search for possible positions to put a piece.

        # north
        i = row - 1
        if (i >= 0 and self.board[i][column] == other):
            i = i - 1
            while (i >= 0 and self.board[i][column] == other):
                i = i - 1
            if (i >= 0 and self.board[i][column] == 0):
                places = places + [(i, column)]

        # northeast
        i = row - 1
        j = column + 1
        if (i >= 0 and j < 8 and self.board[i][j] == other):
            i = i - 1
            j = j + 1
            while (i >= 0 and j < 8 and self.board[i][j] == other):
                i = i - 1
                j = j + 1
            if (i >= 0 and j < 8 and self.board[i][j] == 0):
                places = places + [(i, j)]

        # east
        j = column + 1
        if (j < 8 and self.board[row][j] == other):
            j = j + 1
            while (j < 8 and self.board[row][j] == other):
                j = j + 1
            if (j < 8 and self.board[row][j] == 0):
                places = places + [(row, j)]

        # southeast
        i = row + 1
        j = column + 1
        if (i < 8 and j < 8 and self.board[i][j] == other):
            i = i + 1
            j = j + 1
            while (i < 8 and j < 8 and self.board[i][j] == other):
                i = i + 1
                j = j + 1
            if (i < 8 and j < 8 and self.board[i][j] == 0):
                places = places + [(i, j)]

        # south
        i = row + 1
        if (i < 8 and self.board[i][column] == other):
            i = i + 1
            while (i < 8 and self.board[i][column] == other):
                i = i + 1
            if (i < 8 and self.board[i][column] == 0):
                places = places + [(i, column)]

        # southwest
        i = row + 1
        j = column - 1
        if (i < 8 and j >= 0 and self.board[i][j] == other):
            i = i + 1
            j = j - 1
            while (i < 8 and j >= 0 and self.board[i][j] == other):
                i = i + 1
                j = j - 1
            if (i < 8 and j >= 0 and self.board[i][j] == 0):
                places = places + [(i, j)]

        # west
        j = column - 1
        if (j >= 0 and self.board[row][j] == other):
            j = j - 1
            while (j >= 0 and self.board[row][j] == other):
                j = j - 1
            if (j >= 0 and self.board[row][j] == 0):
                places = places + [(row, j)]

        # northwest
        i = row - 1
        j = column - 1
        if (i >= 0 and j >= 0 and self.board[i][j] == other):
            i = i - 1
            j = j - 1
            while (i >= 0 and j >= 0 and self.board[i][j] == other):
                i = i - 1
                j = j - 1
            if (i >= 0 and j >= 0 and self.board[i][j] == 0):
                places = places + [(i, j)]

        return places

    def get_selectable_index(self, color):
        pos_list = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    pos_list = pos_list + self.lookup(i, j, color)

        pos_list = list(set(pos_list))
        self.valid_pos = pos_list
        return pos_list

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
            return True

        if self.get_selectable_index(BLACK) == [] and self.get_selectable_index(WHITE) == []:
            return True

        return False

    def select(self, move, color):
        if move in self.valid_pos:
            self.board[move[0]][move[1]] = color
            for i in range(1, 9):
                self.flip(i, move, color)

    def flip(self, direction, position, color):
        """
        Flips (capturates) the pieces of the given color in the given direction
        (1=North,2=Northeast...) from position.
        """

        if direction == 1:
            # north
            row_inc = -1
            col_inc = 0
        elif direction == 2:
            # northeast
            row_inc = -1
            col_inc = 1
        elif direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        elif direction == 4:
            # southeast
            row_inc = 1
            col_inc = 1
        elif direction == 5:
            # south
            row_inc = 1
            col_inc = 0
        elif direction == 6:
            # southwest
            row_inc = 1
            col_inc = -1
        elif direction == 7:
            # west
            row_inc = 0
            col_inc = -1
        elif direction == 8:
            # northwest
            row_inc = -1
            col_inc = -1

        places = []     # pieces to flip
        i = position[0] + row_inc
        j = position[1] + col_inc

        if color == WHITE:
            other = BLACK
        else:
            other = WHITE

        if i in range(8) and j in range(8) and self.board[i][j] == other:
            # assures there is at least one piece to flip
            places = places + [(i, j)]
            i = i + row_inc
            j = j + col_inc
            while i in range(8) and j in range(8) and self.board[i][j] == other:
                # search for more pieces to flip
                places = places + [(i, j)]
                i = i + row_inc
                j = j + col_inc
            if i in range(8) and j in range(8) and self.board[i][j] == color:
                # found a piece of the right color to flip the pieces between
                for pos in places:
                    # flips
                    self.board[pos[0]][pos[1]] = color

    def next_state(self, color):
        """
        generator function
        """
        valid_pos = self.get_selectable_index(color)
        for move in valid_pos:
            newBoard = deepcopy(self)
            newBoard.apply_move(move, color)
            yield newBoard

    def undo(self):
        pass
