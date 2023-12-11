''' Advent of Code 2023
    Day 11: Cosmic Expansion
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

from itertools import combinations

# 0. Functions that are common to both problems


class Universe(object):

    ALL_EMPTY = re.compile('^\.+$')

    def __init__(self, filepath:str):
        with open(filepath, 'r') as f:
            self.rows = [x.strip('\n\s\t') for x in f.readlines()]
        self.expand()
        self.expand(True)
        self.galaxies = [x for x in self.find_galaxies()]

    def expand(self, cols=False):
        rows = self.transpose(self.rows) if cols else list(self.rows)
        rows_copy = list(rows)
        i = 0
        for j, row in enumerate(rows_copy):
            if (self.ALL_EMPTY.search(row)):
                rows.insert(i, rows_copy[j])
                i += 1
            i += 1

        self.rows = self.transpose(rows) if cols else rows

    def find_galaxies(self, what:str='#'):
        galaxies = set()
        for row_index, row in enumerate(self.rows):
            for col_index, char in enumerate(row):
                if (char == what):
                    galaxies.add((row_index, col_index))
        return galaxies

    def get_galaxy_pairs(self):
        return combinations(self.galaxies, 2)

    @staticmethod
    def get_manhattan_distance(galaxy_a, galaxy_b):
        return sum(map(abs, [x - y for x, y in zip(galaxy_a, galaxy_b)]))

    @staticmethod
    def transpose(list_of_lists):
        row_length = len(list_of_lists[0])
        return [''.join([x[i] for x in list_of_lists]) for i in range(row_length)]


# 1. Functions that are specific for problem 1

def cosmic_expansion_1(filepath:str):
    universe = Universe(filepath)
    galaxy_pairs = universe.get_galaxy_pairs()
    return sum(map(lambda x: universe.get_manhattan_distance(*x), galaxy_pairs))


if __name__ == '__main__':
    assert(cosmic_expansion_1('test_01.txt') == 374)
    assert(cosmic_expansion_1('puzzle_input.txt') == 9947476)

    print(cosmic_expansion_1('test_01.txt'))
