''' Advent of Code 2023
    Day 4: Scratchcards
    https://adventofcode.com/2023/day/4
    Keywords: sets, recursion

Status:
    - Part 1:
        * Test 1: PASS
        * Puzzle: PASS
    - Part 2:
        * Test 2: PASS
        * Puzzle: PASS
'''
import re

from timeit import default_timer

line_pattern = 'Card\s+(?P<card_id>\d+)\:\s+'
line_pattern += '(?P<winning_numbers>[\d\s]+)'
line_pattern += '\s\|\s+'
line_pattern += '(?P<your_numbers>[\d\s]+)'

LINE_PATTERN = re.compile(line_pattern)
SPLIT_PATTERN = re.compile('\s+')

class Solver(object):

    def __init__(self, filepath:str):
        self.cards = {}
        self.filepath = filepath

        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

    def process_input_line(self, input_line:str):
        line = LINE_PATTERN.search(input_line)

        card_id = int(line.group('card_id'))
        winning_numbers = set(re.split(SPLIT_PATTERN, line.group('winning_numbers')))
        your_numbers = set(re.split(SPLIT_PATTERN, line.group('your_numbers')))

        your_winning_numbers = len(your_numbers & winning_numbers)

        self.cards[card_id] = your_winning_numbers

        if (your_winning_numbers) == 0:
            return


    def solve(self, part:int):
        if (part == 1):
            return self.solve_part_1()
        elif (part == 2):
            return self.solve_part_2()

    def solve_part_1(self):
        winning_cards = filter(lambda x: x > 0, self.cards.values())
        points = map(lambda x: 2 ** (x - 1), winning_cards)
        return sum(points)

    def solve_part_2(self):
        number_of_cards_won = len(self.cards)
        
        cards = [(key, value) for key, value in self.cards.items() if value > 0]

        while (len(cards) > 0):
            card_id, value = cards.pop()
            number_of_cards_won += value
            for copy_id in range(card_id + 1, card_id + value + 1):
                value = self.cards[copy_id]
                if (value > 0):
                    cards.append((copy_id, value))

        return number_of_cards_won


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
    assert(solve('test_01.txt', part=1) == 13)
    assert(solve('puzzle_input.txt', part=1) == 20107)
    assert(solve('test_01.txt', part=2) == 30)
    assert(solve('puzzle_input.txt', part=2) == 8172507)

    print(solve('puzzle_input.txt', part=2))
