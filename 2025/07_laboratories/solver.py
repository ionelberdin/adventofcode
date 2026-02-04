from timeit import default_timer
from collections.abc import Iterable


def readline(filepath:str) -> Iterable[str]:
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip('\n\b')

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    line_iter = readline(filepath)
    
    start_postition = next(line_iter).index('S')
    print(start_postition)

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
    
    assert(solve_part_1('test.txt') == 21)
    assert(solve_part_1('puzzle.txt') == None)

    assert(solve_part_2('test.txt') == None)
    assert(solve_part_2('puzzle.txt') == None)