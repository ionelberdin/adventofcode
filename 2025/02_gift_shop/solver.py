''' Advent of Code 2025
    Day 2: Gift Shop
    https://adventofcode.com/2025/day/2

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: FAIL
'''

from timeit import default_timer
from collections.abc import Iterable


def parse_file(filepath:str) -> Iterable[list[int]]:
    with open(filepath, 'r') as file:
        for line in file:
            for id_range in line.split(','):
                ids = id_range.split('-')
                yield [int(x) for x in ids]


def check_invalid(number:int) -> int:
    number_str = str(number)
    number_lenght = len(number_str)
    if (number_lenght % 2):
        return 0
    middle = int(number_lenght/2)
    if (number_str[:middle] == number_str[middle:]):
        return number
    return 0

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    # brute force solution
    result = 0
    for ids in parse_file(filepath):
        result += sum(map(check_invalid, range(ids[0], ids[1]+1)))

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result

def get_factors(number:int) -> Iterable[int]:
    yield 1
    for factor in range(2, int(number/2)+1):
        if(number % factor == 0):
            yield factor


def check_invalid2(number:int) -> int:
    number_str = str(number)
    number_lenght = len(number_str)
    for i in get_factors(number_lenght):
        groups = map(lambda x: number_str[0:i] == number_str[i*x:i*(x+1)], range(1, int(number_lenght/i)))
        if all(groups):
            return number
    return 0

def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    # brute force solution
    result = 0
    for ids in parse_file(filepath):
        result += sum(map(check_invalid2, range(ids[0], ids[1]+1)))

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 1227775554)
    assert(solve_part_1('puzzle.txt') == 21898734247)

    assert(solve_part_2('test.txt') == 4174379265)
    assert(solve_part_2('test2.txt') == 11+22)
    assert(solve_part_2('test3.txt') == 99+111)
    assert(solve_part_2('test4.txt') == 999+1010)
    assert(solve_part_2('test5.txt') == 1188511885)
    assert(solve_part_2('test6.txt') == 222222)
    assert(solve_part_2('test7.txt') == 0)
    assert(solve_part_2('puzzle.txt') == 28915664433)  # too high