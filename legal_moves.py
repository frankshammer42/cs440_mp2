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
        exit("inpossible initial_position from legal_moves")
    direct_pos = (initial_position[0], initial_position[1]+forward_direction)
    right_diag_pos = (initial_position[0]+1, initial_position[1]+forward_direction)
    left_diag_pos = (initial_position[0]-1, initial_position+forward_direction)
    ret_list = []
    if in_board(len(configuration.chess_board), direct_pos) and configuration.chess_board[direct_pos[0]][direct_pos[1]]!=side:
        ret_list.append(direct_pos)
    if in_board(len(configuration.chess_board), right_diag_pos) and configuration.chess_board[right_diag_pos[0]][right_diag_pos[1]]!=side:
        ret_list.append(right_diag_pos)
    if in_board(len(configuration.chess_board), left_diag_pos) and configuration.chess_board[left_diag_pos[0]][left_diag_pos[1]]!=side:
        ret_list.append(left_diag_pos)
    return ret_list
