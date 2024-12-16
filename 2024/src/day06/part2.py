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
    start_i, start_j = None, None
    blockers = set()
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == '^':
                start_i, start_j = i, j
            elif c == '#':
                blockers.add((i, j))
    s = 0
    print(blockers)
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if (i, j) in blockers:
                continue
            print(i * len(inp) + j, '/', len(inp) * len(inp[0]))
            visited = set()
            dir_i = 0
            curr_i, curr_j = start_i, start_j
            while aoc.inbounds2(curr_i, curr_j, len(inp), len(inp[0])):
                if (curr_i, curr_j, dir_i) in visited:
                    s += 1
                    break
                n_i, n_j = aoc.udlr_ij(ROTATION[dir_i], (curr_i, curr_j))
                if (n_i, n_j) in blockers or (n_i, n_j) == (i, j):
                    dir_i = (dir_i + 1) % len(ROTATION)
                else:
                    visited.add((curr_i, curr_j, dir_i))
                    curr_i, curr_j = n_i, n_j
    return s


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=6, year=2024))
    print(solve(inp))
