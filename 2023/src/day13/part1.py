import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def test(grid):
    for j in range(1, len(grid[0])):
        #print(grid, j)
        for row in grid:
            left, right = row[:j], row[j:]
            #if j == 5:
                #print(left, right)
            if len(left) > len(right) and not left[::-1].startswith(right):
                break
            elif len(left) <= len(right) and not right[::-1].endswith(left):
                break
        else:
            return j
            break
    return 0


def solve(inp):
    total = 0
    for grid in inp:
        res = test([''.join(x) for x in grid])
        if res != 0:
            total += res
            continue
        new_grid = [['.'] * len(grid) for _ in range(len(grid[0]))]
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                new_grid[j][i] = item
        total += 100*test([''.join(x) for x in new_grid])
    return total


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=13, year=2023))
    print(solve(inp))
