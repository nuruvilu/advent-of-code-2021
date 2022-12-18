import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict

import common as aoc


def solve(inp):
    drops = set()
    for line in inp:
        drops.add(tuple(int(x) for x in line.split(',')))
    surface = 0
    pos = (0, 0, 0)
    pos = aoc.bfs(pos, lambda p: aoc.adjs(p.item), lambda p: p in drops).path[-1]
    print(pos)
    queue = [(pos, 0)]
    counted = set()
    while queue:
        curr, counter = queue.pop(0)
        if curr in counted or counter > 3:
            continue
        counted.add(curr)
        for adj in aoc.adjs(curr):
            if adj in drops:
                surface += 1
                counter = 0
        for adj in aoc.adjs(curr):
            if adj not in drops and counter < 3:
                queue.append((adj, counter + 1))
    return surface


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
