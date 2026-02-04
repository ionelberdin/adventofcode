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

    with open(filepath) as file:
        lines = file.readlines()
        num_of_lines = len(lines)

    line_iter = readline(filepath)
    
    beams = {next(line_iter).index('S'): 1}

    splits = 1
    for line in line_iter:
        spliters = get_splitters(line)
        next_beams = {}
        for beam, multiplicity in beams.items():
            if beam in spliters:
                try:
                    next_beams[beam - 1] += multiplicity
                except:
                    next_beams[beam - 1] = multiplicity
                try:
                    next_beams[beam + 1] += multiplicity
                except:
                    next_beams[beam + 1] = multiplicity
                splits += multiplicity
            else:
                try:
                    next_beams[beam] += multiplicity
                except:
                    next_beams[beam] = multiplicity

        beams = dict(next_beams)
    
    result = splits

    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 21)
    assert(solve_part_1('puzzle.txt') == 1622)

    assert(solve_part_2('test.txt') == 40)
    assert(solve_part_2('puzzle.txt') == 10357305916520)