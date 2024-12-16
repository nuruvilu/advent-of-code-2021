import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path
from collections import defaultdict
from math import gcd

import common as aoc
from aocd import get_data


def solve(inp):
    node_sets = defaultdict(list)
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c.isalnum():
                node_sets[c].append((i, j))
    antinodes = set()
    for node_set in node_sets.values():
        for i, (x1, y1) in enumerate(node_set[:-1]):
            for x2, y2 in node_set[i+1:]:
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                dx, dy = dx / g, dy / g
                xs, ys = x1, y1
                while aoc.inbounds2(xs, ys, len(inp), len(inp[0])):
                    antinodes.add((xs, ys))
                    xs, ys = xs - dx, ys - dy
                xs, ys = x2, y2
                while aoc.inbounds2(xs, ys, len(inp), len(inp[0])):
                    antinodes.add((xs, ys))
                    xs, ys = xs + dx, ys + dy
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c.isalnum() and (i, j) in antinodes:
                print('@', end='')
            elif (i, j) in antinodes:
                print('#', end='')
            else:
                print(c, end='')
        print()
    return len(antinodes)


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=8, year=2024))
    print(solve(inp))
