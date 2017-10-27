import time
import utility
from puzzle_object import Puzzle
import copy
import random

def full_configuration(puzzle):
    for i in range(len(puzzle.configuration)):
        for j in range(len(puzzle.configuration[0])):
            if puzzle.configuration[i][j] == 0:
                return False
    return True

def goal_configuration(configuration, blank_pos):
    num_color_around = 0
    for a in range(len(blank_pos)):
        i = blank_pos[a][0]
        j = blank_pos[a][1]
        color = configuration[i][j]
        if color != 0:
            top_pos = (i, j-1)
            left_pos = (i-1, j)
            right_pos = (i+1, j)
            bot_pos = (i, j+1)
            if utility.in_board(top_pos, configuration):
                if configuration[i][j] == configuration[i][j-1]:
                    num_color_around += 1
            if utility.in_board(left_pos, configuration):
                if configuration[i][j] == configuration[i-1][j]:
                    num_color_around += 1
            if utility.in_board(right_pos, configuration):
                if configuration[i][j] == configuration[i+1][j]:
                    num_color_around += 1
            if utility.in_board(bot_pos, configuration):
                if configuration[i][j] == configuration[i][j+1]:
                    num_color_around += 1
            if num_color_around != 2:
                return False
        num_color_around = 0
    return True

def satisfy_constrain(configuration):
    num_color_around = 0
    valid_diff_color = 0
    for i in range(len(configuration)):
        for j in range(len(configuration[0])):
            color = configuration[i][j]
            if color != 0:
                top_pos = (i, j-1)
                left_pos = (i-1, j)
                right_pos = (i+1, j)
                bot_pos = (i, j+1)
                if utility.in_board(top_pos, configuration):
                    if color == configuration[i][j-1]:
                        num_color_around += 1
                    if configuration[i][j-1] != 0 and color != configuration[i][j-1]:
                        valid_diff_color += 1
                if utility.in_board(left_pos, configuration):
                    if color == configuration[i-1][j]:
                        num_color_around += 1
                    if configuration[i-1][j] != 0 and color != configuration[i-1][j]:
                        valid_diff_color += 1
                if utility.in_board(right_pos, configuration):
                    if color == configuration[i+1][j]:
                        num_color_around += 1
                    if configuration[i+1][j] != 0 and color != configuration[i+1][j]:
                        valid_diff_color += 1
                if utility.in_board(bot_pos, configuration):
                    if color == configuration[i][j+1]:
                        num_color_around += 1
                    if configuration[i][j+1] != 0 and color != configuration[i][j+1]:
                        valid_diff_color += 1
                if num_color_around > 2:
                    return False
                if i == 0 or j == 0 or i == len(configuration) or j == len(configuration):
                    if valid_diff_color == 3:
                        return False
                else:
                    if valid_diff_color == 4:
                        return False
            num_color_around = 0
            valid_diff_color = 0
    return True


def actual_dumb(puzzle):
    puzzle_arr = []
    puzzle_arr.append(puzzle)
    color_dict = puzzle.color_dict
    start_blank_pos = puzzle.blank_pos
    while len(puzzle_arr):
        curr_puzzle = puzzle_arr.pop()


        #if full_configuration(curr_puzzle):
            #if goal_configuration(curr_puzzle.configuration):
                #return curr_puzzle
        next_color_pos = curr_puzzle.blank_pos[0]
        #curr_puzzle.blank_pos.remove(next_color_pos)
        for i in range(len(curr_puzzle.color_dict)):
            new_configuration = copy.deepcopy(curr_puzzle.configuration)
            color_to_fill = list(color_dict.keys())[i]
            new_configuration[next_color_pos[0]][next_color_pos[1]] = color_to_fill
            new_blank_pos = copy.deepcopy(curr_puzzle.blank_pos)
            new_blank_pos.remove(next_color_pos)
            if satisfy_constrain(new_configuration):
                new_puzzle = Puzzle(new_configuration, curr_puzzle.color_dict, new_blank_pos)
                if full_configuration(new_puzzle):
                    utility.print_configuration(new_puzzle.configuration)
                    print '\n'
                    if goal_configuration(new_puzzle.configuration, start_blank_pos):
                        return new_puzzle
                else:
                    puzzle_arr.append(new_puzzle)


def main():
    ret_matrix, color_position, empty_position = utility.read_puzzle("puzzle1.txt")
    p = Puzzle(ret_matrix, color_position, empty_position)

    start_time = time.time()

    solution = actual_dumb(p)
    if solution == None:
        print "No fukcing solution"
    else:
        utility.print_configuration(solution.configuration)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
