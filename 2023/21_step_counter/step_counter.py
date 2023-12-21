''' Advent of Code 2023
    Day 21: Step Counter
    https://adventofcode.com/2023/day/21

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

# 0. Functions that are common to both problems
class GardenPlot(object):
    
    garden_map = {}

    def __init__(self, position):
        self.position = position
        self.neighbour_plots = set()

    def add_neighbour_plot(self, neighbour_plot):
        self.neighbour_plots.add(neighbour_plot)

    def get_neighbour_plots(self):
        for neighbour_plot in self.neighbour_plots:
            yield neighbour_plot
    
    @property
    def number_of_neighbour_plots(self):
        return len(self.neighbour_plots)

    @classmethod
    def add_garden_plot(cls, position, garden_plot):
        cls.garden_map[position] = garden_plot
        for position in cls.get_neightbour_positions(position):
            if (neighbour_plot := cls.get_garden_plot_by_position(position)):
                neighbour_plot.add_neighbour_plot(garden_plot)
                garden_plot.add_neighbour_plot(neighbour_plot)

    @classmethod
    def get_garden_plot_by_position(cls, position):
        try:
            return cls.garden_map[position]
        except:
            return None

    @classmethod
    def init_garden_map(cls):
        cls.garden_map = {}

    @classmethod
    def __print__(cls):


    @staticmethod
    def get_neightbour_positions(position):
        delta = [-1, 1]
        row_number, column_number = position
        for row_delta in delta:
            for column_delta in delta:
                yield (row_number + row_delta, column_number + column_delta)

class StepCounter(object):

    def __init__(self, filepath:str):

        self.TYPES = {
            '.': self.add_garden_plot,
            '#': self.add_rock,
            'S': self.add_start
        }

        self.garden_map = []

        with open(filepath, 'r') as f:
            for row_number, input_line in f.readline().strip('\n\s\t'):
                self.garden_map.append([])
                self.process_input_line(input_line, row_number)


    def process_input_line(self, input_line:str, row_number:int):
        for column_number, character in enumerate(input_line):
            position = (row_number, column_number)
            self.add_position[character](position)

# 1. Functions that are specific for part 1

def solve_part_1(filepath:str):
    step_counter = StepCounter(filepath)
    return 1  # TODO: map correct output

# 2. Functions that are specific for part 2


if __name__ == '__main__':
    # assert(solve_part_1('test_01.txt') == 62)
    # assert(pipe_maze_1('puzzle_input.txt') == 6733)

    print(solve_part_1('test_01.txt'))
