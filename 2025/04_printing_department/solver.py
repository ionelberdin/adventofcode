''' Advent of Code 2025
    Day 4: Printing Department
    https://adventofcode.com/2025/day/4

Status:
    - Part 1:
        * Test: TODO
        * Puzzle: TODO
    - Part 2:
        * Test: TODO
        * Puzzle: TODO
'''

from timeit import default_timer
from collections.abc import Iterable


def parse_file(filepath:str) -> Iterable[str]:
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip('\s\t\n')



def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    
    result = -1  # TODO

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result


def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    result = -1  # TODO

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 13)
    assert(solve_part_1('puzzle.txt') == 17113)

    assert(solve_part_2('test.txt') == 4174379265)
    assert(solve_part_2('puzzle.txt') == 28915664433) 