''' Day 7: Camel Cards 
    https://adventofcode.com/2023/day/7
'''

import re

from argparse import ArgumentParser
from collections import Counter
from functools import cmp_to_key, reduce

LINE = re.compile('(\w+) (\d+)')


TYPE_MAP = {
   '5': 7,  # 5 of a kind
   '41': 6,  # 4 of a kind
   '32': 5,  # Full house
   '311': 4,  # 3 of a kind
   '221': 3,  # 2 pairs
   '2111': 2,  # 1 pair
   '11111': 1  # High card
}


class Hand(object):
    
    CARD_MAP = {x: n for n, x in enumerate('23456789TJQKA')}
    hands = []

    def __init__(self, hand, bid):
        self.str_hand = hand
        self.hand = Counter(hand)
        self.bid = int(bid)
        self.get_type()
        self.get_int_hand(hand)
        self.rank = None
        Hand.add(self)

    def get_type(self):
        values = list(self.hand.values())
        values.sort(reverse=True)
        values = ''.join(map(str, values))

        self.hand_type = TYPE_MAP[values]

    def get_int_hand(self, hand):
        self.int_hand = [self.CARD_MAP[x] for x in hand]

    def __lt__(self, other):
        return other > self

    def __gt__(self, other):
        if (self.hand_type == other.hand_type):
            for i in range(len(self.int_hand)):
                if (self.int_hand[i] != other.int_hand[i]):
                    return self.int_hand[i] > other.int_hand[i]
            raise(Exception('Same  hand twice!'))

        else:
            return self.hand_type > other.hand_type

    def __repr__(self):
        return self.str_hand

    @property
    def winnings(self):
        return self.bid * self.rank

    @classmethod
    def add(cls, hand):
        cls.hands.append(hand)

    @classmethod
    def sort(cls):
        cls.hands.sort(key=cmp_to_key(cls.cmp_to_key))
        for rank, hand in enumerate(cls.hands, start=1):
            hand.rank = rank

    @staticmethod
    def cmp_to_key(a, b):
        return 1 if (a > b) else -1


class HandWithJokers(Hand):
    CARD_MAP = {x: n for n, x in enumerate('J23456789TQKA')}
    
    def __init__(self, hand, bid):
        self.str_hand = hand
        self.hand = Counter(hand)
        self.bid = int(bid)
        self.get_type()
        self.get_int_hand(hand)
        self.rank = None
        HandWithJokers.add(self)

    def get_type(self):

        old = dict(self.hand)
        if (('J' in self.hand) and (self.hand['J'] < 5)):
            J = self.hand.pop('J')
            highest = sorted(self.hand.items(), key=lambda x: HandWithJokers.CARD_MAP[x[0]], reverse=True)
            highest.sort(key=lambda x: x[1], reverse=True)
            highest = highest[0][0]
            self.hand[highest] += J

        values = list(self.hand.values())
        values.sort(reverse=True)
        values = ''.join(map(str, values))

        self.hand_type = TYPE_MAP[values]


def camel_cards(filepath):
    with open(filepath, 'r') as f:
        while (line := f.readline().strip('\n\s\t')):
            matches = LINE.search(line)
            Hand(hand=matches.group(1), bid=matches.group(2))
    Hand.sort()
    return reduce(lambda x, y: x + y, map(lambda x: x.winnings, Hand.hands))


def camel_cards_01(filepath):
    with open(filepath, 'r') as f:
        while (line := f.readline().strip('\n\s\t')):
            matches = LINE.search(line)
            HandWithJokers(hand=matches.group(1), bid=matches.group(2))
    HandWithJokers.sort()
    return reduce(lambda x, y: x + y, map(lambda x: x.winnings, HandWithJokers.hands))


if __name__ == '__main__':
    VERSIONS = {0: camel_cards, 1: camel_cards_01}
    parser = ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-v', '--version', default=0, type=int)
    args = parser.parse_args()
    
    print(VERSIONS[args.version](args.filepath))
