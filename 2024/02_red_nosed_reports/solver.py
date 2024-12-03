''' Advent of Code 2024
    Day 2: Red-Nosed Reports
    https://adventofcode.com/2024/day/2

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from functools import reduce

def parse_line(line:str) -> list[int]:
    return list(map(int, line.strip('\n\s\t').split(' ')))

def is_report_safe(report:str, problem_dampener:bool=False) -> bool:
    diff = list(map(lambda x, y: x - y, report[1:], report[:-1]))
    positive = all(map(lambda x: 0 < x < 4, diff))
    negative = all(map(lambda x: 0 > x > -4, diff))
    if (positive or negative):
        return True
    if problem_dampener == False:
        return False
    return any(map(is_report_safe, [report[:i] + report[i+1:] for i in range(len(report))]))

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    with open(filepath, 'r') as f:
        result = reduce(lambda x, y: x + y, map(is_report_safe, map(parse_line, f.readlines())))
    print("Number of safe reports:", result)
    return result


def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    with open(filepath, 'r') as f:
        result = reduce(lambda x, y: x + y, 
                        map(lambda x: is_report_safe(x, True), 
                            map(parse_line, f.readlines())))
    print("Number of safe reports:", result)
    return result


if __name__ == '__main__':
    assert(solve_part_1('test.txt') == 2)
    assert(solve_part_1('puzzle.txt') == 356)

    assert(solve_part_2('test.txt') == 4)
    print(solve_part_2('puzzle.txt') == 413)