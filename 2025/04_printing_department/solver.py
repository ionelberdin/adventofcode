''' Advent of Code 2025
    Day 4: Printing Department
    https://adventofcode.com/2025/day/4

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
from itertools import chain


def parse_file(filepath:str) -> Iterable[str]:
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip('\s\t\n')

def get_roll_set(line:str) -> set[int]:
    return set([n for n, x in enumerate(line) if x == '@'])

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    file = open(filepath, 'r')
    prv = set()
    ths = get_roll_set(file.readline())

    result = 0

    for line in chain.from_iterable([file, ['']]):
        nxt = get_roll_set(line)
        for pos in ths:
            cnt = (pos - 1 in prv) + (pos - 1 in ths) + (pos - 1 in nxt)
            cnt += (pos in prv) + (pos in nxt)
            cnt += (pos + 1 in prv) + (pos + 1 in ths) + (pos + 1 in nxt)
            if cnt < 4:
                result += 1
        
        prv = set(ths)
        ths = set(nxt)

    file.close()
    
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
    assert(solve_part_1('puzzle.txt') == 1508)

    assert(solve_part_2('test.txt') == 4174379265)
    assert(solve_part_2('puzzle.txt') == 28915664433) 