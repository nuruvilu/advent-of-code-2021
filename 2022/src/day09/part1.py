import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    t = (0, 0)
    h = t
    visited = {h}
    for line in inp:
        drx, mag = line.split()
        for _ in range(int(mag)):
            t = aoc.udlr_xy(drx, t)
            if aoc.dist(t, h) >= 2:
                mingap = 9
                minmove = None
                for adj in aoc.adjsdiags2(h):
                    gap = aoc.dist(t, adj)
                    if gap < mingap:
                        mingap = gap
                        minmove = adj
                h = minmove
                visited.add(h)
            print(t, h)
    return len(visited)


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
