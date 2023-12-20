import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


dirs = {
    'L': 'UD',
    'R': 'UD',
    'U': 'LR',
    'D': 'LR'
}


def solve(inp):
    def step(p_item):
        nexts = []
        coords, drct, reps = p_item.item
        for ch in dirs[drct] + drct:
            if ch == drct and reps >= 2:
                continue
            nxt = aoc.udlr_ij(ch, coords)
            if aoc.inbounds2(nxt[0], nxt[1], len(inp), len(inp[0])):
                nexts.append((inp[nxt[0]][nxt[1]], (nxt, ch, (reps + 1) if ch == drct else 0)))
        return nexts
    def is_target(p_item):
        loc, _, _ = p_item.item
        return loc == (len(inp) - 1, len(inp[0]) - 1)
    result = aoc.dijkstra(((0, 0), 'R', 0), step, is_target)
    return result.total_weight


if __name__ == '__main__':
    #inp = aoc.readgridnums(Path('sample.txt'))
    inp = aoc.readgridnums(get_data(day=17, year=2023))
    print(solve(inp))
