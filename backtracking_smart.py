import utility
from puzzle_object import Puzzle
import copy
import time

def backtracking_dumb(puzzle):    #gameObject puzzle

    puzzle_arr = []

    puzzle_arr.append(puzzle)

    while len(puzzle_arr):
        cur_puzzle = puzzle_arr.pop()
        if (utility.isGoal(cur_puzzle.configuration)):
            return cur_puzzle
        else:
            #get filtered puzzles: on gameboard & not fillled
            cp = cur_puzzle.curr_pos
            # print cp

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

            color = cur_puzzle.configuration[cp[0]][cp[1]]
            color_dst = cur_puzzle.color_dict[color][1]
            sorted_position = sorted(tmp, key=lambda x:abs(x[0]-color_dst[0]) + abs(x[1]-color_dst[1]))
            sorted_position = list(reversed(sorted_position))

            # sorted_position = (sorted_position)
            # print color
            # print sorted_position
            # print "-----"
            #check source
            for pos in sorted_position:
                if utility.exact_n_surrounding(color, pos, cur_puzzle.configuration, 1) or utility.exact_n_surrounding(color, pos, cur_puzzle.configuration, 2):
                    if utility.exact_n_surrounding(color, pos, cur_puzzle.configuration, 2):
                        if not utility.no_dst_in_surroudings(cur_puzzle.configuration, pos, color, cur_puzzle.color_dict):
                            new_configuration = copy.deepcopy(cur_puzzle.configuration)
                            new_color_dict = copy.deepcopy(cur_puzzle.color_dict)
                            new_puzzle = Puzzle(new_configuration, new_color_dict, cur_puzzle.blank_pos)
                            # new_puzzle = Puzzle(cur_puzzle.configuration, cur_puzzle.color_dict, cur_puzzle.blank_pos)
                            new_puzzle.fill_color(pos, color)
                            new_puzzle.color_dict.pop(color)
                            try:
                                new_puzzle.curr_pos = new_puzzle.color_dict[list(new_puzzle.color_dict.keys())[0]][0]
                            except:
                                print "empty dict"
                            if len(new_puzzle.color_dict) == 0:
                                puzzle_arr.append(new_puzzle)
                                # utility.print_configuration(new_puzzle.configuration)
                                # print "---------------------------"
                            else:
                                if utility.forward_checking(new_puzzle.configuration, new_puzzle.color_dict) and utility.check_zigzag_neighbors(new_puzzle.color_dict, pos, new_puzzle.configuration):
                                    puzzle_arr.append(new_puzzle)
                                    # utility.print_configuration(new_puzzle.configuration)
                                    # print "---------------------------"
                    else:
                        new_configuration = copy.deepcopy(cur_puzzle.configuration)
                        new_color_dict = copy.deepcopy(cur_puzzle.color_dict)
                        if len(new_color_dict) == 0:
                            return None
                        new_puzzle = Puzzle(new_configuration, new_color_dict, cur_puzzle.blank_pos)
                        new_puzzle.fill_color(pos, color)
                        if len(new_puzzle.color_dict) == 0:
                            puzzle_arr.append(new_puzzle)
                            # utility.print_configuration(new_puzzle.configuration)
                            # print "---------------------------"
                        else:
                            if utility.forward_checking(new_puzzle.configuration, new_puzzle.color_dict) and utility.check_zigzag_neighbors(new_puzzle.color_dict, pos, new_puzzle.configuration):
                                puzzle_arr.append(new_puzzle)
                                # utility.print_configuration(new_puzzle.configuration)
                                # print "---------------------------"

    return None

def main():
    ret_matrix, color_position, empty_position = utility.read_puzzle("puzzle3.txt")
    color_position = utility.sort_dict_by_manhatan(color_position)
    p = Puzzle(ret_matrix, color_position, empty_position)
    start_time = time.time()
    solution = backtracking_dumb(p)
    if solution == None:
        print "No fukcing solution"
    else:
        utility.print_configuration(solution.configuration)
    end_time = time.time()
    print end_time - start_time

if __name__ == '__main__':
    main()
