''' Advent of Code 2025
    Day 1: Secret Entrance
    https://adventofcode.com/2025/day/1

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from timeit import default_timer
from collections.abc import Iterable
import re


PATTERN = re.compile("[LR]{1}\d+")


def parse_file(filepath:str) -> Iterable[int]:
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip('\n\s\t')
            sign = -1 if (line[0] == "L") else 1
            yield sign * int(line[1:])


def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()

    dial = int(50)
    zeros = 0
     
    for rotation in parse_file(filepath):
        dial += rotation
        dial %= 100
        zeros += (dial == 0)

    result = zeros

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result

def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    dial = 50
    zeros = 0
     
    for rotation in parse_file(filepath):
               
        prev_was_zero = (dial == 0)

        cycles = int(rotation / 100)
        rotation -= cycles * 100
        dial += rotation
        
        # Change to negative only counts if the previous dial was not already zero
        change_to_negative = (dial < 0 and not prev_was_zero)

        zeros += dial > 100
        zeros += abs(cycles)
        zeros += change_to_negative
        dial %= 100
        zeros += (dial == 0) 
        zeros -= (rotation == 0)

        print(f"{dial};{rotation};{cycles};{zeros}")

    result = zeros

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 3)
    assert(solve_part_1('puzzle.txt') == 1052)

    assert(solve_part_2('test.txt') == 6)
    assert(solve_part_2('test2.txt') == 10)
    assert(solve_part_2('puzzle.txt') == 6295)
    assert(solve_part_2('test3.txt') == 2)  # FIXME : This  test fails