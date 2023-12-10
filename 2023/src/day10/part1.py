import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


pipes = {
    '|': 'UD',
    '-': 'LR',
    'L': 'DR',
    'J': 'DL',
    '7': 'UL',
    'F': 'UR',
    '.': '',
    'S': 'UDLR'
}


def connected(p1, grid):
    i1, j1 = p1
    ret = []
    for direct in pipes[inp[i1][j1]]:
        i2, j2 = aoc.udlr_ij(direct, (i1, j1))
        if aoc.inbounds2(i2, j2, len(inp), len(inp[0])):
            for d2 in pipes[inp[i2][j2]]:
                i3, j3 = aoc.udlr_ij(d2, (i2, j2))
                if aoc.inbounds2(i3, j3, len(inp), len(inp[0])) and (i3, j3) == (i1, j1):
                    ret.append((i2, j2))
    return ret

def solve(inp):
    points = []
    for i, row in enumerate(inp):
        for j, item in enumerate(row):
            if item == 'S':
                points.append((i, j))
    visited = set()
    dist = 0
    while points:
        print(points, dist)
        new_points = []
        for p in points:
            for pp in connected(p, inp):
                if pp not in visited:
                    new_points.append(pp)
            visited.add(p)
        points = new_points
        dist += 1
    return dist - 1


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=10, year=2023))
    print(solve(inp))
