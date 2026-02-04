from timeit import default_timer
from itertools import combinations

def parse_line(line:str) -> tuple[int,int,int]:
    return tuple(list(map(int, line.strip('\n').split(','))))

def readfile(filepath:str) -> set[tuple[int]]:
    with open(filepath, 'r') as file:
        lines = set(map(parse_line, file))
    return lines

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    points = readfile(filepath)
    for a, b in combinations(points, 2):
        

    result = 0

    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result


def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    result = 0

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == None)
    assert(solve_part_1('puzzle.txt') == None)

    assert(solve_part_2('test.txt') == None)
    assert(solve_part_2('puzzle.txt') == None)