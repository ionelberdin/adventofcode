''' Advent of Code 2023
    Day 22: Sand Slabs
    https://adventofcode.com/2023/day/22

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

from functools import reduce

# 0. Code common to both parts of the problem
class Brick(object):

    collection = set()
    fallen = 0

    def __init__(self, brick_init, brick_end):
        x0, y0, z0 = brick_init
        x1, y1, z1 = brick_end
        self.x = tuple(sorted([x0, x1]))
        self.y = tuple(sorted([y0, y1]))
        self.z = tuple(sorted([z0, z1]))

        self.is_grounded = False
        self.supported_by = set()

        Brick.add(self)

    def can_fall(self):
        if (self.z[0] == 1):
            self.supported_by.add('ground')
            self.is_grounded = True
            return False

        if (self.is_grounded):
            return False

        other_bricks = filter(lambda brick: brick is not self, Brick.collection)
        bricks_directly_below = filter(lambda brick: brick.is_directly_below_of(self), other_bricks)
        
        if (len(bricks_directly_below := list(bricks_directly_below)) > 0):
            for brick in bricks_directly_below:
                self.supported_by.add(brick)
                if (brick.is_grounded):
                    self.is_grounded = True
            return False

        self.z = (self.z[0] - 1, self.z[-1] - 1)
        Brick.fallen += 1
        return True

    def is_directly_below_of(self, brick):
        ''' Checks if self is directly below brick '''
        if (brick.z[0] != self.z[-1] + 1):
            return False

        x_overlap = ((brick.x[0] <= self.x[0] <= brick.x[-1]) or
                     (brick.x[0] <= self.x[-1] <= brick.x[-1]) or
                     ((brick.x[0] > self.x[0]) and (self.x[-1] > brick.x[-1])))

        y_overlap = ((brick.y[0] <= self.y[0] <= brick.y[-1]) or
                     (brick.y[0] <= self.y[-1] <= brick.y[-1]) or
                     ((brick.y[0] > self.y[0]) and (self.y[-1] > brick.y[-1])))

        if (x_overlap and y_overlap):
            return True

        return False

    @classmethod
    def add(cls, brick):
        cls.collection.add(brick)

    @classmethod
    def init(cls):

        cls.collection = set()

class SandSlabs(object):

    def __init__(self, filepath:str):
        Brick.init()
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def get_disintegratable_briks(self):
        ''' Disintegratable bricks are those that, if removed, no other bricks would fall '''
        bricks_with_only_one_support = filter(lambda brick: len(brick.supported_by) == 1, Brick.collection)
        essential_bricks = map(lambda brick: brick.supported_by, bricks_with_only_one_support)
        essential_bricks = set(reduce(lambda x, y: x | y, essential_bricks))

        return Brick.collection - essential_bricks

    def let_bricks_fall(self):
        bricks = sorted(Brick.collection, key=lambda brick: brick.z[0])
        while (any(map(lambda brick: brick.can_fall(), filter(lambda x: not x.is_grounded, bricks)))):
            print
            continue

    def process_input_line(self, input_line:str):
        brick_init, brick_end = input_line.split('~')
        brick_init = tuple([int(x) for x in brick_init.split(',')])
        brick_end = tuple([int(x) for x in brick_end.split(',')])
        Brick(brick_init, brick_end)


# 1. Functions that are specific for problem 1

def solve_part_1(filepath:str):
    sand_slabs = SandSlabs(filepath)
    print("Number of bricks:", len(Brick.collection))
    sand_slabs.let_bricks_fall()
    print("Bricks fallen:", Brick.fallen)
    return len(sand_slabs.get_disintegratable_briks())

# 2. Functions that are specific for problem 2

if __name__ == '__main__':
    assert(solve_part_1('test_01.txt') == 5)
    # assert(pipe_maze_1('puzzle_input.txt') == 6733)

    print(solve_part_1('puzzle_input.txt'))
