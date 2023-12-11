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
    empty_rows = set()
    empty_cols = set()
    for i, row in enumerate(inp):
        if len(set(row)) == 1 and '.' in row:
            empty_rows.add(i)
    for j in range(len(inp[0])):
        for row in inp:
            if row[j] == '#':
                break
        else:
            empty_cols.add(j)
    dists = []
    counted = set()
    for i, row in enumerate(inp):
        for j, gal in enumerate(row):
            if gal == '.':
                continue
            visited = set()
            def is_target(prio_it):
                (i2, j2), dst = prio_it.item, prio_it.total_weight
                if inp[i2][j2] == '#' and (i2, j2) not in visited:
                    pathkey = tuple(sorted([(i, j), (i2, j2)]))
                    if pathkey not in counted:
                        #print(i, j, i2, j2, dst)
                        dists.append(dst)
                        visited.add((i2, j2))
                        counted.add(pathkey)
                return False
            def step(prio_it):
                nxts = []
                (i1, j1) = prio_it.item
                for (i2, j2) in aoc.adjs((i1, j1)):
                    if aoc.inbounds2(i2, j2, len(inp), len(inp[0])):
                        dst = 1
                        if i1 == i2 and j1 in empty_cols:
                            dst = 1_000_000
                        elif j1 == j2 and i1 in empty_rows:
                            dst = 1_000_000
                        nxts.append((dst, (i2, j2)))
                return nxts
            try:
                aoc.dijkstra((i, j), step, is_target)
            except RuntimeError:
                print('one down')
    return sum(dists)


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=11, year=2023))
    print(solve(inp))
