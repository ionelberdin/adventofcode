# Day 7: Laboratories

[https://adventofcode.com/2025/day/7]

Tags: {tags}

## Part 1

- Parsing type: LineByLine
- Difficulty (0/9): {part1_dificulty}
- Development time (0:15): {part1_develpment_time}
- Lines of code (int): {part1_lines_of_code}
- Test status (PASS|FAIL): {part1_test_status}
- Puzzle status (PASS|FAIL): {part1_puzzle_status}

## Part 2

- Parsing type: {part2_parsing_type}
- Difficulty (0/9): {part2_dificulty}
- Development time (0:30): {part2_develpment_time}
- Lines of code (int): {part2_lines_of_code}
- Test status (PASS|FAIL): {part2_test_status}
- Puzzle status (PASS|FAIL): {part2_puzzle_status}

First try was brute force adding the timelines to a list.
That doesn't work, too many timelines.
In the end I combined different timelines going through the same path adding
a multiplicity integer and using a dictionary instead of a list.