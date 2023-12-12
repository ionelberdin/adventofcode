''' Advent of Code 2023
    Day 12: Hot Springs 
    https://adventofcode.com/2023/day/11

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: TBC
        * Puzzle: TBC
'''

import re

from itertools import permutations, product

# 0. Functions that are common to both problems

DAMAGED = re.compile('(\#)')
UNKNOWN = re.compile('(\?)')

def get_records(filepath:str):
    with open(filepath, 'r') as f:
        while (line := f.readline().strip('\n\s\t')):
            yield line

def get_arrangements(record:str):
    ''' Doesn't converge for long strings with many unknowns '''
    record, damaged_group_sizes = record.split(' ')
    damaged_group_sizes = [int(x) for x in damaged_group_sizes.split(',')]
    total_damaged = sum(damaged_group_sizes)
    total_unknowns = len(UNKNOWN.findall(record))
    total_damaged_in_str = len(DAMAGED.findall(record))

    pattern = '\.+'.join(['(\#{{{}}})'] * len(damaged_group_sizes))
    pattern = re.compile(pattern.format(*damaged_group_sizes))

    template = record.replace('?', '{}')
    
    damaged = '#' * (total_damaged - total_damaged_in_str)
    operational = '.' * (total_unknowns - len(damaged))

    unknown_permutations = set(permutations(damaged + operational, total_unknowns))

    arrangements = map(lambda x: template.format(*x), unknown_permutations)
    arrangements = filter(pattern.search, arrangements)

    return len([x for x in arrangements])

def get_arrangements_2(record):
    record, damaged_group_sizes = record.split(' ')
    damaged_group_sizes = [int(x) for x in damaged_group_sizes.split(',')]

    total_damaged = sum(damaged_group_sizes)
    total_unknowns = len(UNKNOWN.findall(record))
    total_damaged_in_str = len(DAMAGED.findall(record))

    pattern = record.replace('.', '\.').replace('#', '\#').replace('?', '.')
    pattern = re.compile(pattern)

    total_operational = len(record) - total_damaged
    
    return get_operational_cases(total_operational, len(damaged_group_sizes))

def get_operational_cases(operational:int, damaged_groups:int):
    internal = list([tuple(range(1, operational - damaged_groups + 2))]) * (damaged_groups - 1)
    external = [tuple(range(operational - damaged_groups + 1))]
    cases = product(*[external + internal + external])
    return len([x for x in cases])


def hot_springs(filepath:str):
    return sum(map(get_arrangements_2, get_records(filepath)))


if __name__ == '__main__':
    # assert(hot_springs('test_01.txt') == 21)
    # assert(hot_springs('puzzle_input.txt') == )

    # assert(hot_springs('test_01.txt') == )
    # assert(hot_springs('puzzle_input.txt') == )

    print(hot_springs('puzzle_input.txt'))
