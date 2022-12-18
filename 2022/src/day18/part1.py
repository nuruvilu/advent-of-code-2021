import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    drops = set()
    for line in inp:
        drops.add(tuple(int(x) for x in line.split(',')))
    surface = 0
    for drop in drops:
        for adj in aoc.adjs(drop):
            if adj not in drops:
                surface += 1
    return surface


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
