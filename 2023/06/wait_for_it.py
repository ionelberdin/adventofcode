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

# Let's compile a regular expression to identify non-digit chars.

def wait_for_it(filepath):
    with open(filepath, 'r') as f:
        return reduce(lambda x, y: x * y, get_ways_to_win(f))

BLANKS = re.compile('[\s\t]+')
EPS = 1e-10  # to exclude the upper limit from the possible solutions

def get_ways_to_win(f):
    times = [int(t) for t in BLANKS.split(f.readline().strip())[1:]]
    distances = [int(d) for d in BLANKS.split(f.readline().strip())[1:]]
    for t, d in zip(times, distances):
        if ((sq := (t * t - 4 * d)) <= 0):
            yield 0
        tm1 = (t - (sq := (sqrt(sq)))) / 2
        tm2 = (t + sq) / 2
        print(t, d, tm1, tm2, int(tm2) - int(tm1)
)
        yield int(tm2 - EPS) - int(tm1)


def wait_for_it_01(filepath):
    pass

if __name__ == '__main__':
    VERSIONS = {0: wait_for_it, 1: wait_for_it_01}
    parser = ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-v', '--version', default=0, type=int)
    args = parser.parse_args()
    
    print(VERSIONS[args.version](args.filepath))
