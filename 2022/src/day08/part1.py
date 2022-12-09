import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def vis(grid, visible):
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            print(n if (i, j) in visible else '.', end='')
        print()


def solve(inp):
    grid = [[int(n) for n in row] for row in inp]
    pivot_grid = [[row[i] for row in grid] for i, _ in enumerate(grid[0])]

    visible = set()
    for i, row in enumerate(grid):
        last = -1
        for j, n in enumerate(row):
            if n > last:
                last = n
                visible.add((i, j))
    for i, row in enumerate(grid):
        last = -1
        for j, n in enumerate(row[::-1]):
            if n > last:
                last = n
                visible.add((i, len(row) - j - 1))
    for i, row in enumerate(pivot_grid):
        last = -1
        for j, n in enumerate(row):
            if n > last:
                last = n
                visible.add((j, i))
    for i, row in enumerate(pivot_grid):
        last = -1
        for j, n in enumerate(row[::-1]):
            if n > last:
                last = n
                visible.add((len(row) - j - 1, i))
    #vis(grid, visible)
    return len(visible)


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
