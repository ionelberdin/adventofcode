# Day 5: Cafeteria
https://adventofcode.com/2025/day/5

## Part 1
Parsing first part of the input file is necessary to load the available ranges.
The ranges can be merged when they intersect.

The ranges are consolidated to have the minimum number of ranges needed.
This is actually not necessary, but could help improving performance for long
lists of numbers to check.

Solving part 1 with: test.txt
2 ranges considered
Result of part 1: 3 (0.00032359990291297436s)
Solving part 1 with: puzzle.txt
98 ranges considered
Result of part 1: 828 (0.005678099929355085s)

Comparison with the simple solution in which ranges are not consolidated:
Solving part 1 with: test.txt
4 ranges considered
Result of part 1: 3 (0.00032350001856684685s)
Solving part 1 with: puzzle.txt
174 ranges considered
Result of part 1: 828 (0.00579450000077486s)

Actually, both solutions are comparable in time, hence it seems in the puzzle
case there's an equilibrium between number of ranges and test numbers in the
input file.

If there were many more test numbers, then the consolidation could help.

## Part 2
For part 2 the consolidation seems quite handy.