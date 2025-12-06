''' Advent of Code 2025
    Day 5: Cafeteria
    https://adventofcode.com/2025/day/5

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
from itertools import chain

def get_containing_range(ranges:set[tuple[int,int]], value:int) -> tuple[int,int] | None:
    for (a, b) in ranges:
        if a<= value <= b:
            return (a, b)
    return None


def consolidate_ranges(file) -> set[tuple[int]]:
    # read first until first empty line
    ranges = set()
    
    for line in file:
        line = line.strip('\s\t\n')
        if line == '':
            break

        a, b = (int(x) for x in line.split('-'))
        if (a > b):
            raise(Exception("Wrong order, first number higher than second"))
        
        # Remove the comment in the next 2 lines to avoid consolidation
        # ranges.add((a, b))
        # continue

        # Consolidation proves to be slower for the actual puzzle of this problem
        range_a = get_containing_range(ranges, a)
        range_b = get_containing_range(ranges, b)

        if (range_a is not None) and (range_b is not None):
            if range_a == range_b:
                continue
            ranges.remove(range_a)
            ranges.remove(range_b)
            range_min = min((range_a[0], range_b[0]))
            range_max = max((range_a[1], range_b[1]))
            ranges.add((range_min, range_max))
        
        elif range_a is None and (range_b is not None):
            ranges.remove(range_b)
            ranges.add((a, range_b[1]))

        elif range_a is not None and (range_b is None):
            ranges.remove(range_a)
            ranges.add((range_a[0], b))
        else:
            ranges.add((a, b))

    return ranges



def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    file = open(filepath, 'r')
    ranges = consolidate_ranges(file)

    result = 0
    for line in file:
        number = int(line.strip('\s\t\n'))
        result += get_containing_range(ranges, number) is not None

    file.close()

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result


def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    file = open(filepath, 'r')
    ranges = consolidate_ranges(file)
    file.close()

    result = sum(map(lambda x: (x[1]-x[0]+1), ranges))

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 3)
    assert(solve_part_1('puzzle.txt') == 828)

    assert(solve_part_2('test.txt') == 14)
    assert(solve_part_2('puzzle.txt') == 354282804136607) # too high