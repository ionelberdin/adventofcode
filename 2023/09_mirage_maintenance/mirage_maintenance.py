''' Advent of Code 2023
    Day 09: Mirage Maintenance
    https://adventofcode.com/2023/day/9

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 1: PASS
        * Puzzle: PASS
'''
import re
from functools import reduce


# 0. Functions that are common to both problems

def parse_input(filepath:str):
    with open(filepath, 'r') as f:
        while (line := f.readline()):
            yield [int(x) for x in line.strip('\n\s\t').split(' ')]

# 1. Functions that are specific for problem 1

def mirage_maintenance_1(filepath:str):
    next_values = map(get_next_value, parse_input(filepath))

    return sum(next_values)

def get_next_value(history):
    history = [history]
    while (any([x != 0 for x in history[-1]])):
        history.append([y - x for x, y in zip(history[-1][:-1], history[-1][1:])])

    for i in range(2, len(history) + 1):
        history[-i].append(history[-i][-1] + history[-i + 1][-1])

    return history[0][-1]

# 2. Functions that are specific for problem 2

def mirage_maintenance_2(filepath:str):
    previous_values = map(get_next_value, map(lambda x: x[::-1], parse_input(filepath)))

    return sum(previous_values)


if __name__ == '__main__':
    assert(mirage_maintenance_1('test_01.txt') == 114)
    assert(mirage_maintenance_1('puzzle_input.txt') == 1938731307)
    assert(mirage_maintenance_2('test_01.txt') == 2)


    print(mirage_maintenance_2('puzzle_input.txt'))
