import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce, cmp_to_key
from pathlib import Path
from collections import defaultdict

import common as aoc
from aocd import get_data


def five_of(hand):
    if len(set(hand)) == 1:
        return True


def four_of(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    return tuple(sorted(weights.values())) == (1, 4)


def full_house(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    return tuple(sorted(weights.values())) == (2, 3)


def three_of(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    return tuple(sorted(weights.values())) == (1, 1, 3)


def two_pair(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    return tuple(sorted(weights.values())) == (1, 2, 2)


def one_pair(hand):
    if len(set(hand)) == 4:
        return True


card_order = 'TJQKA'


def compare(shb1, shb2):
    score1, hand1, _ = shb1
    score2, hand2, _ = shb2
    if score1 > score2:
        return 1
    elif score1 < score2:
        return -1
    for c1, c2 in zip(hand1, hand2):
        if c1.isdigit() and c2.isdigit():
            if int(c1) > int(c2):
                return -1
            elif int(c1) < int(c2):
                return 1
        elif c1.isdigit():
            return 1
        elif c2.isdigit():
            return -1
        elif card_order.index(c1) < card_order.index(c2):
            print(c1, c2, 'LESS')
            return 1
        elif card_order.index(c1) > card_order.index(c2):
            print(c1, c2, 'MORE')
            return -1


def solve(inp):
    processed = []
    for handbid in inp:
        hand, bid = handbid.split()
        bid = int(bid)
        score = 6
        if five_of(hand):
            score = 0
        elif four_of(hand):
            score = 1
        elif full_house(hand):
            score = 2
        elif three_of(hand):
            score = 3
        elif two_pair(hand):
            score = 4
        elif one_pair(hand):
            score = 5
        processed.append((score, hand, bid))
    processed = sorted(processed, key=cmp_to_key(compare), reverse=True)
    total = 0
    print(processed)
    for i, (s, h, bid) in enumerate(processed, start=1):
        print(i, s, h, bid)
        total += i * bid
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=7, year=2023))
    print(solve(inp))
