''' Day 2: Cube Conundrum 
https://adventofcode.com/2023/day/2
'''

import re

from argparse import ArgumentParser
from collections import Counter
from functools import reduce

''' The idea to solve the 1st problem is to:
1. Parse each line.
2. Use a Counter object to get the max value of each color occurrence.
3. Compare the build Counter with the Limit provided.
4. Filter out impossible games.
5. Sum the IDs of the possible ones.
'''

LINE = re.compile('Game (\d+): (.+)')

def cube_conundrum(filepath):
    game_max = Counter(red=12, green=13, blue=12)
    with open(filepath, 'r') as f:
        possible_games = filter(lambda x: is_game_possible(x[1], game_max), get_games(f))
        return reduce(lambda x, y: x + y, map(lambda x: x[0], possible_games))

def is_game_possible(game, game_max):
    return game <= game_max

def get_games(f):
    return map(parse_line, read_lines(f))

def read_lines(f):
    while (line := f.readline()):
        yield line.strip(' \n\t\s')


def parse_line(line):
    line = LINE.search(line)
    game = reduce(lambda x, y: x | y, map(parse_hand, line.group(2).split('; ')))
    return int(line.group(1)), game

def parse_hand(hand):
    return Counter({y: int(x) for x, y in [z.split(' ') for z in hand.split(', ')]})

def cube_conundrum_01(filepath):
    with open(filepath, 'r') as f:
        return reduce(lambda x, y: x + y, get_ids_of_possible_games(f))

if __name__ == '__main__':
    VERSIONS = {0: cube_conundrum, 1: cube_conundrum_01}
    parser = ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-v', '--version', default=0, type=int)
    args = parser.parse_args()
    
    print(VERSIONS[args.version](args.filepath))
