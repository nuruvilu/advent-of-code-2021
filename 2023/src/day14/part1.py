import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    better = aoc.rotate_counterclock(inp)
    total = 0
    for row in better:
        last_barrier = -1
        for j, item in enumerate(row):
            if item == 'O':
                last_barrier += 1
                total += len(row) - last_barrier
            elif item == '#':
                last_barrier = j

    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=14, year=2023))
    print(solve(inp))
