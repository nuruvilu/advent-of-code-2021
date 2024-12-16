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
    good_seats = set()
    curr_lowest = []
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == 'S':
                s = (i, j)
            elif c == 'E':
                e = (i, j)
    def h(p):
        return aoc.mandist(p[0], e)
    def is_target(p_item):
        p, _ = p_item.item
        if p == e:
            #print(p_item)
            if not curr_lowest:
                curr_lowest.append(p_item.total_weight)
            if p_item.total_weight == curr_lowest[0]:
                for pp, _ in p_item.path:
                    good_seats.add(pp)
                good_seats.add(p)
                return False
            return True
        return False
    def step(p_item):
        p, dr = p_item.item
        nexts = []
        ip, jp = aoc.udlr_ij(DIRS[dr], p)
        if inp[ip][jp] != '#':
            nexts.append((1, ((ip, jp), dr)))
        nexts.append((1000, (p, (dr - 1) % 4)))
        nexts.append((1000, (p, (dr + 1) % 4)))
        return nexts
    try:
        aoc.astar((s, 0), step, h, is_target)
    except RuntimeError as e:
        print(e)
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if (i, j) in good_seats:
                print('O', end='')
            else:
                print(c, end='')
        print()
    return len(good_seats)


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=16, year=2024))
    print(solve(inp))
