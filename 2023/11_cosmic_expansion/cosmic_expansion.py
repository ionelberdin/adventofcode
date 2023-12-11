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
        self.empty_rows = self.get_empty_rows()
        self.empty_cols = self.get_empty_rows(transpose=True)
        self.galaxies = [x for x in self.find_galaxies()]

    def get_empty_rows(self, transpose=False):
        rows = self.transpose(self.rows) if transpose else list(self.rows)
        empty_indices = set()
        for i, row in enumerate(rows):
            if (self.ALL_EMPTY.search(row)):
                empty_indices.add(i)
        return empty_indices

    def find_galaxies(self, what:str='#'):
        galaxies = set()
        for row_index, row in enumerate(self.rows):
            for col_index, char in enumerate(row):
                if (char == what):
                    galaxies.add((row_index, col_index))
        return galaxies

    def get_expanded_distance(self, galaxy_a, galaxy_b, expansion_factor):
        row_a, col_a = galaxy_a
        row_b, col_b = galaxy_b
        row_max, row_min = max(row_a, row_b), min(row_b, row_a)
        col_max, col_min = max(col_a, col_b), min(col_b, col_a)
        
        expansion_factor -= 1

        empty_rows = filter(lambda x: row_min < x < row_max, self.empty_rows) 
        row_delta = row_max - row_min + expansion_factor * len(list(empty_rows))
        
        empty_cols = filter(lambda x: col_min < x < col_max, self.empty_cols) 
        col_delta = col_max - col_min + expansion_factor * len(list(empty_cols))
        
        return row_delta + col_delta

    def get_galaxy_pairs(self):
        return combinations(self.galaxies, 2)

    @staticmethod
    def get_manhattan_distance(galaxy_a, galaxy_b):
        return sum(map(abs, [x - y for x, y in zip(galaxy_a, galaxy_b)]))

    @staticmethod
    def transpose(list_of_lists):
        row_length = len(list_of_lists[0])
        return [''.join([x[i] for x in list_of_lists]) for i in range(row_length)]


def cosmic_expansion_1(filepath:str, expansion_factor:int=2):
    universe = Universe(filepath)
    galaxy_pairs = universe.get_galaxy_pairs()
    return sum(map(lambda x: universe.get_expanded_distance(x[0], x[1], expansion_factor), galaxy_pairs))


if __name__ == '__main__':
    assert(cosmic_expansion_1('test_01.txt', expansion_factor=2) == 374)
    assert(cosmic_expansion_1('puzzle_input.txt', expansion_factor=2) == 9947476)

    assert(cosmic_expansion_1('test_01.txt', expansion_factor=10) == 1030)
    assert(cosmic_expansion_1('test_01.txt', expansion_factor=100) == 8410)
    assert(cosmic_expansion_1('puzzle_input.txt', expansion_factor=1000000) == 519939907614)

    print(cosmic_expansion_1('puzzle_input.txt', expansion_factor=1000000))
