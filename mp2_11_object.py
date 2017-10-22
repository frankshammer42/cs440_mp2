class puzzle_obj(object):
    def __init__(self, puzzle, color_dic, blank_pos):
        self.puzzle = puzzle
        self.color_dic = color_dic
        self.blank_pos = blank_pos
        self.curr_pos = color_dic[list(color_dic.keys())[0]][0]

    def fill_color(self, pos, color):
        self.blank_pos.remove(pos)
        self.puzzle[pos[0]][pos[1]] = color
        self.curr_pos = pos
        if pos in self.color_dic[color]:
            self.color_dict.remove(color)
