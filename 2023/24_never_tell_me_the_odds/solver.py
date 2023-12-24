''' Advent of Code 2023
    Day 24: Never tell me the odds  
    https://adventofcode.com/2023/day/24
    Keywords: Straight lines intersection, 2D, 3D

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from itertools import combinations
from timeit import default_timer

class Line(object):
    
    collection = set()

    def __init__(self, point, direction):
        self.point = point
        self.direction = direction

        Line.collection.add(self)

    def get_2D_intersection(self, other):
        # Check if they are parallel
        ax, ay, _ = self.direction
        bx, by, _ = other.direction
        if ((div := (ax * by - ay * bx)) == 0):
            # They could actually collide if they were in the same line,
            # but I've checked in the input data and that never happens.
            return None  

        # Get intersection
        Ax, Ay, _ = self.point
        Bx, By, _ = other.point
        x = ((Ay * ax - Ax * ay) * bx - (By * bx - Bx * by) * ax) / div
        y = ((ay / ax) * (x - Ax) + Ay) if ax != 0 else ((by / bx) * (x - Bx) + By)

        # Check if intersection is in the future for each line
        if (((x - Ax) * ax + (y - Ay) * ay) < 0):
            return None  # Line "a" (self) intersected in the past
        if (((x - Bx) * bx + (y - By) * by) < 0):
            return None  # Line "b" (other) intersected in the past
        
        return (x, y)

    @staticmethod
    def get_static_2D_intersection(line_a, line_b):
        return line_a.get_2D_intersection(line_b)

    @staticmethod
    def get_static_2D_distance(line_a, line_b):
        Ax, Ay, _ = line_a.point
        Bx, By, _ = line_b.point
        ax, ay, _ = line_a.direction
        nx, ny = ay, -ax
        return abs(nx * (Bx - Ax) + ny * (By - Ay))

    def __repr__(self):
        x, y, _ = self.point
        dx, dy, _ = self.direction
        return '({}, {})~({}, {})'.format(x, y, dx, dy)

        
class Solver(object):

    SPLIT_PATTERN = re.compile('[\s\,\@]+')

    def __init__(self, filepath:str, boundary:tuple):
        Line.collection = set()
        self.input_path = filepath
        self.boundary = boundary

    def is_intersection_within_boundaries(self, intersection):
        x, y = intersection
        a, b = self.boundary
        if ((a <= x <= b) and (a <= y <= b)):
            return True
        return False

    def process_input(self):
        with open(self.input_path, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def process_input_line(self, input_line:str):
        line = list(map(int, Solver.SPLIT_PATTERN.split(input_line)))
        x, y, z, dx, dy, dz = line
        Line((x, y, z), (dx, dy, dz))

    def solve(self, part:int): 
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        intersections = map(lambda lines: Line.get_static_2D_intersection(*lines),
                            combinations(Line.collection, 2))
        intersections = filter(lambda i: i is not None, intersections)
        intersections = filter(self.is_intersection_within_boundaries, intersections)
        return len(list(intersections))

    def solve_part_2(self):
        return None


def solve(filepath:str, part:int, boundary:tuple):
    print("Solving part {} with:".format(part), filepath)
    start = default_timer()
    solver = Solver(filepath, boundary)
    solver.process_input()
    result = solver.solve(part=part)
    duration = default_timer() - start
    print("Solved in {}s".format(duration))
    print("Result:", result)
    return result


if __name__ == '__main__':
    assert(solve('test_01.txt', part=1, boundary=(7, 27)) == 2)
    big = 100 * 1000 * 1000 * 1000 * 1000
    assert(solve('puzzle_input.txt', part=1, boundary=(2 * big, 4 * big)) == 17776)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)
    print(solve('test_01.txt', part=1, boundary=(7, 27)))
    #print(solve('puzzle_input.txt', part=1, boundary=(2 * big, 4 * big)))
