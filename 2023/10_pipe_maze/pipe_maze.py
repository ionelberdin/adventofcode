''' Advent of Code 2023
    Day 10: Pipe Maze
    https://adventofcode.com/2023/day/10

Status:
    - Part 1:
        * Test 1: PASS
        * Test 2: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 3: PASS
        * Test 4: PASS
        * Test 5: PASS
        * Puzzle: PASS
'''

# 0. Functions that are common to both problems


class Maze(object):

    TILE_MAP = {
        '|': ((1, 0), (-1, 0)),
        '-': ((0, 1), (0, -1)),
        'L': ((-1, 0), (0, 1)),
        'J': ((-1, 0), (0, -1)),
        '7': ((1, 0), (0, -1)),
        'F': ((1, 0), (0, 1)),
        'S': ((1, 0), (0, 1), (0, -1), (-1, 0))
    }

    def __init__(self, filepath:str):
        with open(filepath, 'r') as f:
            self.map = [x.strip('\n\s\t') for x in f.readlines()]
        self.number_of_rows = len(self.map)
        self.number_of_columns = len(self.map[0])
        self.start = self.find_tile_position('S')
        self.restart()

    def find_tile_position(self, what:str):
        for row_index, row in enumerate(self.map):
            if (col_index := row.find(what)) > -1:
                return (row_index, col_index)
        return None

    def get_tile(self, position):
        return self.map[position[0]][position[1]]

    def is_wrong_move(self, position, direction):

        is_wrong = ((position is None) or
                    (position in self.visited) or
                    (self.direction == (reversed_direction := (-direction[0], -direction[1]))) or
                    ((tile := self.get_tile(position)) not in self.TILE_MAP) or
                    (reversed_direction not in self.TILE_MAP[tile]))
        return is_wrong

    def move(self, direction=None):
        directions = direction or self.TILE_MAP[self.get_tile(self.position)]

        for direction in directions:
            position = self.sum(self.position, direction)
            if (self.is_wrong_move(position, direction)):
                continue

            self.visited.append(position)
            self.position = position
            self.direction = direction
            tile = self.get_tile(position)

            if (tile == 'S'):
                return False

            return True

        return None

    def restart(self):
        self.position = self.start
        self.visited = []
        self.direction = (0, 0)

    def sum(self, position:tuple[int, int], direction:tuple[int, int]):
        position = (position[0] + direction[0], position[1] + direction[1])
        row_in_range = (0 <= position[0] <= self.number_of_rows)
        column_in_range = (0 <= position[1] <= self.number_of_columns)
        return position if (row_in_range and column_in_range) else None


def solve_maze(filepath:str):
    maze = Maze(filepath)
    for direction in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        maze.restart()
        keep_moving = maze.move([direction])
        while (keep_moving):
            keep_moving = maze.move()
            if keep_moving is None:
                continue
        if keep_moving is False:
            break
    else:
        return None

    return maze

# 1. Functions that are specific for problem 1

def pipe_maze_1(filepath:str):
    maze = solve_maze(filepath)
    return int(len(maze.visited) / 2)

# 2. Functions that are specific for problem 2

def pipe_maze_2(filepath:str):
    ''' The key to this problem is realising that the inner points can be
        obtained knowing the inner area and the external perimiter.
        For a given area, the inner points are:
            InnerPoints = (MaxPerimiter - Perimiter) / 2
        where:
            MaxPerimiter = 2 * (Area + 1)
    '''
    maze = solve_maze(filepath)
    perimiter = len(maze.visited)
    area = integrate_manhattan_line([maze.start] + maze.visited)
    max_perimiter = 2 * (area + 1)
    return int((max_perimiter - perimiter) / 2)


def integrate_manhattan_line(points):
    ''' All segments son either horizontal or vertical and in any case
        they all have unitary lenght. Hence, integrating them is just
        adding triangles in which:
           the base is 1
           the height is the orthogonal distance of the segment to the origin
        since all triangles are half of the product of their base by their height,
        the division by 2 is left for the end.
        Since the direction of integration is arbitrary, the result could
        be negative, that's why its absolute value is taken.
        And finally, since we are counting squares, the result must be an integer.
    '''
    area = 0
    for a, b in zip(points[:-1], points[1:]):
        ax, ay = a
        bx, by = b
        area += ax * (by - ay) if (ax == bx) else ay * (ax - bx)
    return int(abs(area / 2))


if __name__ == '__main__':
    assert(pipe_maze_1('test_01.txt') == 4)
    assert(pipe_maze_1('test_02.txt') == 8)
    assert(pipe_maze_1('puzzle_input.txt') == 6733)
    assert(pipe_maze_2('test_03.txt') == 4)
    assert(pipe_maze_2('test_04.txt') == 8)
    assert(pipe_maze_2('test_05.txt') == 10)
    assert(pipe_maze_2('puzzle_input.txt') == 435)

    print(pipe_maze_2('puzzle_input.txt'))
