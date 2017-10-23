class Puzzle(object):
    def __init__(self, configuration, color_dict, blank_pos):
        self.configuration = configuration
        self.color_dict = color_dict
        self.blank_pos = blank_pos
        self.curr_pos = color_dict[list(color_dict.keys())[0]][0]

    def fill_color(self, pos, color):
        self.blank_pos.remove(pos)
        self.configuration[pos[0]][pos[1]] = color
        self.curr_pos = pos
        if pos in self.color_dic[color]:
            self.color_dict.remove(color)

    def is_source(self, pos, color):
        if pos in self.color_dict[color]:
            return True
        return False
