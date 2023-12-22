import math
import operator

import sys
sys.path.append('..')

from collections import defaultdict, deque
from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


MAX_STEPS = 26501365


def solve(inp):
    width = len(inp)
    start = None
    for i, row in enumerate(inp):
        for j, x in enumerate(row):
            if x == 'S':
                start = (i, j)
    coeffs = [0]
    it = 0
    queue = {start}
    while len(coeffs) < 4:
        it += 1
        new_queue = set()
        for loc in queue:
            for i, j in aoc.adjs(loc):
                if inp[i % width][j % width] != '#':
                    new_queue.add((i, j))
        if it % width == MAX_STEPS % width:
            coeffs.append(len(new_queue))
        queue = new_queue
    tiles = MAX_STEPS // width
    return coeffs[1] + (coeffs[2] - coeffs[1]) * tiles + (tiles * (tiles - 1) // 2) * (coeffs[3] - 2*coeffs[2] + coeffs[1])


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=21, year=2023))
    print(solve(inp))
