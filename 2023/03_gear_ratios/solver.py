''' Advent of Code 2023
    Day 3: Gear Ratios
    https://adventofcode.com/2023/day/3
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from timeit import default_timer

INT_PATTERN = re.compile('\d+')
SYMBOL_PATTERN = re.compile('[^\d\.]{1}')

class Solver(object):

    def __init__(self, filepath:str):
        self.numbers = set()
        self.symbols = set()

        with open(filepath, 'r') as f:
            rows = f.readlines()
        self.rows = list(map(lambda x: x.strip('\n\s\t'), rows))

    @staticmethod
    def findall_and_positions(pattern:re.Pattern, row:str, row_number:int):
        """ Given a regular expression pattern, a row, and its row number,
            this method finds the elements that match the given pattern within the row,
            and return them in a set of tuples together with their positions
            in row and column fashion 
            Result: set(tuple((element, (row_number, column_number))), ...) """

        elements = pattern.findall(row)
        elements_and_positions = set()
        column_number = 0
        for n, element in enumerate(elements):
            column_number = row.index(element, column_number)
            elements_and_positions.add((element, (row_number, column_number)))
            column_number += 1
    
        return elements_and_positions

    def has_any_adjoining_symbol(self, number_and_position):

        number, position = number_and_position
        row, column = position
        lenght = len(number)
        r0 = row - 1
        r1 = row + 1
        c0 = column - 1
        c1 = column + lenght

        symbol_positions = filter(lambda x: (r0 <= x[0] <= r1), self.symbol_positions)
        symbol_positions = filter(lambda x: (c0 <= x[1] <= c1), symbol_positions)
        
        return next(symbol_positions, None) is not None

    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        """ Strategy:
            1. Get numbers and their position.
            2. Get symbols and their position.
            3. Filter out numbers that don't have any adjoining symbol.
            4. Sum the rest.
            """
        for row_number, row in enumerate(self.rows):
            self.numbers |= self.findall_and_positions(INT_PATTERN, row, row_number)
            self.symbols |= self.findall_and_positions(SYMBOL_PATTERN, row, row_number)
        symbols = set(map(lambda x: x[0], self.symbols))
        print(len(self.rows), len(self.numbers), len(self.symbols), len(symbols))
        print("".join(symbols))

        self.symbol_positions = set(map(lambda x: x[1], self.symbols))

        numbers = filter(self.has_any_adjoining_symbol, self.numbers)

        return sum(list(map(lambda x: int(x[0]), numbers)))

    def solve_part_2(self):
        return None


def solve(filepath:str, part:int):
    print("Solving part {} with:".format(part), filepath)
    start = default_timer()
    solver = Solver(filepath)
    result = solver.solve(part=part)
    duration = default_timer() - start
    print("Solved in {}s".format(duration))
    print("Result:", result)
    return result


if __name__ == '__main__':
    assert(solve('test_01.txt', part=1) == 4361)
    # assert(solve('puzzle_input.txt', part=1) == TBD)  # 553806 < x < 557509
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('puzzle_input.txt', part=1))
