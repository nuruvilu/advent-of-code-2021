import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


TARGET = 'XMAS'


def look(inp, i, j, depth, direction):
    if depth == len(TARGET):
        return 1
    if aoc.inbounds2(i, j, len(inp), len(inp[0])) and inp[i][j] == TARGET[depth]:
        s = 0
        for dx, (ip, jp) in enumerate(aoc.adjsdiags2((i, j))):
            if direction is None or direction == dx:
                s += look(inp, ip, jp, depth + 1, dx)
        return s
    else:
        return 0


def solve(inp):
    count = 0
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            count += look(inp, i, j, 0, None)
    return count


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=4, year=2024))
    print(solve(inp))
