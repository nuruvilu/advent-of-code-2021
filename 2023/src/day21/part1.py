import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


MAX_STEPS = 64


def solve(inp):
    total = [0]
    def step(p_item):
        loc, steps = p_item.item
        nexts = []
        for i, j in aoc.adjs(loc):
            if aoc.inbounds2(i, j, len(inp), len(inp[0])) and inp[i][j] != '#':
                nexts.append(((i, j), steps + 1))
        return nexts
    def is_target(p_item):
        steps = p_item.item[1]
        if steps == MAX_STEPS:
            total[0] += 1
        return steps > MAX_STEPS
    start = None
    for i, row in enumerate(inp):
        for j, x in enumerate(row):
            if x == 'S':
                start = (i, j)
    aoc.bfs((start, 0), step, is_target)
    return total[0]


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=21, year=2023))
    print(solve(inp))
