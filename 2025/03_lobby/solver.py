''' Advent of Code 2025
    Day 3: Lobby
    https://adventofcode.com/2025/day/3

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
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


def get_joltage(number:str) -> int:
    a = max(number)
    ai = number.index(a)

    if(ai < len(number)-1):
        b = max(number[ai+1:])
        # a and b are string objects, hence + concatenates!
        return int(a + b)
    
    number = number[:ai] + number[ai+1:]
    b = max(number)
    # a and b are string objects, hence + concatenates!
    return int(b + a)

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    result = sum(map(get_joltage, parse_file(filepath)))

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result

def get_higher_joltage(number:str, digits:int) -> str:

    return '-1'

def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    result = sum(map(lambda x: int(get_higher_joltage(x, 12)), parse_file(filepath)))

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 357)
    assert(solve_part_1('puzzle.txt') == 17113)

    assert(solve_part_2('test.txt') == 4174379265)
    assert(solve_part_2('puzzle.txt') == 28915664433)  # too high