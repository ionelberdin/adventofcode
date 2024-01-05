''' Advent of Code 2023
    Day 3: Gear Ratios
    https://adventofcode.com/2023/day/3
    Keywords: {List of keywords}

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import re

from functools import reduce
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
            column_number += len(element)
    
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

    def show_numbers_with_adjoining_elements(self):

        for number_and_position in self.numbers:
            number, position = number_and_position
            row_number, column_number = position        
            row_min = row_number - 1 if row_number > 0 else 0
            row_max = row_number + 2
            col_min = column_number - 1 if column_number > 0 else 0
            col_max = column_number + len(number) + 1

            has = self.has_any_adjoining_symbol(number_and_position)
            a = {True: "\033[92m", False: "\033[93m"}
            print(f"{a[has]}{number_and_position}\033[0m")
            for row in self.rows[row_min:row_max]:
                print(f"{a[has]}{row[col_min:col_max]}\033[0m")
            print()

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

        self.symbol_positions = set(map(lambda x: x[1], self.symbols))

        # self.show_numbers_with_adjoining_elements()

        numbers = filter(self.has_any_adjoining_symbol, self.numbers)

        return sum(list(map(lambda x: int(x[0]), numbers)))

    def solve_part_2(self):
        """ Strategy:
            1. Find gears: star symbols with exactly 2 adjacent numbers.
            2. Get their gear ratio.
            3. Sum the gear ratio of all gears.
        """
        gears = self.find_gears()
        gear_ratios = map(lambda gear: gear[2][0] * gear[2][1], gears)

        return reduce(sum, gear_ratios)

    def find_gears(self):
        stars = set(filter(lambda x: x[0] == '*', self.symbols))
        stars = map(lambda x: (x[0], x[1], self.get_adjoining_numbers(x)), stars)
        gears = filter(lambda x: len(x[2]) == 2, stars)
        return set(gears)

    def get_adjoining_numbers(self, symbol_and_position):
        symbol, position = symbol_and_position
        row_number, column_number = position
        numbers = filter(lambda x: abs(row_number - x[1][0]) <= 1, self.numbers)
        numbers = filter(lambda x: (x[1][1] - len(x[0])) <= column_number <= (column_number + 1, numbers)  # FIXME
        return set(numbers)



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
    assert(solve('puzzle_input.txt', part=1) == 553825)
    # assert(solve('test_01.txt', part=2) == TBD)
    # assert(solve('puzzle_input.txt', part=2) == TBD)

    print(solve('test_01.txt', part=2))
