''' Advent of Code 2023
    Day 4: Scratchcards
    https://adventofcode.com/2023/day/4
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''
import re

from timeit import default_timer

line_pattern = 'Card\s+(?P<card_id>\d+)\:\s+'
line_pattern += '(?P<winning_numbers>[\d\s]+)'
line_pattern += '\s\|\s+'
line_pattern += '(?P<your_numbers>[\d\s]+)'

LINE_PATTERN = re.compile(line_pattern)
SPLIT_PATTERN = re.compile('\s+')

class Solver(object):

    def __init__(self, filepath:str):
        self.filepath = filepath
        self.points = 0
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def process_input_line(self, input_line:str):
        line = LINE_PATTERN.search(input_line)
        winning_numbers = set(re.split(SPLIT_PATTERN, line.group('winning_numbers')))
        your_numbers = set(re.split(SPLIT_PATTERN, line.group('your_numbers')))

        your_winning_numbers = len(your_numbers & winning_numbers)

        if (your_winning_numbers) == 0:
            return

        self.points += 2 ** (your_winning_numbers - 1) 

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        return self.points

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
    assert(solve('test_01.txt', part=1) == 13)
    assert(solve('puzzle_input.txt', part=1) == 20107)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('puzzle_input.txt', part=1))
