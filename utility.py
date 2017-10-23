import numpy as np


def read_puzzle(file_name):
    ret_matrix = []
    color_position = {}
    empty_position = []
    with open(file_name, "r+") as f:
        line_count = 0
        for line in f:
            chars = list(line.rstrip())
            temp_array = []
            char_count = 0
            for i in chars:
                if i == '_':
                    temp_array.append(0)
                    empty_position.append((line_count, char_count))
                else:
                    if i in color_position:
                        color_position[i].append((line_count, char_count))
                    else:
                        color_position[i] = [(line_count, char_count)]
                    temp_array.append(i)
                char_count += 1
            line_count += 1
            ret_matrix.append(temp_array)
    return ret_matrix, color_position, empty_position


def print_configuration(configuration):
    array = np.array(configuration)
    print array


def occupied(position_to_check, configuration):
    row, col = position_to_check
    if configuration[row][col] != 0:
        return True 
    else:
        return False


def in_board(position_to_check, configuration):
    row_size = len(configuration)
    col_size = len(configuration[0])
    row, col = position_to_check
    if row < row_size and 0 <= col_size > col >= 0:
        return True
    else:
        return False


def exact_n_surrounding(center_color, position_to_check, configuration, n):
    same_color_count = 0
    row, col = position_to_check

    top_pos = (row, col-1)
    left_pos = (row-1, col)
    right_pos = (row+1, col)
    bottom_pos = (row, col+1)

    tmp = []
    if (in_board(top_pos, configuration) and not occupied(top_pos, configuration)):
        tmp.append(top_pos)
    if (in_board(left_pos, configuration) and not occupied(left_pos, configuration)):
        tmp.append(left_pos) 
    if (in_board(right_pos, configuration) and not occupied(right_pos, configuration)):
        tmp.append(right_pos)
    if (in_board(bottom_pos, configuration) and not occupied(bottom_pos, configuration)):
        tmp.append(bottom_pos)

    print tmp

    for position in tmp:
        row, col = position
        if configuration[row][col] == center_color:
            same_color_count += 1
    print same_color_count
    if same_color_count == n:
        return True
    else:
        return False


def isGoal(configuration):
    for i in range(len(configuration)):
        for j in range(len(configuration[0])):
            if configuration[i][j] == 0:
                return False
    return True
