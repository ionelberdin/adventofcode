''' Advent of Code 2024
    Day 4: Ceres Search
    https://adventofcode.com/2024/day/4

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

import re
from itertools import chain, product
from collections import Counter

def parse_file(filepath:str) -> list[str]:
    with open(filepath, 'r') as file:
        return list(map(lambda x: x.strip('\n\s\t'), file.readlines()))

def get_transposed_lines(lines):
    line_length = len(lines[0])
    for column in range(line_length):
        yield ''.join([line[column] for line in lines])

def get_forward_diagonals(lines):
    
    I = len(lines)
    J = len(lines[0])

    # upper diagonal
    for i in range(I):
        yield ''.join([lines[i-j][j] for j in range(min(i+1, J))])

    # lower diagonal
    for j in range(J-1):
        # -1 to avoid covering the same diagonal twice
        yield ''.join([lines[I-1-i][J-1-j+i] for i in range(min(j+1, I))])

def get_matches(line, regex_pattern):
    result = len(regex_pattern.findall(line))
    result += len(regex_pattern.findall(line[::-1]))
    return result

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    horizontal_lines = parse_file(filepath)
    vertical_lines = get_transposed_lines(horizontal_lines)
    forward_diagonal_lines = get_forward_diagonals(horizontal_lines)
    backward_diagonal_lines = get_forward_diagonals(horizontal_lines[::-1])

    all_lines = chain(horizontal_lines, vertical_lines)
    all_lines = chain(all_lines, forward_diagonal_lines)
    all_lines = chain(all_lines, backward_diagonal_lines)

    PATTERN = re.compile('XMAS')
    result = sum(map(lambda x: get_matches(x, PATTERN), all_lines))
    print("Result of part 1:", result)
    return result


def get_cross_center_candidates(lines):
    for i, j in product(range(1, len(lines)-1), range(1, len(lines[0])-1)):
        if lines[i][j] == 'A':
            yield (i, j)

def is_cross(candidate_center, lines):
    i, j = candidate_center
    top_left = lines[i-1][j-1]
    top_right = lines[i-1][j+1]
    bottom_left = lines[i+1][j-1]
    bottom_right = lines[i+1][j+1]
    counter = Counter([top_left, top_right, bottom_left, bottom_right])
    return (counter['M'] == 2 and counter['S'] == 2 and top_left != bottom_right)


def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    lines = parse_file(filepath)
    cross_center_candidates = get_cross_center_candidates(lines)
    mas_crosses = filter(lambda x: is_cross(x, lines), cross_center_candidates)
    result = len(list(mas_crosses))
    print("Result of part 2:", result)
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 18)
    assert(solve_part_1('puzzle.txt') == 2578)

    assert(solve_part_2('test.txt') == 9)
    print(solve_part_2('puzzle.txt') == 1972)