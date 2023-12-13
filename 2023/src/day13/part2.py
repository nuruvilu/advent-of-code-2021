import math
import operator

import sys
sys.path.append('..')

from collections import defaultdict
from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def get_badlines(grid):
    badlines = defaultdict(int)
    for j in range(1, len(grid[0])):
        counted = False
        for i, row in enumerate(grid):
            left, right = row[:j], row[j:]
            smudges = 0
            for k, (l, r) in enumerate(zip(left[::-1], right)):
                if l != r:
                    smudges += 1
                    if smudges > 1:
                        break
            if smudges < 1:
                continue
            elif smudges < 2 and not counted:
                counted = True
            else:
                break
        else:
            if counted:
                badlines[j] += 1
    return badlines


def solve(inp):
    total = 0
    for grid in inp:
        badlines = get_badlines([''.join(x) for x in grid])
        res = [j for j, lines in badlines.items() if lines == 1]
        if res:
            total += res[0]
        else:
            new_grid = [['.'] * len(grid) for _ in range(len(grid[0]))]
            for i, row in enumerate(grid):
                for j, item in enumerate(row):
                    new_grid[j][i] = item
            badlines = get_badlines([''.join(x) for x in new_grid])
            total += 100*[j for j, lines in badlines.items() if lines == 1][0]
    return total


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=13, year=2023))
    print(solve(inp))
