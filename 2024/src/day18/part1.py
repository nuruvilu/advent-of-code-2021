import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


#SIZE_XY, TOTAL_FALLEN = 7, 12
SIZE_XY, TOTAL_FALLEN = 71, 1024
DEST = (SIZE_XY - 1, SIZE_XY - 1)


def solve(inp):
    corrupted = set()
    for b in inp[:TOTAL_FALLEN]:
        bx, by = tuple(int(n) for n in b.split(','))
        corrupted.add((bx, by))
    #print(corrupted)
    q = [((0, 0), 0)]
    visited = set()
    while q:
        (x, y), dist = q.pop(0)
        if (x, y) == DEST:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for xp, yp in aoc.adjs((x, y)):
            if aoc.inbounds2(xp, yp, SIZE_XY, SIZE_XY) and (xp, yp) not in corrupted:
                q.append(((xp, yp), dist + 1))


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=18, year=2024))
    print(solve(inp))
