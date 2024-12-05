''' Advent of Code 2024
    Day 5: Print Queue
    https://adventofcode.com/2024/day/5

Status:
    - Part 1:
        * Test: PASS
        * Puzzle: PASS
    - Part 2:
        * Test: PASS
        * Puzzle: PASS
'''

from functools import cmp_to_key

def parse_file(filepath:str) -> list[str]:
    rules = []
    updates = []
    with open(filepath, 'r') as file:
        lines = map(lambda x: x.strip('\n\s\t'), file.readlines())
    for line in lines:
        if '|' in line:
            x, y = tuple(map(int, line.split('|')))
            rules.append((x, y))
        elif ',' in line:
            pages = list(map(int, line.split(',')))
            updates.append(pages)
    return rules, updates

def is_update_in_right_order(update, rules):
    for rule in rules:
        x, y = rule
        if (x not in update) or (y not in update):
            continue
        if update.index(x) > update.index(y):
            return False   
    return True

def get_middle_page(update):
    return update[int((len(update)+1)/2) - 1]


def solve_part_1(filepath:str):
    print("Solving part 1 with:", filepath)
    rules, updates = parse_file(filepath)

    right_updates = filter(lambda x: is_update_in_right_order(x, rules), updates)
    middle_pages = map(get_middle_page, right_updates)
    result = sum(middle_pages)

    print("Result of part 1:", result)
    return result

def correct_update(update, rules):
    return sorted(update, key=cmp_to_key(lambda x, y: compare_pages([x, y], rules)))

def compare_pages(pages, rules):
    x, y = pages
    if is_update_in_right_order([x, y], rules):
        return 1
    return -1


def solve_part_2(filepath:str):
    print("Solving part 2 with:", filepath)
    rules, updates = parse_file(filepath)

    incorrect_updates = filter(lambda x: not is_update_in_right_order(x, rules), updates)
    corrected_updates = map(lambda x: correct_update(x, rules), incorrect_updates)
    middle_pages = map(get_middle_page, corrected_updates)
    result = sum(middle_pages)

    print("Result of part 2:", result)
    return result


if __name__ == '__main__':
    
    assert(solve_part_1('test.txt') == 143)
    assert(solve_part_1('puzzle.txt') == 4135)

    assert(solve_part_2('test.txt') == 123)
    print(solve_part_2('puzzle.txt') == 5285)