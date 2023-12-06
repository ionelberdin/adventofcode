'''
https://adventofcode.com/2023/day/6
'''

import re

from argparse import ArgumentParser
from functools import reduce
from math import sqrt

''' It's a mathematical problem.
Parameters:
- TotalTime (t)
- MinDistance (d)

Unknowns:
- Distance (x)
- ChargingTime (tc)
- MovingTime (tm)
- Speed (v)

Constraints (Equations):
    t = tc + tm
    x = tm * v
    v = tc (weird but given...)

Combining those 3 equations:
    x = (t - tc) * tc
which has a MaxDistance (xmax) for tc = t/2
    xmax = (tc^2)/2

Forcing x > d we get:
    tm^2 - t * tm + d = 0
Which have 2 solutions when:
    t^2 > 4 * d

The MovingTime thresholds to win are:
    tm1 = (t - sqrt(t^2 - 4 * d)) / 2
    tm2 = (t + sqrt(t^2 - 4 * d)) / 2
'''


def wait_for_it(filepath):
    with open(filepath, 'r') as f:
        times = map(int, BLANKS.split(f.readline().strip())[1:])
        distances = map(int, BLANKS.split(f.readline().strip())[1:])
    ways_to_win = map(get_ways_to_win, times, distances)
    return reduce(lambda x, y: x * y, ways_to_win)

BLANKS = re.compile('[\s\t]+')
EPS = 1e-10  # to exclude the upper threshold from the possible solutions

def get_ways_to_win(t, d):
    if ((sq := (t * t - 4 * d)) <= 0):
        return 0
    tm1 = (t - (sq := (sqrt(sq)))) / 2
    tm2 = (t + sq) / 2
    return int(tm2 - EPS) - int(tm1)


''' The 2nd problem can be solved with the same approach, only
    the first parse needs to be modified and, since the input are combined,
    there's no need for a reduce in this case
'''

def wait_for_it_01(filepath):
    with open(filepath, 'r') as f:
        t = int(''.join(BLANKS.split(f.readline().strip())[1:]))
        d = int(''.join(BLANKS.split(f.readline().strip())[1:]))
    return get_ways_to_win(t, d)

if __name__ == '__main__':
    VERSIONS = {0: wait_for_it, 1: wait_for_it_01}
    parser = ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-v', '--version', default=0, type=int)
    args = parser.parse_args()
    
    print(VERSIONS[args.version](args.filepath))
