''' Advent of Code 2023
    Day 25: Snowoverload
    https://adventofcode.com/2023/day/25
    Keywords: Dictionaries, Sets, Connections

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from itertools import combinations
from timeit import default_timer


class Solver(object):
    
    SPLIT_PATTERN = re.compile('[\:\s]+')
    def __init__(self, filepath:str):
        self.connectors = set()
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def process_input_line(self, input_line:str):
        components = self.SPLIT_PATTERN.split(input_line)
        for other in components[1:]:
            self.connectors.add((components[0], other))

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        all_components = set([x for y in self.connectors for x in y])
        print("Components", len(all_components))
        print("Conectors:", len(self.connectors))
        groups = self.get_groups(self.connectors)
        print("Groups:", len(groups))
        connectors_comb = combinations(self.connectors, len(self.connectors) - 3)
        groups_comp = map(lambda x: self.get_groups(set(x)), connectors_comb)
        solution = next(filter(lambda x: len(x) == 2, groups_comp), None)

        return len(solution[0]) * len(solution[1]) if solution is not None else None

    def solve_part_2(self):
        return None

    @staticmethod
    def get_groups(connectors):
        groups = [set(connectors.pop())]

        for component_1, component_2 in connectors:
            group_1 = next(filter(lambda x: component_1 in x, groups), None)
            group_2 = next(filter(lambda x: component_2 in x, groups), None)

            if ((group_1 is None) and (group_2 is None)):
                groups.append(set([component_1, component_2]))
            elif ((group_1 is None) and (group_2 is not None)):
                group_2.add(component_1)
            elif ((group_1 is not None) and (group_2 is None)):
                group_1.add(component_2)
            elif (group_1 != group_2):
                group_1 |= group_2
                groups.pop(groups.index(group_2))
            else:  # both components already in the same group
                pass

        return groups


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
    assert(solve('test_01.txt', part=1) == 54)
    # assert(solve('puzzle_input.txt', part=1) == TBD)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('test_01.txt', part=1))
    # print(solve('puzzle_input.txt', part=1))
