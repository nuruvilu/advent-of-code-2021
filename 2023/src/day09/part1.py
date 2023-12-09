import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    total = 0
    for history in inp:
        hist = [int(n) for n in history.split()]
        tiers = [hist]
        differing = True
        tier = 0
        while differing:
            curr = tiers[tier][0]
            tiers.append([])
            differing = False
            for n in tiers[tier][1:]:
                if n != curr:
                    differing = True
                tiers[-1].append(n - curr)
                curr = n
            tier += 1
        print(tiers)
        total += sum((t[-1] for t in tiers))
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=9, year=2023))
    print(solve(inp))
