class Ai():
    """
    ai class
    """
    def __init__(self):
        pass

    def eval(self, board, color):
        valid_moves = board.get_selectable_index(color)
        board.select(valid_moves[0], color)
        return 0, board
