''' Advent of Code 2024
    Day 1: Historian Hysteria
    https://adventofcode.com/2024/day/1

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
from collections import Counter

separator = re.compile('[\s\t]+')
def parse_line(line:str) -> list[int]:
    return list(map(int, separator.split(line.strip('\n\s\t'))))


def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    with open(filepath, 'r') as f:
        entries = list(map(parse_line, f.readlines()))
    list_a = sorted([x[0] for x in entries])
    list_b = sorted([x[1] for x in entries])
    result = reduce(lambda x, y: x + y, 
                    map(lambda x, y: abs(x - y), list_a, list_b))
    print("Total distance:", result)
    return result


def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    with open(filepath, 'r') as f:
        entries = list(map(parse_line, f.readlines()))
    list_a = Counter([x[0] for x in entries])
    list_b = Counter([x[1] for x in entries])
    result = reduce(lambda x, y: x + y, map(lambda x: x*list_a[x]*list_b[x], list_a))
    print("Total similarity:", result)
    return result


if __name__ == '__main__':
    assert(solve_part_1('test.txt') == 11)
    assert(solve_part_1('puzzle.txt') == 1938424)

    assert(solve_part_2('test.txt') == 31)
    assert(solve_part_2('puzzle.txt') == 22014209)