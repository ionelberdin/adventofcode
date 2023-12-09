''' Advent of Code 2023
    Day 2: Cube Conundrum 
    https://adventofcode.com/2023/day/2

Status:
    * Part 1:
        - Test 1: PASS
        - Puzzle: PASS
    * Part 2:
        - Test 1: PASS
        - Puzzle: PASS

'''

import re

from collections import Counter
from functools import reduce

''' The idea to solve the 1st problem is to:
1. Parse each line.
2. Use a Counter object to get the max value of each color occurrence.
3. Compare the build Counter with the Limit provided.
4. Filter out impossible games.
5. Sum the IDs of the possible ones.
'''

# 0. Common to both parts 

class Game(object):
    LINE = re.compile('Game (\d+): (.+)')

    def __init__(self, line):
        line = self.LINE.search(line)
        self.id = int(line.group(1))
        hands = [[y.split(' ') for y in x.split(', ')] for x in line.group(2).split('; ')]
        self.hands = [Counter({y: int(x) for x, y in z}) for z in hands]

    @property
    def min(self):
        return reduce(lambda x, y: x | y, self.hands)

def parse_input(filepath):
    with open(filepath, 'r') as f:
        while (line := f.readline().strip('\n\s\t')):
            yield line

# 1. Specific to part 1
    
def cube_conundrum_1(filepath):

    games = [Game(line) for line in parse_input(filepath)]

    game_max = Counter(red=12, green=13, blue=14)
    possible_games = filter(lambda g: g.min <= game_max, games)
    return sum(map(lambda x: x.id, possible_games))

# 2. Specific to part 2

def cube_conundrum_2(filepath):

    games = [Game(line) for line in parse_input(filepath)]

    return sum(map(lambda x: reduce(lambda y, z: y * z, x.min.values()), games))

if __name__ == '__main__':
    assert(cube_conundrum_1('test_01.txt') == 8)
    assert(cube_conundrum_1('puzzle_input.txt') == 2239)

    print(cube_conundrum_2('puzzle_input.txt'))
