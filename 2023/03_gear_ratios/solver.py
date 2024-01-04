''' Advent of Code 2023
    Day 3: Gear Ratios
    https://adventofcode.com/2023/day/3
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from timeit import default_timer

INT_PATTERN = re.compile('\d+')

class Solver(object):

    def __init__(self, filepath:str):
        with open(filepath, 'r') as f:
            for line_number, input_line in enumerate(f.readlines()):
                self.process_input_line(line_number, input_line.strip('\n\s\t'))

    def process_input_line(self, line_number:int, input_line:str):
        numbers = INT_PATTERN.findall(input_line)
        for number in numbers:
            print(line_number, number, input_line.index(number))

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        """ Strategy:
            1. Get the position from all numbers
            2. Get the position of all symbols.
            3. Filter out numbers that don't have a adjoining symbol.
            """
        return None

    def solve_part_2(self):
        return None


def solve(filepath:str, part:int):
    print("Solving part {} with:".format(part), filepath)
    start = default_timer()
    solver = Solver(filepath)
    result = solver.solve(part=part)
    duration = default_timer() - start
    print("Solved in {}s".format(duration))
    print("Result:", result)
    return result


if __name__ == '__main__':
    # assert(solve('test_01.txt', part=1) == 4361)
    # assert(solve('puzzle_input.txt', part=1) == TBD)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('test_01.txt', part=1))
