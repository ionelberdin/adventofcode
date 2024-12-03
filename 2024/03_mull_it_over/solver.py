''' Advent of Code 2024
    Day 3: Mull It Over
    https://adventofcode.com/2024/day/3

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

import re
from functools import reduce

PATTERN1 = re.compile('mul\((?P<X>\d+)\,(?P<Y>\d+)\)')
PATTERN2 = re.compile('mul\((?P<X>\d+)\,(?P<Y>\d+)\)|do\(\)|don\'t\(\)')

def parse_line(line:str) -> list[int]:
    return list(map(int, line.strip('\n\s\t').split(' ')))

def get_products1(file):
    for line in file:
        for match in PATTERN1.finditer(line):
            yield int(match.group('X')) * int(match.group('Y'))

def get_products2(file):
    do = True
    for line in file:
        for match in PATTERN2.finditer(line):
            if match.group(0) == 'do()':
                do = True
            elif match.group(0) == "don't()":
                do = False
            elif do:
                yield int(match.group('X')) * int(match.group('Y'))

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    with open(filepath, 'r') as file:
        result = reduce(lambda x, y: x + y, get_products1(file))
    print("Result of part 1:", result)
    return result


def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    with open(filepath, 'r') as file:
        result = reduce(lambda x, y: x + y, get_products2(file))
    print("Result of part 2:", result)
    return result


if __name__ == '__main__':
    assert(solve_part_1('test.txt') == 161)
    assert(solve_part_1('puzzle.txt') == 188192787)

    assert(solve_part_2('test2.txt') == 48)
    print(solve_part_2('puzzle.txt') == 413)