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


big_pipes = {
    '|': [
        ['.', '#', '.'],
        ['.', '#', '.'],
        ['.', '#', '.'],
    ],
    '-': [
        ['.', '.', '.'],
        ['#', '#', '#'],
        ['.', '.', '.'],
    ],
    'L': [
        ['.', '#', '.'],
        ['.', '#', '#'],
        ['.', '.', '.'],
    ],
    'J': [
        ['.', '#', '.'],
        ['#', '#', '.'],
        ['.', '.', '.'],
    ],
    '7': [
        ['.', '.', '.'],
        ['#', '#', '.'],
        ['.', '#', '.'],
    ],
    'F': [
        ['.', '.', '.'],
        ['.', '#', '#'],
        ['.', '#', '.'],
    ],
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
    loop = set()
    biggrid = []
    for _ in range(len(inp) * 3):
        biggrid.append(['.'] * (len(inp[0]) * 3))
    while points:
        new_points = []
        for p in points:
            curr = inp[p[0]][p[1]]
            for pp in connected(p, inp):
                if pp not in loop:
                    new_points.append(pp)
            if curr == 'S':
                ds = set()
                for d in 'UDLR':
                    if aoc.udlr_ij(d, p) in new_points:
                        ds.add(d)
                for shape, directions in pipes.items():
                    if set(directions) == ds:
                        curr = shape
            loop.add(p)
            for i in range(3):
                for j in range(3):
                    biggrid[p[0]*3 + i][p[1]*3 + j] = big_pipes[curr][i][j]
        points = new_points
    total = 0
    for line in biggrid:
        print(''.join(line))
    for i in range(len(inp)):
        print(i / len(inp))
        for j in range(len(inp[0])):
            if (i, j) not in loop:
                def is_target(p):
                    for pp in aoc.adjsdiags2(p):
                        if not aoc.inbounds2(pp[0], pp[1], len(biggrid), len(biggrid[0])):
                            return True
                    return False
                def step(pi):
                    x = []
                    p = pi.item
                    for pp in aoc.adjs(p):
                        if biggrid[pp[0]][pp[1]] == '.':
                            x.append(pp)
                    return x
                try:
                    aoc.bfs((i * 3, j * 3), step, is_target)
                except RuntimeError:
                    total += 1
    return total


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=10, year=2023))
    print(solve(inp))
