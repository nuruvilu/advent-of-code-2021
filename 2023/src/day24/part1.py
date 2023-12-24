import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


LOWER = 7
UPPER = 27


def solve(inp):
    hails = []
    for line in inp:
        pos, vel = line.split(' @ ')
        x, y = tuple(int(n) for n in pos.split(', ')[:-1])
        dx, dy = tuple(int(n) for n in vel.split(', ')[:-1])
        hails.append(((x, y), (dx, dy)))
    count = 0
    for i, ((x1, y1), (dx1, dy1)) in enumerate(hails):
        for (x2, y2), (dx2, dy2) in hails[i+1:]:
            p1, q1, r1 = dy1, -dx1, dx1 * y1 - dy1 * x1
            p2, q2, r2 = dy2, -dx2, dx2 * y2 - dy2 * x2
            det = p1 * q2 - p2 * q1
            if det != 0:
                yp = (p2 * r1 - p1 * r2) / det
                xp = (r2 * q1 - q2 * r1) / det
                if LOWER <= xp <= UPPER and LOWER <= yp <= UPPER:
                    if (xp - x1) / dx1 > 0 and (xp - x2) / dx2 > 0 and (yp - y1) / dy1 > 0 and (yp - y2) / dy2 > 0:
                        count += 1
    return count


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    LOWER = 200000000000000
    UPPER = 400000000000000
    inp = aoc.readlines(get_data(day=24, year=2023))
    print(solve(inp))
