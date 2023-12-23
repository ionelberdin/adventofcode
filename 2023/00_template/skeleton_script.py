''' Advent of Code 2023
    Day 00: Skeleton Script
    https://adventofcode.com/2023/day/00

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''


# 0. Code common to both parts of the problem

class Main(object):

    def __init__(self, filepath:str):
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def process_input_line(self, input_line:str):
        pass

    def solve_part_1(self):
        return None

    def solve_part_2(self):
        return None


# 1. Code specific for part 1

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    main = Main(filepath)
    return main.solve_part_1()

# 2. Code specific for part 2

def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    main = Main(filepath)
    return main.solve_part_1()

if __name__ == '__main__':
    # assert(solve_part_1('test_01.txt') == TBD)
    # assert(solve_part_1('puzzle_input.txt') == TBD)
    # assert(solve_part_2('test_01.txt') == TBD)
    # assert(solve_part_2('puzzle_input.txt') == TBD)

    print(solve_part_1('test_01.txt'))
