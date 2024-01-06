''' Advent of Code 2023
    Day 3: Gear Ratios
    https://adventofcode.com/2023/day/3
    Keywords: adjacent

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: PASS
        * Puzzle: PASS
'''

import re

from functools import reduce
from timeit import default_timer

INT_PATTERN = re.compile('\d+')
SYMBOL_PATTERN = re.compile('[^\d\.]{1}')

class Solver(object):

    def __init__(self, filepath:str):
        self.filepath = filepath

        self.numbers = set()
        self.symbols = set()

        with open(filepath, 'r') as f:
            rows = f.readlines()

        self.rows = list(map(lambda x: x.strip('\n\s\t'), rows))

        for row_number, row in enumerate(self.rows):
            self.numbers |= self.findall_and_positions(INT_PATTERN, row_number)
            self.symbols |= self.findall_and_positions(SYMBOL_PATTERN, row_number)

    def findall_and_positions(self, pattern:re.Pattern, row_number:int) -> set[tuple[str, tuple[int, int]]]:
        """ Given a regular expression pattern and i row number,
            this method finds the elements that match the given pattern within the row,
            and return them in a set of tuples together with their positions
            in row and column fashion 
            Result: set(tuple((element, (row_number, column_number))), ...) """

        row = self.rows[row_number]
        elements = pattern.findall(row)
        elements_and_positions = set()
        column_number = 0
        for n, element in enumerate(elements):
            column_number = row.index(element, column_number)
            elements_and_positions.add((element, (row_number, column_number)))
            # The column_number needs to be increased with the length of the 
            # element processed to continue in the next iteration the search
            # of the index of the next element after the end of the last.
            column_number += len(element)
    
        return elements_and_positions

    def find_gears(self) -> set[tuple[str, tuple[int, int], tuple[tuple[str, tuple[int, int], ]]]]:
        """ According to the problem text, gears are star symbols which have
            exactly 2 adjacent numbers, and those are the ones retrieved and
            returned by this function. """
        stars = filter(lambda x: x[0] == '*', self.symbols)
        stars = map(lambda x: (x[0], x[1], self.get_adjacent_numbers(x)), stars)
        gears = filter(lambda x: len(x[2]) == 2, stars)
        return set(gears)

    def get_adjacent_numbers(self, symbol_and_position) -> tuple[tuple[str, tuple[int, int]], ]:
        """ For any given symbol with its position, this function finds the adjacent
            numbers with their positions, and returns them all as a tuple. """
        symbol, position = symbol_and_position
        row_number, column_number = position

        numbers = filter(lambda x: abs(row_number - x[1][0]) <= 1, self.numbers)
        numbers = filter(lambda x: (column_number - len(x[0])) <= x[1][1], numbers)
        numbers = filter(lambda x: x[1][1] <= (column_number + 1), numbers)

        return tuple(numbers)

    def has_any_adjacent_symbol(self, number_and_position:tuple[str, tuple[int, int]]) -> bool:
        """ For any given number with its position, this function checks if it has any
            adjacent symbol. If so, it returns True, otherwise False. """

        number, position = number_and_position
        row_number, column_number = position

        min_column = column_number - 1
        max_column = column_number + len(number)

        symbol_positions = filter(lambda x: abs(x[0] - row_number) <= 1, self.symbol_positions)
        symbol_positions = filter(lambda x: min_column <= x[1], symbol_positions)
        symbol_positions = filter(lambda x: x[1] <= max_column, symbol_positions)
        
        return next(symbol_positions, None) is not None

    def show_numbers_with_adjacent_elements(self) -> None:
        """ Helper method for debugging purposes.
            It prints all the numbers found with their adjacent chars """

        for number_and_position in self.numbers:
            number, position = number_and_position
            row_number, column_number = position        
            row_min = row_number - 1 if row_number > 0 else 0
            row_max = row_number + 2
            col_min = column_number - 1 if column_number > 0 else 0
            col_max = column_number + len(number) + 1

            has = self.has_any_adjacent_symbol(number_and_position)
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

    def solve_part_1(self) -> int:
        """ Strategy:
            1. Get numbers and their position. (done in __init__)
            2. Get symbols and their position. (done in __init__)
            3. Filter out numbers that don't have any adjacent symbol.
            4. Sum the rest.
            """

        symbols = set(map(lambda x: x[0], self.symbols))

        self.symbol_positions = set(map(lambda x: x[1], self.symbols))

        numbers = filter(self.has_any_adjacent_symbol, self.numbers)

        return sum(list(map(lambda x: int(x[0]), numbers)))

    def solve_part_2(self) -> int:
        """ Strategy:
            1. Get numbers and their position. (done in __init__)
            2. Get symbols and their position. (done in __init__)
            3. Find gears: star symbols with exactly 2 adjacent numbers.
            4. Get their gear ratio.
            5. Sum the gear ratio of all gears.
        """

        gears = self.find_gears()
        gear_ratios = map(lambda x: int(x[2][0][0]) * int(x[2][1][0]), gears)

        return reduce(lambda x, y: x + y, gear_ratios)


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
    assert(solve('test_01.txt', part=2) == 467835)
    assert(solve('puzzle_input.txt', part=2) == 93994191)

    print(solve('puzzle_input.txt', part=2))
