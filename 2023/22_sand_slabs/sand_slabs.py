''' Advent of Code 2023
    Day 22: Sand Slabs
    https://adventofcode.com/2023/day/22

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
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

        self.overlap_above = set()
        self.overlap_below = set()
        self.no_overlap = set()

        Brick.add(self)

    def can_fall(self):
        if (self.z[0] == 1):
            self.supported_by.add('ground')
            self.is_grounded = True
            return False

        if (self.is_grounded):
            return False

        bricks_directly_below = filter(lambda brick: brick.is_directly_below_of(self), self.overlap_below)
        
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

        if (not self.overlap_already_checked(brick)):
            self.check_overlap(brick)

        return (brick in self.overlap_above) 

    def check_overlap(self, brick):

        if (brick in (self.overlap_above | self.overlap_below)):
            return True
        elif (brick in (self.no_overlap)):
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

    def overlap_already_checked(self, brick):
        return brick in (self.overlap_above | self.overlap_below | self.no_overlap)

    def __str__(self):
        return "{0},{2},{4}~{1},{3},{5}".format(*(*self.x, *self.y, *self.z))
    
    @classmethod
    def add(cls, brick):
        cls.collection.add(brick)

    @classmethod
    def init(cls):
        cls.collection = set()
        cls.fallen = 0

class SandSlabs(object):

    def __init__(self, filepath:str):
        Brick.init()
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def get_bricks_with_single_support(self):

        return filter(lambda brick: len(brick.supported_by) == 1, Brick.collection)

    def get_disintegratable_briks(self):
        ''' Disintegratable bricks are those that, if removed, no other bricks would fall '''

        return Brick.collection - self.get_essential_bricks()

    def get_bricks_that_would_fall(self):
        essential_bricks = self.get_essential_bricks()
        counter = 0
        for brick in essential_bricks:
            fallen_bricks = set([brick])
            while True:
                other_bricks = filter(lambda x: x not in fallen_bricks, Brick.collection)
                other_bricks = set(filter(lambda x: len(x.supported_by - fallen_bricks) == 0, other_bricks))
                if (len(other_bricks) > 0):
                    counter += len(other_bricks)
                    fallen_bricks = fallen_bricks | other_bricks
                else:
                    break

        return counter

    def get_essential_bricks(self):
        ''' Those you shouldn't remove to prevent other bricks from falling '''
        bricks = self.get_bricks_with_single_support()
        essential_bricks = map(lambda brick: brick.supported_by, bricks)

        return set(reduce(lambda x, y: x | y, essential_bricks))


    def let_bricks_fall(self):
        bricks = sorted(Brick.collection, key=lambda brick: brick.z[0])
        
        for brick in bricks:
            for other_brick in bricks:
                if ((other_brick == brick) or brick.overlap_already_checked(other_brick)):
                    continue
                if (brick.check_overlap(other_brick)):
                    brick.overlap_above.add(other_brick)
                    other_brick.overlap_below.add(brick)
                else:
                    brick.no_overlap.add(other_brick)
                    other_brick.no_overlap.add(brick)

        print("Overlap checked")
        while (any(map(lambda brick: brick.can_fall(), filter(lambda x: not x.is_grounded, bricks)))):
            continue

    def process_input_line(self, input_line:str):
        brick_init, brick_end = input_line.split('~')
        brick_init = tuple([int(x) for x in brick_init.split(',')])
        brick_end = tuple([int(x) for x in brick_end.split(',')])
        Brick(brick_init, brick_end)


# 1. Functions that are specific for problem 1

def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    sand_slabs = SandSlabs(filepath)
    print("Number of bricks:", len(Brick.collection))
    sand_slabs.let_bricks_fall()
    print("Bricks fallen:", Brick.fallen)
    return len(sand_slabs.get_disintegratable_briks())

# 2. Functions that are specific for problem 2

def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    sand_slabs = SandSlabs(filepath)
    print("Number of bricks:", len(Brick.collection))
    sand_slabs.let_bricks_fall()
    print("Bricks fallen:", Brick.fallen)
    return sand_slabs.get_bricks_that_would_fall()

if __name__ == '__main__':
    assert(solve_part_1('test_01.txt') == 5)
    # assert(solve_part_1('puzzle_input.txt') == 401)  # Takes a minute to complete

    print(solve_part_2('test_01.txt'))
