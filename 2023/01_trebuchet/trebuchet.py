'''
https://adventofcode.com/2023/day/1
'''

import re

from argparse import ArgumentParser
from functools import reduce

''' The idea to solve the 1st problem is to iterate line by line discarding
all characters that are not numbers and then taking the 1st and last 
to concatenate them and convert the string into an integer

ASSUMPTION: No zeroes!
The statement of the problem doesn't consider the number zero within 
the list of possible digits provided, hence if there was any zero we would
potentially have to skip it... or not...
Snce it's not clear I assume there are no zeroes.
'''

# Let's compile a regular expression to identify non-digit chars.
NAN = re.compile('[^\d]+')

def trebuchet(filepath):
    result = 0
    with open(filepath, 'r') as f:
        while line := f.readline():
            # Walrus operator (:=) comes in handy to iterate over the lines of the file
            # without loading them all in memory

            # remove all non digits using the compiled regular expression
            numbers = NAN.sub('', line)  

            result += int(numbers[0] + numbers[-1])

    return result


''' For the 2nd problem the strategy could be the same as in the previous one.
Instead, I choose a functional approach with a map reduce strategy.
The idea is to create an iterator that for every line it gives the relevant number.
Then reduce that iterator summing the elements by pairs. That way only one line is read
at a time and only 2 values of the iterator are loaded in memory at a time.
'''

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
MATCH_DICT = {x: str(y) for x, y in zip(NUMBERS, range(1, 10))}
MATCH_DICT.update({str(x): str(x) for x in range(1, 10)})
MATCH_FWD = re.compile('(\d|{})'.format('|'.join(NUMBERS)))
MATCH_BCK = re.compile('(\d|{})'.format('|'.join([x[::-1] for x in NUMBERS])))


def trebuchet_01(filepath):
    with open(filepath, 'r') as f:
        return reduce(lambda x, y: x + y, get_numbers(f))

def get_numbers(f):
    while line := f.readline():
        first = MATCH_DICT[MATCH_FWD.search(line).group(0)]
        last = MATCH_DICT[MATCH_BCK.search(line[::-1]).group(0)[::-1]]
        yield int(first + last)


if __name__ == '__main__':
    VERSIONS = {0: trebuchet, 1: trebuchet_01}
    parser = ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-v', '--version', default=0, type=int)
    args = parser.parse_args()
    
    print(VERSIONS[args.version](args.filepath))
