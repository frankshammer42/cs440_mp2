from GameNode import Node
import copy
import numpy as np
import random

def in_board(configuration_size, position):
    row, col = position
    if row>=0 and row<configuration_size and col>=0 and col<configuration_size:
        return True
    return False


def legal_moves(configuration, initial_position):
    side = configuration[initial_position[0]][initial_position[1]]
    forward_direction = 0
    if side == 'B':
        forward_direction = 1
    elif side == 'W':
        forward_direction = -1
    else:
        exit("impossible initial_position from legal_moves")
    direct_pos = (initial_position[0] + forward_direction, initial_position[1])
    right_diag_pos = (initial_position[0]+ forward_direction, initial_position[1]+1)
    left_diag_pos = (initial_position[0] + forward_direction, initial_position[1]-1)
    ret_list = []
    if in_board(len(configuration), direct_pos) and configuration[direct_pos[0]][direct_pos[1]]==0:
        ret_list.append(direct_pos)
    if in_board(len(configuration), right_diag_pos) and configuration[right_diag_pos[0]][right_diag_pos[1]]!=side:
        ret_list.append(right_diag_pos)
    if in_board(len(configuration), left_diag_pos) and configuration[left_diag_pos[0]][left_diag_pos[1]]!=side:
        ret_list.append(left_diag_pos)
    # print np.array(configuration)
    # print initial_position
    # print ret_list
    # print "------------------------------"
    return ret_list


def move_chess_piece(start_pos, end_pos, parentNode):
    parent_board = parentNode.chess_board
    child_board = copy.deepcopy(parent_board)
    player = parentNode.chess_board[start_pos[0]][start_pos[1]]
    child_board[start_pos[0]][start_pos[1]] = 0
    child_board[end_pos[0]][end_pos[1]] = player
    childNode = Node(child_board)
    parentNode.add_child(childNode)
    childNode.set_parent(parentNode)
    return childNode


def get_minimax_children(node_to_expand, side):
    """
    :param node_to_expand: The parent node
    :param side: which turn it is
    :return: a list of child nodes
    """
    node_board = node_to_expand.chess_board
    newly_generated_children = []
    for i in range(8):
        for j in range(8):
            if node_board[i][j] == side:
                moves = legal_moves(node_board, (i,j))
                for move in moves:
                    child_node = move_chess_piece((i,j),move, node_to_expand)
                    newly_generated_children.append(child_node)
    return newly_generated_children


def get_alpha_children(node_to_expand, side, alpha, heuristic_function):
    node_board = node_to_expand.chess_board
    newly_generated_children = []
    alpha_break = False
    temp_min = 9999999
    for i in range(8):
        for j in range(8):
            if not alpha_break:
                if node_board[i][j] == side:
                    moves = legal_moves(node_board, (i,j))
                    for move in moves:
                        child_node = move_chess_piece((i,j),move, node_to_expand)
                        heuristic_value = heuristic_function(side, child_node)
                        #print "alpha value:" + str(heuristic_value)
                        if heuristic_value < alpha:
                            newly_generated_children.append(child_node)
                            alpha_break = True
                            break
                        else:
                            if heuristic_value < temp_min:
                                temp_min = heuristic_value
                            newly_generated_children.append(child_node)
    return newly_generated_children, temp_min


def get_beta_children(node_to_expand, side, beta, heuristic_function):
    node_board = node_to_expand.chess_board
    newly_generated_children = []
    beta_break = False
    temp_max = 0
    for i in range(8):
        for j in range(8):
            if not beta_break:
                if node_board[i][j] == side:
                    moves = legal_moves(node_board, (i,j))
                    for move in moves:
                        child_node = move_chess_piece((i,j),move, node_to_expand)
                        heuristic_value = heuristic_function(side, child_node)
                        #print "beta value:" + str(heuristic_value)
                        if heuristic_value > beta:
                            newly_generated_children.append(child_node)
                            beta_break = True
                            break
                        else:
                            if heuristic_value > temp_max:
                                temp_max = heuristic_value
                            newly_generated_children.append(child_node)
    return newly_generated_children, temp_max


def create_init_board():
    chess_board = []
    for i in range(0,8):
        chess_board.append([])
    for i in range(0,8):
        for j in range(0,8):
            chess_board[i].append(0)
    for i in range(0,2):
        for j in range(0,8):
            chess_board[i][j] = 'B'
    for i in range(6,8):
        for j in range(0,8):
            chess_board[i][j] = 'W'
    return chess_board


def offensive_heuristic(player, node):
    chessboard = node.chess_board
    remaining_pieces = 0
    opponent = ""
    if (player == "B"):
        opponent = "W"
    else:
        opponent = "B"
    for i in range(8):
        for j in range(8):
            if (chessboard[i][j] == opponent):
                remaining_pieces += 1
    return 2*(30 - remaining_pieces) + random.random()


def defensive_heuristic(player, node):
    chessboard = node.chess_board
    remaining_pieces = 0
    for i in range(8):
        for j in range(8):
            if (chessboard[i][j] == player):
                remaining_pieces += 1
    return 2*(remaining_pieces) + random.random()


def calculate_depth_n(dict, heuristic, player, n):
    layer = dict[n]
    for node in layer:
        # apply_heuristic(node, off_or_def, player)
        heuristic_value = heuristic(player, node)
        node.set_value(heuristic_value)


