# -*- coding: utf-8 -*-

import board
from config import BLACK, WHITE, DEPTH

from copy import deepcopy, copy

class Ai():
    """
    ai class
    """
    def __init__(self):
        pass

    def eval(self, node, color):
        self.color = color
        count = node.count()
        stone_num = count[0] + count[1]
        if 64 - stone_num > DEPTH:
            index, num = self.min_max(node, color, DEPTH)
        else:
            index, num = self.min_max(node, color, 64 - stone_num - 1)
        node.select(index, color)
        return 0, node

    # ミニマックス法
    def min_max(self, node, color, depth):
        if depth == 0:
            return self.max_num(node, color)

        if color == BLACK:
            next_turn = WHITE
        else:
            next_turn = BLACK

        indices = node.get_selectable_index(color)

        best = -100
        best_index = (None, None)
        for index in indices:
            next_node = board.Board()
            next_node = deepcopy(node)
            next_node.select(index, color)
            val_index, val_num = self.min_max(next_node, next_turn, depth - 1)
            print val_num
            if color == self.color and best < val_num:
                best = copy(val_num)
                best_index = deepcopy(index)
            elif best < -val_num:
                best = copy(-val_num)
                best_index = deepcopy(index)

        print "depth", depth
        print "best", best
        if color == self.color:
            return best_index, best
        else:
            return best_index, -best

    # 取れる石の最大値を返す
    def max_num(self, node, color):
        indices = node.get_selectable_index(color)
        best = -100
        best_index = (None, None)

        for index in indices:

            leaf = board.Board()
            leaf = deepcopy(node)
            num = leaf.select(index, color)

            if color == self.color and best < num:
                best = copy(num)
                best_index = deepcopy(index)
            elif best < -num:
                best = copy(-num)
                best_index = deepcopy(index)

        if color == self.color:
            return best_index, best
        else:
            return best_index, -best
