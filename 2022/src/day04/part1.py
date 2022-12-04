import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    c = 0
    for line in inp:
        left, right = line.split(',')
        lefts = left.split('-')
        rights = right.strip().split('-')
        lmin, lmax = [int(x) for x in lefts]
        rmin, rmax = [int(x) for x in rights]
        if lmin <= rmin and lmax >= rmax:
            c += 1
        elif rmin <= lmin and rmax >= lmax:
            c += 1
    return c


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
