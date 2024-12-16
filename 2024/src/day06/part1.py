import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


ROTATION = 'URDL'


def solve(inp):
    curr_i, curr_j = None, None
    blockers = set()
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == '^':
                curr_i, curr_j = i, j
            elif c == '#':
                blockers.add((i, j))
    visited = set()
    dir_i = 0
    while aoc.inbounds2(curr_i, curr_j, len(inp), len(inp[0])):
        n_i, n_j = aoc.udlr_ij(ROTATION[dir_i], (curr_i, curr_j))
        if (n_i, n_j) in blockers:
            dir_i = (dir_i + 1) % len(ROTATION)
        else:
            visited.add((curr_i, curr_j))
            curr_i, curr_j = n_i, n_j
    return len(visited)


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=6, year=2024))
    print(solve(inp))
