''' Advent of Code 2023
    Day 5: If you give a Seed a Fertilizer
    https://adventofcode.com/2023/day/5
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from timeit import default_timer

MAP_PATTERN = re.compile('^(?p<map_name>[\w\-]+) map:$')

class Map(object):
    collection = {}
    sources = {}

    def __init__(self, map_name:str):
        self.map_name = map_name
        self.source, self.destination = map_name.split('-to-')
        self.rules = {}
        Map.add_map(self)

    @classmethod
    def add_map(cls, a_map):
        cls.collection[a_map.map_name] = a_map
        cls.sources[a_map.source] = a_map

    @classmethod
    def init(cls):
        cls.collection = {}
        cls.sources

    @classmethod
    def get_destination_from_source(cls, source:int, source_name:str, destination_name:str) -> int:
        result = source
        destination = None
        while (destination != destination_name):
            a_map = cls.sources[source_name]
            destination = a_map.destination
            result = a_map.get(result)
        return result

    def set(self, first_source:int, first_destination:int, amount:int) -> None:
        for n in range(amount):
            self.rules[first_source + n] = first_destination + n

    def get(self, source:int) -> int:
        return self.rules[source] if source in self.rules else source

class Solver(object):

    def __init__(self, filepath:str):
        self.filepath = filepath

    def load_input(self):
        with open(self.filepath, 'r') as f:
            seeds = f.readline().split(':')[1].strip('\n\t\s')
            self.seeds = set(map(int, seeds.split(' ')))

            f.readline()
            map_name = None
            while (line := f.readline().strip('\n\t\s')):
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
        self.load_input()
        get_locations = lambda x: Map.get_destination_from_source(x, 'seed', 'location')
        locations = map(get_locations, self.seeds)
        return min(locations)

    def solve_part_2(self):
        return None


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
    # assert(solve('test_01.txt', part=1) == TBD)
    # assert(solve('puzzle_input.txt', part=1) == TBD)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('test_01.txt', part=1))
