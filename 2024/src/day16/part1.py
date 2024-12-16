import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


DIRS = 'RDLU'


def solve(inp):
    s, e = None, None
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == 'S':
                s = (i, j)
            elif c == 'E':
                e = (i, j)
    def h(p):
        return aoc.mandist(p[0], e)
    def is_target(p_item):
        return p_item.item[0] == e
    def step(p_item):
        p, dr = p_item.item
        nexts = []
        ip, jp = aoc.udlr_ij(DIRS[dr], p)
        if inp[ip][jp] != '#':
            nexts.append((1, ((ip, jp), dr)))
        nexts.append((1000, (p, (dr - 1) % 4)))
        nexts.append((1000, (p, (dr + 1) % 4)))
        return nexts
    return aoc.astar((s, 0), step, h, is_target).total_weight


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=16, year=2024))
    print(solve(inp))
