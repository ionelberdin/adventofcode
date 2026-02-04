from timeit import default_timer
from collections.abc import Iterable


def readline(filepath:str) -> Iterable[str]:
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip('\n\b')

def get_splitters(line):
    indices = set()
    last_index = 0
    while True:
        try:
            i = line.index('^', last_index)
            indices.add(i)
            last_index = i + 1
        except:
            return indices

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    line_iter = readline(filepath)
    
    beams = set([next(line_iter).index('S')])

    splits = 0
    for line in line_iter:
        spliters = get_splitters(line)
        beam_splits = spliters.intersection(beams)
        splits += len(beam_splits)
        beams = beams - spliters
        for beam_split in beam_splits:
            beams.add(beam_split - 1)
            beams.add(beam_split + 1)
    
    result = splits

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
    assert(solve_part_1('puzzle.txt') == 1622)

    assert(solve_part_2('test.txt') == None)
    assert(solve_part_2('puzzle.txt') == None)