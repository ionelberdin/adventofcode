''' Advent of Code 2023
    Day 08: Haunted Wasteland
    https://adventofcode.com/2023/day/8

Status:
    - Part 1:
        * Test passing
        * Puzzle passing
    - Part 2:
        * Tests passing
        * Puzzle fails --> solution doesn't converge
'''
import re
from argparse import ArgumentParser
from itertools import cycle

LINE_PATTERN = re.compile('(\w+) \= \((\w+), (\w+)\)')

# 0. Functions that are common to both problems

def parse_input(filepath:str):
    with open(filepath, 'r') as f:
        directions = f.readline().strip('\n\s\t')
        f.readline()  # empty line skipped

        lines = []
        while (line := f.readline()):
            line = LINE_PATTERN.search(line)
            lines.append([line.group(x) for x in [1, 2, 3]])
    return directions, lines

def get_network(lines:list):
    return {pos: {'L': left, 'R': right} for pos, left, right in lines}

# 1. Functions that are specific for problem 1

def haunted_wasteland(filepath:str):
    directions, lines = parse_input(filepath)
    network = get_network(lines)

    goal = re.compile('ZZZ')
    return navigate(network, directions, position='AAA', goal=goal)

def navigate(network:dict, directions:str, position:str, goal:re.Pattern):
    for n, direction in enumerate(cycle(directions), 1):
        position = network[position][direction]
        if (goal.match(position)):
            return n

# 2. Functions that are specific for problem 2

def haunted_wasteland_01(filepath:str):
    directions, lines = parse_input(filepath)
    network = get_network(lines)

    INIT_POS = re.compile('\w{2}A')

    goal = re.compile('\w{2}Z')
    positions = list(filter(lambda x: INIT_POS.match(x), network))

    return navigate_all(network, directions, positions, goal)

def navigate_all(network:dict, directions:list, positions:list, goal:re.Pattern):
    for n, direction in enumerate(cycle(directions), 1):
        positions = [network[position][direction] for position in positions]
        if (any([goal.match(position) for position in positions])):
            print(n, positions, [goal.match(position) for position in positions])
        if (all([goal.match(position) for position in positions])):
            return n

if __name__ == '__main__':
    VERSIONS = {0: haunted_wasteland, 1: haunted_wasteland_01}
    parser = ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-v', '--version', type=int, default=0)
    args = parser.parse_args()
    print(VERSIONS[args.version](args.filepath))
