''' Advent of Code 2024
    Day 9: Disk Fragmenter
    https://adventofcode.com/2024/day/9

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from timeit import default_timer
from functools import reduce
from itertools import combinations

def parse_file(filepath:str) -> list[list[str]]:
    with open(filepath, 'r') as file:
        return file.readline().strip('\n\s\t')

def get_products(diskmap):
    if len(diskmap) % 2 == 0:
        diskmap = diskmap[:-1]
    last_id = int((len(diskmap) - 1) / 2)
    forward = map(int, diskmap)
    file_id_from_the_right = get_id_from_the_right(diskmap, last_id)
    position = 0
    for i, number in enumerate(forward):
        if i % 2 == 0:
            file_id = int(i / 2)
            if file_id == last_id:
                while(file_id == next(file_id_from_the_right)):
                    yield position * file_id
                    position += 1
                break
            for _ in range(number):
                yield position * file_id
                position += 1
        else:
            for _ in range(number):
                last_id = next(file_id_from_the_right)
                if last_id == file_id:
                    break
                yield position * last_id
                position += 1
        if last_id == file_id:
                    break
    
def get_id_from_the_right(elements, last_id):
    for i, element in enumerate(elements[::-1]):
        if i % 2 == 0:
            for _ in range(int(element)):
                yield last_id
            last_id -= 1

def solve_part_1(filepath:str) -> int:
    print("Solving part 1 with:", filepath)
    start = default_timer()
    
    diskmap = parse_file(filepath)
        
    products = get_products(diskmap)
    result = reduce(lambda x, y: x + y, products)


    duration = default_timer() - start
    print(f"Result of part 1: {result} ({duration}s)")
    return result

def get_files(diskmap):
    position = 0
    for i, number in enumerate(map(int, diskmap)):
        if i % 2 == 0:
            yield (position, number, int(i / 2))
            position += number
        else:
            position +=number

def get_spaces(diskmap):
    position = 0
    for i, number in enumerate(map(int, diskmap)):
        if i % 2 == 0:
            position += number
        else:
            yield (position, number)
            position +=number

def get_products_moving_whole_files(files, spaces):
    spaces.append(None)
    for file in files[::-1]:
        spaces.pop()
        position, number, file_id = file
        try:
            space_index = find_space(number, spaces)
            position, space_number = spaces[space_index]
            spaces[space_index] = (position + number, space_number - number)
        except Exception as err:
            pass
        for i in range(number):
            yield (position + i ) * file_id

def find_space(number, spaces):
    for n, (_, space_number) in enumerate(spaces):
        if number <= space_number:
            return n
    raise Exception("Space not found.")

def solve_part_2(filepath:str) -> int:
    print("Solving part 2 with:", filepath)
    start = default_timer()

    diskmap = parse_file(filepath)
    spaces = list(get_spaces(diskmap))
    files = list(get_files(diskmap))
    products = get_products_moving_whole_files(files, spaces)
    
    result = reduce(lambda x, y: x + y, products)
    duration = default_timer() - start
    print(f"Result of part 2: {result} ({duration}s)")
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 1928)  # ~0.00032s
    assert(solve_part_1('puzzle.txt') == 6258319840548)  # ~0.014s

    assert(solve_part_2('test.txt') == 2858)  # ~0.00024s
    assert(solve_part_2('puzzle.txt') == 6286182965311)  #  ~1.01s