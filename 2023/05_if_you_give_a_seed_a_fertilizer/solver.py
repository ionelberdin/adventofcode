''' Advent of Code 2023
    Day 5: If you give a Seed a Fertilizer
    https://adventofcode.com/2023/day/5
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: PASS
        * Puzzle: TBD
'''

import re

from functools import reduce
from timeit import default_timer

MAP_PATTERN = re.compile('^(?P<map_name>[\w\-]+) map:$')

class Map(object):
    collection = {}
    sources = {}

    def __init__(self, map_name:str) -> None:
        self.map_name = map_name
        self.source, self.destination = map_name.split('-to-')
        self.rules = set()
        Map.add_map(self)

    @classmethod
    def add_map(cls, a_map) -> None:
        cls.collection[a_map.map_name] = a_map
        cls.sources[a_map.source] = a_map

    @classmethod
    def init(cls) -> None:
        cls.collection = {}
        cls.sources

    @classmethod
    def get_destination_from_source(cls, source:int, source_name:str, destination_name:str) -> int:
        result = source
        while (source_name != destination_name):
            a_map = cls.sources[source_name]
            result = a_map.get(result)
            source_name = a_map.destination
        return result

    def set(self, first_destination:int, first_source:int, amount:int) -> None:
        condition = lambda x: first_source <= x < first_source + amount
        transformation = lambda x: x + first_destination - first_source
        self.rules.add((condition, transformation)) 

    def get(self, source:int) -> int:
        for condition, transformation in self.rules:
            if (condition(source)):
                return transformation(source)
        return source

class Solver(object):

    def __init__(self, filepath:str):
        self.filepath = filepath

    def load_input(self):
        with open(self.filepath, 'r') as f:
            seeds = f.readline().split(':')[1].strip('\n\t ')
            self.seeds = list(map(int, seeds.split(' ')))

            f.readline()
            map_name = None
            while (line := f.readline()):
                line = line.strip('\n\t ')
                if (line == ''):
                    continue
                if ((result := MAP_PATTERN.search(line)) is not None):
                    map_name = result.group('map_name')
                    a_map = Map(map_name)
                    continue
                a_map.set(*[int(x) for x in line.split(' ')])
                

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        Map.init()
        self.load_input()
        get_locations = lambda x: Map.get_destination_from_source(x, 'seed', 'location')
        locations = map(get_locations, self.seeds)
        return min(locations)

    def solve_part_2(self):
        Map.init()
        self.load_input()
        get_locations = lambda x: Map.get_destination_from_source(x, 'seed', 'location')
        locations = map(get_locations, self.generate_seeds())
        return reduce(lambda x, y: min(x, y), locations)

    def generate_seeds(self) -> int:
        for x, y in zip(self.seeds[0::2], self.seeds[1::2]):
            for n in range(y):
                if (n % 1000000 == 0):
                yield x + n

def solve(filepath:str, part:int):
    print("Solving part {} with:".format(part), filepath)
    start = default_timer()
    solver = Solver(filepath)
    result = solver.solve(part=part)
    duration = default_timer() - start
    print("Solved in {}s".format(duration))
    print("Result:", result)
    return result


if __name__ == '__main__':
    assert(solve('test_01.txt', part=1) == 35)
    assert(solve('puzzle_input.txt', part=1) == 31599214)
    assert(solve('test_01.txt', part=2) == 46)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('puzzle_input.txt', part=2))
