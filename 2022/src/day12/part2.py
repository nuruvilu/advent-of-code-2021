import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


grid = None


def is_target(x):
    return grid[x[0]][x[1]] == 'E'


def get_next(x):
    c, d = x.item
    nexts = []
    curr_height = ord('a') if grid[c][d] == 'S' else ord(grid[c][d])
    for a, b in aoc.adjs(x.item):
        if aoc.inbounds2(a, b, len(grid), len(grid[0])):
            height = ord('z') if grid[a][b] == 'E' else ord(grid[a][b])
            if height - curr_height <= 1:
                nexts.append((a, b))
    return nexts


def solve(inp):
    global grid
    grid = inp
    mini = 999999
    for i, row in enumerate(inp):
        for j, e in enumerate(row):
            if e in ('S', 'a'):
                try:
                    result = aoc.bfs((i, j), get_next, is_target)
                except:
                    continue
                curr_len = len(result.path)
                mini = min(mini, curr_len)
    return mini


if __name__ == '__main__':
    inp = aoc.readgrid('input.txt')
    print(solve(inp))
