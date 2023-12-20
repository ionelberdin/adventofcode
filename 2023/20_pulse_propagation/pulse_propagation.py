''' Advent of Code 2023
    Day 20: Pulse Propagation
    https://adventofcode.com/2023/day/20

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from itertools import pairwise

# 0. Functions that are common to both problems

class PulsePropagator(object):

    LINE_PATTERN = re.compile('([^\s]+) \-\> ([\w\,\s]+)')

    def __init__(self, filepath:str):
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)
    
    def process_input_line(self, input_line:str):
        parse_input = self.LINE_PATTERN.search(input_line)
        print(parse_input.group(1), parse_input.group(2))
        # TODO: Continue

# 1. Functions that are specific for problem 1

def solve_part_1(filepath:str, with_hex:bool=False):
    pulse_propagator = PulsePropagator(filepath)
    return 1  # TODO: map correct output

# 2. Functions that are specific for problem 2

def solve_part_2(filepath:str, with_hex:bool=False):
    pulse_propagator = PulsePropagator(filepath)
    return 1  # TODO: map correct output

if __name__ == '__main__':
    # assert(solve_part_1('test_01.txt') == 62)
    # assert(pipe_maze_1('puzzle_input.txt') == 6733)

    print(solve_part_1('test_01.txt'))
