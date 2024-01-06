''' Advent of Code 2023
    Day 4: Scratchcards
    https://adventofcode.com/2023/day/4
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

from timeit import default_timer


class Solver(object):

    def __init__(self, filepath:str):
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def process_input_line(self, input_line:str):
        pass

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
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
    # assert(solve('test_01.txt', part=1) == TBD)
    # assert(solve('puzzle_input.txt', part=1) == TBD)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('test_01.txt', part=1))
