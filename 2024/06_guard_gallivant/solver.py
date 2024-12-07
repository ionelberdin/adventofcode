''' Advent of Code 2024
    Day 6: Guard Gallivant
    https://adventofcode.com/2024/day/6

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from timeit import default_timer
# import copy  # copy.deepcopy(lines) takes x3 time

move = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
change = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def parse_file(filepath:str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = list(map(lambda x: x.strip('\n\s\t'), file.readlines()))
    
    for n, line in enumerate(lines):
        for direction in '^>v<':
            if direction in line:
                position = (n, line.index(direction))
                return position, direction, lines

def get_visited(position, direction, lines):
    x_max, y_max = len(lines), len(lines[0])
    x, y = position
    dx, dy = move[direction]
    visited = set([(x, y)])
    history = set([(x, y, direction)])
    while ((0 <= x + dx < x_max) and (0<= y + dy < y_max)):
        while (lines[x + dx][y + dy] == '#'):
            direction = change[direction]
            dx, dy = move[direction]
        x += dx
        y += dy
        visited.add((x, y))
        if (x, y, direction) in history:
            raise Exception('Infinite Loop')
        history.add((x, y, direction))
    return visited

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    start = default_timer()
    position, direction, lines = parse_file(filepath)

    result = len(get_visited(position, direction, lines))

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result

def count_loop_possibilities(position, direction, lines):
    #lines = [[symbol for symbol in line] for line in lines]
    possibilities = 0
    visited = get_visited(position, direction, lines)
    visited.remove(position)
    for x, y in visited:
        possibility = [[symbol for symbol in line] for line in lines]
        #possibility = copy.deepcopy(lines) takes x3 time
        possibility[x][y] = '#'
        
        try:
            get_visited(position, direction, possibility)
        except:
            possibilities +=1
    return possibilities

def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    start = default_timer()
    position, direction, lines = parse_file(filepath)
    result = count_loop_possibilities(position, direction, lines)
    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 41)
    assert(solve_part_1('puzzle.txt') == 5145)

    assert(solve_part_2('test.txt') == 6)
    assert(solve_part_2('puzzle.txt') == 1523)