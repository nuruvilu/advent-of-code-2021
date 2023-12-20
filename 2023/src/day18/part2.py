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
    pos = (0, 0)
    vertices = [pos]
    perimeter = 0
    for line in inp:
        _direction, _num, color = line.split()
        num, direction = int(color[2:-2], base=16), int(color[-2])
        direction = 'RDLU'[direction]
        num = int(num)
        perimeter += num
        pos = aoc.udlr_xy(direction, pos, dist=num)
        vertices.append(pos)
    total = 0
    for (x1, y1), (x2, y2) in aoc.window(vertices, 2):
        total += x1*y2 - y1*x2
    return perimeter / 2 + abs(total / 2) + 1


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=18, year=2023))
    print(solve(inp))
