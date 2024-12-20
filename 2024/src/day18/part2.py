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


def find_path(start, stop, accept):
    q = [(start, [start])]
    visited = set()
    while q:
        (x, y), path = q.pop(0)
        if (x, y) == stop:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for xp, yp in aoc.adjs((x, y)):
            if aoc.inbounds2(xp, yp, SIZE_XY, SIZE_XY) and accept((xp, yp)):
                q.append(((xp, yp), path + [(xp, yp)]))
    else:
        return None


def corrupted_acceptor(corrupted):
    return lambda p: p not in corrupted


def solve(inp):
    corrupted = set()
    for b in inp[:TOTAL_FALLEN]:
        bx, by = tuple(int(n) for n in b.split(','))
        corrupted.add((bx, by))
    path = find_path((0, 0), DEST, corrupted_acceptor(corrupted))
    path_flipped = {p: i for i, p in enumerate(path)}
    for b in inp[TOTAL_FALLEN:]:
        bx, by = tuple(int(n) for n in b.split(','))
        corrupted.add((bx, by))
        if (bx, by) in ((0, 0), DEST):
            return f'{bx},{by}'
        if (bx, by) in path:
            i = path.index((bx, by))
            new_path = find_path(path[i - 1], path[i + 1], corrupted_acceptor(corrupted))
            if not new_path:
                return f'{bx},{by}'
            okay = set(new_path) | set(path[:i]) | set(path[i+1:])
            path = find_path((0, 0), DEST, lambda p: p in okay)
            if not path:
                return f'{bx},{by}'


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=18, year=2024))
    print(solve(inp))
