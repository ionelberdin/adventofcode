''' Advent of Code 2025
    Day 6: Trash Compactor
    https://adventofcode.com/2025/day/6

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: TODO
        * Puzzle: TODO
'''

from timeit import default_timer
from functools import reduce
import re


OPERATORS = {
    '+': lambda x, y: x+y,
    '*': lambda x, y: x*y
}

SEP = re.compile(r'[\s\t]+')

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    lines = list()
    with open(filepath, 'r') as file:
        for line in file:
            try:
                line = line.strip('\s\t\n')
                line = list(filter(lambda x: x != '', SEP.split(line)))
                lines.append(list(map(int, line)))
            except:
                operators = list(line)
    
    result = 0 
    for i, operator in enumerate(operators):
        result += reduce(OPERATORS[operator], [x[i] for x in lines])


    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result


def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    result = -1

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 4277556)
    assert(solve_part_1('puzzle.txt') == 5877594983578)

    assert(solve_part_2('test.txt') == 14)
    assert(solve_part_2('puzzle.txt') == 354282804136607) # too high