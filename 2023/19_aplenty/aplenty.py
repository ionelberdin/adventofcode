''' Advent of Code 2023
    Day 19: Aplenty
    https://adventofcode.com/2023/day/19

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

def integrate_manhattan_line(points):
    ''' All segments are either horizontal or vertical.
        Hence, integrating them is just adding triangle areas in which:
           * The base is the difference of the coordinates that are not equal.
           * The height is the orthogonal distance of the segment to the origin.
        This is what's done in differential geometry by vectorially multiplying the 
        vector from the coordinate origin to the segment origin by the segment.
        Since all triangle areas are half of the product of their base by their height,
        the division by 2 is left to be done at the end.
        Since the direction of integration is arbitrary, the result could
        be negative, that's why its absolute value is taken.
        And finally, since we are counting squares, the result must be an integer.
    '''
    area = 0
    for a, b in pairwise(points):
        ax, ay = a
        bx, by = b
        area += ax * (by - ay) if (ax == bx) else ay * (ax - bx)
    return int(abs(area / 2))


class Lavaduct(object):

    LINE_PATTERN = re.compile('([UDLR]{1}) (\d+) \(\#(\w{6})\)')
    DIRECTION_MAP = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    DIR_HEX_MAP = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

    def __init__(self, filepath:str, with_hex=False):
        self.points = [(0, 0)]
        self.perimeter = 0
        self.with_hex = with_hex
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)
    
    @property
    def inner_area(self):
        return integrate_manhattan_line(self.points)

    @property
    def outer_area(self):
        return self.inner_area + int(self.perimeter / 2) + 1

    def add_point(self, direction:str, amount:int, colour:str):
        x, y = self.points[-1]
        dx, dy = self.DIRECTION_MAP[direction]
        self.points.append((x + dx * amount, y + dy * amount))


    def process_input_line(self, input_line:str):
        parse_input = self.LINE_PATTERN.search(input_line)
        direction = parse_input.group(1)
        amount = int(parse_input.group(2))
        colour = parse_input.group(3)
        if self.with_hex:
            direction = self.DIR_HEX_MAP[colour[5]]
            amount = int(colour[:-1], 16)
        self.add_point(direction, amount, colour)
        self.perimeter += amount


# 1. Functions that are specific for problem 1

def lavaduct_lagoon_1(filepath:str, with_hex:bool=False):
    lavaduct = Lavaduct(filepath, with_hex)
    return lavaduct.outer_area

# 2. Functions that are specific for problem 2

def lavaduct_lagoon_2(filepath:str):
    lavaduct = Lavaduct(filepath)
    return lavaduct.outer_area


if __name__ == '__main__':
    assert(lavaduct_lagoon_1('test_01.txt') == 62)
    # assert(pipe_maze_1('puzzle_input.txt') == 6733)

    print(lavaduct_lagoon_1('puzzle_input.txt', True))
