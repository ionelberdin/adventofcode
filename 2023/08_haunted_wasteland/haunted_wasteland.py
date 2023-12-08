import re
from argparse import ArgumentParser
from itertools import cycle

LINE = re.compile('(\w+) \= \((\w+), (\w+)\)')

def haunted_wasteland(filepath):
    directions, lines = process_input(filepath)
    network = get_network(lines)

    goal = re.compile('ZZZ')
    return navigate(network, directions, position='AAA', goal=goal)

def process_input(filepath):
    with open(filepath, 'r') as f:
        directions = f.readline().strip('\n\s\t')
        f.readline()  # empty line skipped

        lines = []
        while (line := f.readline()):
            line = LINE.search(line)
            lines.append([line.group(x) for x in [1, 2, 3]])
    return directions, lines

def get_network(lines):
    return {pos: {'L': left, 'R': right} for pos, left, right in lines}

def navigate(network, directions, position, goal):
    for n, direction in enumerate(cycle(directions), 1):
        position = network[position][direction]
        if (goal.match(position)):
            return n

def haunted_wasteland_01(filepath):
    directions, lines = process_input(filepath)
    network = get_network(lines)

    INIT_POS = re.compile('\w{2}A')

    goal = re.compile('\w{2}Z')
    positions = list(filter(lambda x: INIT_POS.match(x), network))

    return navigate_all(network, directions, positions, goal)

def navigate_all(network, directions, positions, goal):
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
