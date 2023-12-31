''' Advent of Code 2023
    Day 08: Haunted Wasteland
    https://adventofcode.com/2023/day/8

Status:
    - Part 1:
        * Test 1: PASS
        * Test 2: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 3: PASS 
        * Puzzle: PASS
'''
import re
from functools import reduce
from itertools import cycle
from math import gcd

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

def navigate(network:dict, directions:str, position:str, goal:re.Pattern):
    for n, direction in enumerate(cycle(directions), 1):
        position = network[position][direction]
        if (goal.match(position)):
            return n

# 1. Functions that are specific for problem 1

def haunted_wasteland_1(filepath:str):
    directions, lines = parse_input(filepath)
    network = get_network(lines)

    goal = re.compile('ZZZ')
    return navigate(network, directions, position='AAA', goal=goal)

# 2. Functions that are specific for problem 2

'''Problem 2 doesn't have a very straight forward solution, because there's 
a huge simplification that they don't explicit in the problem explanation.

Basically, it requires you to dig into the data, otherwise the solution 
may take very long to converge.

When you look into the data, you need to realise that each ghost only arrives
to a certain goal and doesn't pass through the others, and once it passes, 
it does so AGAIN and AGAIN in the same number of steps over and over.

Furthermore, all ghosts arrive to their goals in a multiple of the 
number of directions provided by the puzzle input (307 in my case).

Hence, it's only necessary to calculate how many steps each ghost takes to
arrives for the 1st time to its goal, and then calculate the least
common multiple of all of them, which is quite high --> 10921547990923.

Once you realise this, finding the solution takes no time.
'''

def haunted_wasteland_2(filepath:str):
    # Same initial parsing as in the 1st problem
    directions, lines = parse_input(filepath)
    network = get_network(lines)

    # Now the initial position requires a regular expression...
    INIT_POS = re.compile('\w{2}A')
    # ...and so does the goal as well.
    goal = re.compile('\w{2}Z')

    positions = list(filter(lambda x: INIT_POS.match(x), network))

    steps = map(lambda x: navigate(network, directions, x, goal), positions)

    # Then return the least common multiple
    # since math library doesn't have such function, but contains
    # the greatest common divisor, we do:
    # lcm(x, y) = x * y / gcd(x, y)
    return reduce(lambda x, y: int((x * y) / gcd(x, y)), steps)

if __name__ == '__main__':
    assert(haunted_wasteland_1('test_01.txt') == 2)
    assert(haunted_wasteland_1('test_02.txt') == 6)
    assert(haunted_wasteland_1('puzzle_input.txt') == 14429)
    assert(haunted_wasteland_2('test_03.txt') == 6)
    assert(haunted_wasteland_2('puzzle_input.txt') == 10921547990923)

    print(haunted_wasteland_2('puzzle_input.txt'))
