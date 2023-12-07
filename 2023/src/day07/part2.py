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
    h = set(hand)
    return len(h) == 1 or (len(h) == 2 and 'J' in h)


def four_of(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    x = tuple(sorted(weights.values()))
    return x == (1, 4) or (weights['J'] > 0 and len(weights) == 3 and not (weights['J'] == 1 and x == (1, 2, 2)))


def full_house(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    x = tuple(sorted(weights.values()))
    return x == (2, 3) or (weights['J'] > 0 and len(weights) == 3)


def three_of(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    x = tuple(sorted(weights.values()))
    return x == (1, 1, 3) or (weights['J'] > 0 and x == (1, 1, 1, 2))


def two_pair(hand):
    weights = defaultdict(int)
    for ch in hand:
        weights[ch] += 1
    x = tuple(sorted(weights.values()))
    if weights['J'] == 2:
        raise 'hmm'
    print(hand, weights)
    return x == (1, 2, 2) or (weights['J'] > 0 and x == (1, 1, 1, 2))


def one_pair(hand):
    if len(set(hand)) == 4 or 'J' in hand:
        return True


card_order = 'TQKA'


def compare(shb1, shb2):
    score1, hand1, _ = shb1
    score2, hand2, _ = shb2
    if score1 > score2:
        return 1
    elif score1 < score2:
        return -1
    for c1, c2 in zip(hand1, hand2):
        if c1 == 'J' and c2 != 'J':
            return 1
        elif c1 != 'J' and c2 == 'J':
            return -1
        elif c1 == 'J' and c2 == 'J':
            continue
        elif c1.isdigit() and c2.isdigit():
            if int(c1) > int(c2):
                return -1
            elif int(c1) < int(c2):
                return 1
        elif c1.isdigit():
            return 1
        elif c2.isdigit():
            return -1
        elif card_order.index(c1) < card_order.index(c2):
            return 1
        elif card_order.index(c1) > card_order.index(c2):
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
