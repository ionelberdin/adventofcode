''' Advent of Code 2023
    Day 5: If you give a Seed a Fertilizer
    https://adventofcode.com/2023/day/5
    Keywords: MappingTables, AgainstBruteForce

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: PASS
        * Puzzle: PASS
'''

import re

from functools import reduce
from timeit import default_timer

MAP_PATTERN = re.compile('^(?P<map_name>[\w\-]+) map:$')

class Map(object):
    collection = {}
    sources = {}
    ordered = []

    def __init__(self, map_name:str) -> None:
        self.map_name = map_name
        self.source, self.destination = map_name.split('-to-')
        self.rules = set()
        self.source_boundaries = set()
        self.destination_boundaries = set()
        Map.add_map(self)

    @classmethod
    def add_map(cls, a_map) -> None:
        cls.collection[a_map.map_name] = a_map
        cls.sources[a_map.source] = a_map
        cls.ordered.append(a_map)

    @classmethod
    def init(cls) -> None:
        cls.collection = {}
        cls.sources = {}
        cls.ordered = []

    @classmethod
    def get_destination_from_source(cls, source:int, source_name:str, destination_name:str) -> int:
        result = source
        while (source_name != destination_name):
            a_map = cls.sources[source_name]
            result = a_map.get(result)
            source_name = a_map.destination
        return result

    @classmethod
    def get_range_boundaries_from_destination_to_source(cls):
        range_boundaries = cls.ordered[-1].source_boundaries
        for a_map in cls.ordered[-2::-1]:
            range_boundaries = [a_map.get(x, forward=False) for x in range_boundaries]

            range_boundaries.extend(a_map.source_boundaries)

        return sorted(range_boundaries)

    def set(self, first_destination:int, first_source:int, amount:int) -> None:
        self.source_boundaries.update([first_source, first_source + amount])
        self.destination_boundaries.update([first_destination, first_destination + amount])

        condition = lambda x: first_source <= x < first_source + amount
        transformation = lambda x: x + first_destination - first_source
        condition_backward = lambda x: first_destination <= x < first_destination + amount

        self.rules.add((condition, transformation, condition_backward)) 

    def get(self, number:int, forward:bool=True) -> int:
        for condition, transformation, condition_backward in self.rules:
            if (forward and condition(number)):
                return transformation(number)
            elif (not forward and condition_backward(number)):
                """ Since the transformation from source to destination is f(x) = x + delta,
                    the inverse transformation from destination to source is -f(-x) = x - delta """
                return -transformation(-number)
        return number


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

    def solve_part_2_brute_force(self):
        """ Doesn't work for puzzle input. Too many cases """
        Map.init()
        self.load_input()
        get_locations = lambda x: Map.get_destination_from_source(x, 'seed', 'location')
        locations = map(get_locations, self.generate_seeds())
        return reduce(lambda x, y: min(x, y), locations)

    def solve_part_2(self):
        """ Let's solve it with 'ranges'.
            Since brute force doesn't work, a bit more of thinking is needed to solve part 2.
            Instead of trying all possible seeds, let's only focus in those that can really
            lead to a minimum location.
            Since all transformations are linear with a delta value for each range, only
            the lower boundaries of the possible ranges can lead to a final minimum.
            Hence, the strategy is to find from destination to source which are the seeds that
            at some point lead to the lower boundary of one of the ranges in one of the stages.
        """
        Map.init()
        self.load_input()

        range_boundaries = Map.get_range_boundaries_from_destination_to_source()
        seeds_and_amounts = sorted(zip(self.seeds[::2], self.seeds[1::2]), key=lambda x: x[0])

        get_locations = lambda x: Map.get_destination_from_source(x, 'seed', 'location')
        locations = map(get_locations, self.generate_seeds())

        result = max(Map.ordered[-1].destination_boundaries)
        for seed, amount in seeds_and_amounts:
            boundaries = filter(lambda x: seed <= x <= seed + amount, range_boundaries)
            results = list(map(get_locations, [seed] + list(boundaries)))
            result = min([result] + results)

        return result

    def generate_seeds(self) -> int:
        for x, y in zip(self.seeds[0::2], self.seeds[1::2]):
            for n in range(y):
                yield x + n

class Range(object):
    def __init__(self, first, last, transformations=[]):
        self.first = first
        self.last = last
        self.transformations = transformations



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
    assert(solve('puzzle_input.txt', part=2) == 20358599)

    print(solve('puzzle_input.txt', part=2))