def apply_heuristic(node, off_or_def, player): #off is 1, def is 0
    if off_or_def == 1:
        node.set_value(offensive_heuristic(player, node.chess_board))
    elif off_or_def == 0:
        node.set_value(defensive_heuristic(player, node.chess_board))
    else:
        exit("apply_heuristic is wrong")


def populate_value(dict, side, depth):
    max_or_min = 0
    if side == 'B':
        max_or_min = 1
    elif side == 'W':
        max_or_min = 0
    else:
        exit("wrong value from pick_move")
    for i in range(depth-1, -1, -1):
        curr_layer_nodes_list = dict[i]
        for node in curr_layer_nodes_list:
            node.get_minimax_value(max_or_min)
        if max_or_min == 0:
            max_or_min = 1
        else:
            max_or_min = 0


def get_node_by_value(nodes_to_check, value_to_check):
    for node in nodes_to_check:
        if node.value == value_to_check:
            return node
    print "Nothing Found there is bug ufck"
    return None


def goal_chess_board(node):
    b_occur = 0
    w_occur = 0
    for i in range(len(node.chess_board)):
        for j in range(len(node.chess_board[0])):
            if node.chess_board[i][j] == 'B':
                b_occur += 1
            if node.chess_board[i][j] == 'W':
                w_occur += 1
    if b_occur == 0 or w_occur == 0:
        return True
    for i in range(len(node.chess_board)):
        if node.chess_board[0][i] == 'W':
            return True
        if node.chess_board[len(node.chess_board)-1][i] == 'B':
            return True
    return False


def legal_move_and_block_count(initial_pos, chess_board, heuristic_val, player):
    initial_val = chess_board[initial_pos[0]][initial_pos[1]]
    chess_board[initial_pos[0]][initial_pos[1]] = player
    forward_direction = 0
    opponent = ""
    if player == 'B':
        forward_direction = 1
        opponent = "W"
    elif player == 'W':
        forward_direction = -1
        opponent = "B"
    else:
        exit("impossible initial_position from legal_moves")
    direct_pos = (initial_pos[0] + forward_direction, initial_pos[1])
    right_diag_pos = (initial_pos[0] + forward_direction, initial_pos[1]+1)
    left_diag_pos = (initial_pos[0] + forward_direction, initial_pos[1]-1)
    ret_list = []
    if in_board(len(chess_board), direct_pos):
        if chess_board[direct_pos[0]][direct_pos[1]] == 0:
            ret_list.append(direct_pos)
        else:
            if chess_board[direct_pos[0]][direct_pos[1]] == opponent:
                heuristic_val += 1

    if in_board(len(chess_board), right_diag_pos):
        if chess_board[right_diag_pos[0]][right_diag_pos[1]] != player:
            ret_list.append(right_diag_pos)

    if in_board(len(chess_board), left_diag_pos):
        if chess_board[left_diag_pos[0]][left_diag_pos[1]] != player:
            ret_list.append(left_diag_pos)

    chess_board[initial_pos[0]][initial_pos[1]] = initial_val

    return ret_list, heuristic_val


def calculate_block_num(player, node):
    node_initial_pos = []
    chess_board = node.chess_board
    for i in range(len(chess_board)):
        for j in range(len(chess_board[0])):
            if chess_board[i][j] == player:
                node_initial_pos.append((i,j))

    heuristic_val = 0
    for ip in node_initial_pos:
        # print ip
        move_queue = []
        curr_board = copy.deepcopy(chess_board)
        curr_board[ip[0]][ip[1]] = 0
        moves, heuristic_val = legal_move_and_block_count(ip, curr_board, heuristic_val, player)
        move_queue += moves

        while len(move_queue) != 0:
            cur_move = move_queue.pop(0)
            moves, heuristic_val = legal_move_and_block_count(cur_move, curr_board, heuristic_val, player)
            if heuristic_val > 1350:
                return heuristic_val
            move_queue += moves
            # print "cur_move:" + str(cur_move)
            # print moves
    return heuristic_val

def calculate_block_num_defensive(player, node):
    if player == 'B':
        player = 'W'
    else:
        player = 'B'
    node_initial_pos = []
    chess_board = node.chess_board
    for i in range(len(chess_board)):
        for j in range(len(chess_board[0])):
            if chess_board[i][j] == player:
                node_initial_pos.append((i,j))

    heuristic_val = 0
    for ip in node_initial_pos:
        # print ip
        move_queue = []
        curr_board = copy.deepcopy(chess_board)
        curr_board[ip[0]][ip[1]] = 0
        moves, heuristic_val = legal_move_and_block_count(ip, curr_board, heuristic_val, player)
        move_queue += moves

        while len(move_queue) != 0:
            cur_move = move_queue.pop(0)
            moves, heuristic_val = legal_move_and_block_count(cur_move, curr_board, heuristic_val, player)
            if heuristic_val > 1350:
                return heuristic_val
            move_queue += moves
            # print "cur_move:" + str(cur_move)
            # print moves
    return heuristic_val


def get_number_of_captured(board):
    black_number = 0
    white_number = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'B':
                black_number += 1
            if board[i][j] == 'W':
                white_number += 1
    return 16-black_number, 16-white_number



# def test():
#     board = create_init_board()
#     heuristic_val = calculate_block_num('W', board)
#     print heuristic_val
#
#
# test()


































