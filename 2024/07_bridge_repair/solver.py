''' Advent of Code 2024
    Day 7: Bridge Repair
    https://adventofcode.com/2024/day/7

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from timeit import default_timer
import re
from itertools import product

PATTERN = re.compile('[\:\s]+')

def parse_file(filepath:str) -> list[str]:
    with open(filepath, 'r') as file:
        for line in file:
            args = list(map(int, PATTERN.split(line.strip('\n\s\b'))))
            yield args

def is_possibly_true(args, operators):
    test_result = args[0]
    operands = args[1:]
    number_of_operands = len(operands)
    number_of_operators = number_of_operands - 1
    for permutation in product(operators, repeat=number_of_operators):
        result = operands[0]
        for operator, operand in zip(permutation, operands[1:]):
            result = operator(result, operand)
        if result == test_result:
            return True
    return False

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    operators = [lambda x, y: x + y, lambda x, y: x * y]
    test_values = filter(lambda x: is_possibly_true(x, operators), parse_file(filepath))
    test_values = map(lambda x: x[0], test_values)
    result = sum(test_values)

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result

def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    start = default_timer()

    operators = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]
    test_values = filter(lambda x: is_possibly_true(x, operators), parse_file(filepath))
    test_values = map(lambda x: x[0], test_values)
    result = sum(test_values)

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 3749)
    assert(solve_part_1('puzzle.txt') == 1153997401072)

    assert(solve_part_2('test.txt') == 11387)
    assert(solve_part_2('puzzle.txt') == 97902809384118)