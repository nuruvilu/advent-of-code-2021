import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path
from copy import deepcopy

import common as aoc
from aocd import get_data


def solve(inp):
    cycle_i = 0  # 0 = N, 1 = W, 2 = S, 3 = E
    memo = {}
    target = 4 * 1000000000
    grid = aoc.rotate_counterclock(inp)
    while cycle_i < target:
        new_grid = deepcopy(grid)
        for i, row in enumerate(grid):
            last_barrier = -1
            for j, item in enumerate(row):
                if item == 'O':
                    last_barrier += 1
                    new_grid[i][last_barrier] = 'O'
                    if last_barrier != j:
                        new_grid[i][j] = '.'
                elif item == '#':
                    last_barrier = j
        grid = aoc.rotate_clock(new_grid)
        cycle_i += 1
        joined = '\n'.join(''.join(x) for x in grid)
        if joined in memo:
            diff = cycle_i - memo[joined]
            cycles_left = target - cycle_i
            cycle_i += diff * (cycles_left // diff)
        else:
            memo[joined] = cycle_i
    total = 0
    for row in grid:
        for j, item in enumerate(row):
            if item == 'O':
                total += len(row) - j
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=14, year=2023))
    print(solve(inp))
