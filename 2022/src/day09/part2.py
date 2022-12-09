import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def next_loc(moved, unmoved):
    if aoc.dist(moved, unmoved) >= 2:
        mingap = 9
        minmove = None
        for adj in aoc.adjsdiags2(unmoved):
            gap = aoc.dist(moved, adj)
            if gap < mingap:
                mingap = gap
                minmove = adj
        return minmove
    else:
        return unmoved


def solve(inp):
    t = (0, 0)
    visited = {t}
    followers = [t] * 9
    for line in inp:
        drx, mag = line.split()
        for _ in range(int(mag)):
            t = aoc.udlr_xy(drx, t)
            followers[0] = next_loc(t, followers[0])
            for i, node in enumerate(followers[1:], 1):
                followers[i] = next_loc(followers[i - 1], node)
            # print(t, h)
            visited.add(followers[-1])
    return len(visited)


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
