import numpy as np


class Node:

    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.parent = None
        self.children = []
        self.value = 0

    def set_parent(self, parent_node):
        self.parent = parent_node

    def add_child(self, child):
        self.children.append(child)

    def set_value(self, value):
        self.value = value

    def print_board(self):
        board_to_print = np.array(self.chess_board)
        print board_to_print

    def get_minimax_value(self, min_or_max):
        if len(self.children) != 0:
            # We need min value
            if min_or_max == 0:
                temp_min = 9999999
                for node in self.children:
                    if node.value < temp_min:
                        temp_min = node.value
                self.set_value(temp_min)
                # print self.value
            else:
                temp_max = 0
                for node in self.children:
                    if node.value > temp_max:
                        temp_max = node.value
                self.set_value(temp_max)
                # print self.value


    def get_minimax_value_alpha(self, alpha):
        if len(self.children) != 0:
            temp_min = 99999
            for node in self.children:
                if node.value < alpha:
                    self.set_value(node.value)
                    return alpha
                else:
                    if node.value < temp_min:
                        temp_min = node.value
            if temp_min > alpha:
                alpha = temp_min
                self.set_value(alpha)
                return alpha


    def get_miminmax_value_beta(self, beta):
        if len(self.children) != 0:
            temp_max = 0
            for node in self.children:
                if node.value > beta:
                    self.set_value(node.value)
                    return beta
                else:
                    if node.value > temp_max:
                        temp_max = node.value
            if temp_max < beta:
                beta = temp_max
                self.set_value(beta)
                return beta










