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
            cp = puzzle.curr_pos

            top_pos = (cp[0], cp[1]-1)
            left_pos = (cp[0]-1, cp[1])
            right_pos = (cp[0]+1, cp[1])
            bottom_pos = (cp[0], cp[1]+1)

            


            #check source
            if (utility.isSource()):

            #check constrain

                #satisfied -> fill -> append


    return null
