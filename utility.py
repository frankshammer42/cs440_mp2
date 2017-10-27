import numpy as np
from collections import OrderedDict


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
    if row < row_size and row >=0 and col < col_size and col >= 0:
        return True
    else:
        return False


def has_filled_surroudings(configuration, position_tocheck):
    row, col = position_tocheck
    legal_positions = get_legal_positions(row, col, configuration)
    for position in legal_positions:
        pos_x, pos_y = position
        if configuration[pos_x][pos_y] == 0:
            return False
    return True


def no_dst_in_surroudings(configuration, position_to_check, color, color_dict):
    dst = color_dict[color][1]
    row, col = position_to_check
    legal_positions = get_legal_positions(row, col, configuration)
    if dst not in legal_positions:
        # print position_to_check
        # print print_configuration(configuration)
        # print "-------------------"
        return True
    else:
        return False


def forward_checking(configuration, color_dict):
    rows = len(configuration)
    cols = len(configuration[0])
    colors_to_check = list(color_dict.keys())
    for i in range(rows):
        for j in range(cols):
            if configuration[i][j] == 0:
                available_color = 0
                position_to_check = (i,j)
                for color in colors_to_check:
                    if has_filled_surroudings(configuration, position_to_check):
                        if exact_n_surrounding(color, position_to_check, configuration, 2) or exact_n_surrounding(color, position_to_check, configuration, 1):
                            available_color += 1
                    else:
                        available_color += 1
                if available_color == 0:
                    # print_configuration(configuration)
                    # print position_to_check
                    # print colors_to_check
                    # print "----------------------"
                    return False
    return True



def exact_n_surrounding(center_color, position_to_check, configuration, n):
    same_color_count = 0
    row, col = position_to_check

    tmp = get_legal_positions(row, col, configuration)
    for position in tmp:
        row, col = position
        if configuration[row][col] == center_color:
            same_color_count += 1

    if same_color_count == n:
        return True
    else:
        return False


def sort_dict_by_manhatan(color_dict):
    sorted_color_dict = OrderedDict(sorted(color_dict.items(), reverse=True, key=lambda x: abs(x[1][0][0]-x[1][1][0]) + abs(x[1][0][1]-x[1][1][1])))
    return sorted_color_dict


def get_filled_neighbors_number(color_dict, center_position, configuration):
    center_row, center_col = center_position
    legal_neighbors = get_legal_positions(center_row, center_col, configuration)
    result = 0
    for neighbor in legal_neighbors:
        neighbor_x, neighbor_y = neighbor
        if configuration[neighbor_x][neighbor_y] != 0:
            result += 1
    return result


def check_zigzag_neighbors(color_dict, center_position, configuration):
    center_row, center_col = center_position

    center_neighbors = get_filled_neighbors(center_row, center_col, configuration)
    # print center_neighbors
    neighbors_to_check = []
    for neighbor in center_neighbors:
        neighbor_number = get_filled_neighbors_number(color_dict, neighbor, configuration)
        if neighbor_number == 4:
            neighbors_to_check.append(neighbor)
    # print center_position
    # print neighbors_to_check
    # print_configuration(configuration)
    # print "------------"
    for neighbor_to_check in neighbors_to_check:
        to_check_x, to_check_y = neighbor_to_check
        neighbor_color = configuration[to_check_x][to_check_y]
        if not exact_n_surrounding(neighbor_color, neighbor_to_check, configuration, 1) and not exact_n_surrounding(neighbor_color, neighbor_to_check, configuration, 2):
            # print neighbor_to_check
            # print_configuration(configuration)
            # print "---------------------------------"
            return False
    return True













def get_filled_neighbors(row, col, configuration):
    filled_neighbors = []
    legal_neighbors = get_legal_positions(row, col, configuration)
    for neighbor in legal_neighbors:
        neighbor_row, neighbor_col = neighbor
        if configuration[neighbor_row][neighbor_col] != 0:
            filled_neighbors.append(neighbor)
    return filled_neighbors









def get_legal_positions(row, col, configuration):
    top_pos = (row, col - 1)
    left_pos = (row - 1, col)
    right_pos = (row + 1, col)
    bottom_pos = (row, col + 1)
    tmp = []
    if (in_board(top_pos, configuration)):
        tmp.append(top_pos)
    if (in_board(left_pos, configuration)):
        tmp.append(left_pos)
    if (in_board(right_pos, configuration)):
        tmp.append(right_pos)
    if (in_board(bottom_pos, configuration)):
        tmp.append(bottom_pos)
    return tmp


def isGoal(configuration):
    for i in range(len(configuration)):
        for j in range(len(configuration[0])):
            if configuration[i][j] == 0:
                return False
    return True
