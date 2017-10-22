class puzzle_obj(object):
    def __init__(size, puzzle, color_dic, blank_pos):
        self.size = size
        self.puzzle = puzzle
        self.color_dic = color_dic
        self.blank_pos = blank_pos
        self.curr_pos = color_dic[list(color_dic.keys())[0]][0]
