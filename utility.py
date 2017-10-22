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
    if configuration[row][col] != 0:
        return True 
    else:
        False


def in_board(position_to_check, configuration):
    row_size = len(configuration)
    col_size = len(configuration[0])
    row, col = position_to_check
    if row < row_size and 0 <= col_size > col >= 0:
        return True
    else:
        return False


def exactly_two_surroudning(center_color, positions_to_check, configuration):
    same_color_count = 0
    for position in positions_to_check:
        row, col = position
        if configuration[row][col] == center_color:
            same_color_count += 1
    if same_color_count == 2:
        return True
    else:
        return False


def isGoal(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == '0':
                return False
    return True
