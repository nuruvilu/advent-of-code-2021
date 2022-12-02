import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


pshape = {'A': 1, 'B': 2, 'C': 3}
beats = {'A': 'C', 'B': 'A', 'C': 'B'}
loses = {'A': 'B', 'B': 'C', 'C': 'A'}


def rps(p, o):
    if o == 'X':
        return pshape[beats[p]]
    elif o == 'Y':
        return pshape[p] + 3
    else:
        return pshape[loses[p]] + 6


def solve(inp):
    s = 0
    for line in inp:
        p, o = line.split(' ')
        s += rps(p, o)
    return s


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
