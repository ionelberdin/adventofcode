''' Advent of Code 2024
    Day 8: Resonant Collinearity
    https://adventofcode.com/2024/day/8

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from timeit import default_timer
from functools import reduce
from itertools import combinations

def parse_file(filepath:str) -> list[list[str]]:
    with open(filepath, 'r') as file:
        lines = map(lambda line: [char for char in line.strip('\n\s\t')], file.readlines())
        return list(lines)

def get_antenna_types(lines):
    antenna_types = map(set, lines)
    antenna_types = reduce(lambda x, y: x | y, antenna_types)
    antenna_types.remove('.')
    return antenna_types

def get_antenna_positions(antenna_type, lines):
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == antenna_type:
                yield (x, y) 

def get_antinodes(antenna_positions, lines):
    rows = len(lines)
    columns = len(lines[0])

    for antenna1, antenna2 in combinations(antenna_positions, 2):
        x1, y1 = antenna1
        x2, y2 = antenna2
        dx = x2 - x1
        dy = y2 - y1
        antinode_x = x1 - dx
        antinode_y = y1 - dy
        if ((0 <= antinode_x < rows) and (0 <= antinode_y < columns)):
            yield (antinode_x, antinode_y)

        antinode_x = x2 + dx
        antinode_y = y2 + dy
        if ((0 <= antinode_x < rows) and (0 <= antinode_y < columns)):
            yield (antinode_x, antinode_y)



def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    lines = parse_file(filepath)
    antenna_types = get_antenna_types(lines)
    antenna_positions = map(lambda x: list(get_antenna_positions(x, lines)), antenna_types)
    antinodes = map(lambda positions: get_antinodes(positions, lines), antenna_positions)
    result = len(reduce(lambda x, y: x | y, map(set, antinodes)))

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result

def get_harmonic_antinodes(antenna_positions, lines):
    rows = len(lines)
    columns = len(lines[0])

    for antenna1, antenna2 in combinations(antenna_positions, 2):
        x1, y1 = antenna1
        x2, y2 = antenna2
        dx = x2 - x1
        dy = y2 - y1
        antinode_x = x1
        antinode_y = y1
        while ((0 <= antinode_x < rows) and (0 <= antinode_y < columns)):
            yield (antinode_x, antinode_y)
            antinode_x -= dx
            antinode_y -= dy

        antinode_x = x2
        antinode_y = y2
        while ((0 <= antinode_x < rows) and (0 <= antinode_y < columns)):
            yield (antinode_x, antinode_y)
            antinode_x += dx
            antinode_y += dy

def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    lines = parse_file(filepath)
    antenna_types = get_antenna_types(lines)
    antenna_positions = map(lambda x: list(get_antenna_positions(x, lines)), antenna_types)
    antinodes = map(lambda positions: get_harmonic_antinodes(positions, lines), antenna_positions)
    result = len(reduce(lambda x, y: x | y, map(set, antinodes)))

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 14)
    assert(solve_part_1('puzzle.txt') == 369)

    assert(solve_part_2('test.txt') == 34)
    assert(solve_part_2('puzzle.txt') == 1169)