''' Advent of Code 2025
    Day 6: Trash Compactor
    https://adventofcode.com/2025/day/6

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


def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    result = -1

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
    
    assert(solve_part_1('test.txt') == 3)
    assert(solve_part_1('puzzle.txt') == 828)

    assert(solve_part_2('test.txt') == 14)
    assert(solve_part_2('puzzle.txt') == 354282804136607) # too high