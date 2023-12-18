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

from itertools import pairwise, permutations, product

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
    print(record)
    record, damaged_groups = record.split(' ')
    damaged_groups = [int(x) for x in damaged_groups.split(',')]

    total_damaged = sum(damaged_groups)
    total_unknowns = len(UNKNOWN.findall(record))
    total_damaged_in_str = len(DAMAGED.findall(record))

    pattern = record.replace('.', '\.').replace('#', '\#').replace('?', '.')
    pattern = re.compile(pattern)

    total_operational = len(record) - total_damaged
    
    operational_cases = get_operational_cases(total_operational, len(damaged_groups))
    operational_cases = map(lambda x: build_record(x, damaged_groups), operational_cases)
    operational_cases = filter(pattern.match, operational_cases)
    return len(list(map(lambda x: 1, operational_cases)))

def get_operational_cases(operational:int, damaged_groups:int):
    '''Given the number of operational hot springs, and the amount of damaged groups, 
    the strategy is to consider all the possible cases of groups of operational
    hot springs in between the non-operational ones.
    This should reduce the number of cases to check in comparison with the strategy
    followed in the first attempt.
    We may divide the types of operational hot spring groups into those that are
    external to the non-operational ones, and the internal ones.
    The difference between both of those types is:
        * The external belong to the integer group bewteen 0 and operational - (damaged_groups - 1)
            + There are only 2 possible external groups.
        * The internal belong to the integer group between 1 and operational - (damaged_groups - 1) + 1
            + There are always N-1 internal groups, being N the number of damaged_groups.
    all boundaries included.
    eg: Ext1 + DG1 + Int1 + DG2 + Int2 + DG3 + Ext2
    '''
    internal_groups = damaged_groups - 1
    external = [tuple(range(operational - internal_groups + 1))]
    internal = list([tuple(range(1, operational - internal_groups + 2))]) * (damaged_groups - 1)
    return map(lambda x: x[0], product(*[external + internal + external]))

def build_record(operational_groups, damaged_groups):
    record = '.' * operational_groups[0]
    for damaged, operational in zip(damaged_groups, operational_groups[1:]):
        print(damaged, operational)
        record += '#' * damaged + '.' * operational
    print(operational_groups, damaged_groups, record)
    return record

def hot_springs(filepath:str):
    return sum(map(get_arrangements_2, get_records(filepath)))


if __name__ == '__main__':
    # assert(hot_springs('test_01.txt') == 21)
    # assert(hot_springs('puzzle_input.txt') == )

    # assert(hot_springs('test_01.txt') == )
    # assert(hot_springs('puzzle_input.txt') == )

    print(hot_springs('test_01.txt'))
    # print(hot_springs('puzzle_input.txt'))
