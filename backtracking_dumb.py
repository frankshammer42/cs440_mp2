import utility
from puzzle_object import puzzle

def backtracking_dumb(puzzle):    #gameObject puzzle

    puzzle_arr = []

    puzzle_arr.append(puzzle)

    while puzzle_arr.length():
        cur_puzzle = puzzle_arr.pop()
        if (utility.isGoal(cur_puzzle)):
            return cur_puzzle
        else:
            #get filtered puzzles: on gameboard & not fillled
            cp = cur_puzzle.curr_pos

            top_pos = (cp[0], cp[1]-1)
            left_pos = (cp[0]-1, cp[1])
            right_pos = (cp[0]+1, cp[1])
            bottom_pos = (cp[0], cp[1]+1)

            tmp = []

            if (utility.in_board(top_pos, cur_puzzle.configuration) and not utility.occupied(top_pos, cur_puzzle.configuration)):
                tmp.append(top_pos)
            if (utility.in_board(left_pos, cur_puzzle.configuration) and not utility.occupied(left_pos, cur_puzzle.configuration)):
                tmp.append(left_pos) 
            if (utility.in_board(right_pos, cur_puzzle.configuration) and not utility.occupied(right_pos, cur_puzzle.configuration)):
                tmp.append(right_pos)
            if (utility.in_board(bottom_pos, cur_puzzle.configuration) and not utility.occupied(bottom_pos, cur_puzzle.configuration)):
                tmp.append(bottom_pos)

            color = cur_puzzle.configuration[cp[0],cp[1]]
            #check source
            for pos in tmp:
                if (cur_puzzle.is_source(pos, color)):
                    if (cur_puzzle.exact_n_surrounding(color, pos, cur_puzzle.configuration, 2)):
                        new_puzzle = Puzzle(cur_puzzle.configuration, cur_puzzle.color_dic, cur_puzzle.blank_pos)
                        new_puzzle.fill_color(pos, color)
                        puzzle_arr.append(new_puzzle)
                else:
                    if (cur_puzzle.exact_n_surrounding(color, pos, cur_puzzle.configuration, 1)):
                        new_puzzle = Puzzle(cur_puzzle.configuration, cur_puzzle.color_dic, cur_puzzle.blank_pos)
                        new_puzzle.fill_color(pos, color)
                        puzzle_arr.append(new_puzzle)

    return None

def main():
    ret_matrix, color_position, empty_position = utility.read_puzzle("puzzle1.txt");
    p = Puzzle(ret_matrix, color_position, empty_position)
    solution = backtracking_dumb(p)
    utility.print_configuration(solution.configuration)

if __name__ == 'main':
    main()
