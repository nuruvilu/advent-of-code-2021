import math
import operator

import sys
sys.path.append('..')

from collections import Counter, defaultdict
from heapq import heappush, heappop
from functools import reduce

import common as aoc


pshape = {
    'A': 1,
    'B': 2,
    'C': 3
}


oshape = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


beats = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}


def rps(p, o):
    if pshape[p] == oshape[o]:
        return oshape[o] + 3
    elif beats[o] == p:
        return oshape[o] + 6
    else:
        return oshape[o]


def solve(inp):
    s = 0
    for line in inp:
        p, o = line.split(' ')
        s += rps(p, o)
    return s


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
