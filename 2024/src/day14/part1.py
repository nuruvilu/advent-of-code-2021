import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


RUNTIME = 100
SIZE_X, SIZE_Y = 101, 103
MID_X, MID_Y = SIZE_X // 2, SIZE_Y // 2


def solve(inp):
    quads = [0, 0, 0, 0]
    for line in inp:
        start_x, start_y, dx, dy = [int(n) for n in re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line).groups()]
        end_x = (start_x + dx*RUNTIME) % SIZE_X
        end_y = (start_y + dy*RUNTIME) % SIZE_Y
        if end_x < MID_X and end_y < MID_Y:
            quads[0] += 1
        elif end_x < MID_X and end_y > MID_Y:
            quads[1] += 1
        elif end_x > MID_X and end_y < MID_Y:
            quads[2] += 1
        elif end_x > MID_X and end_y > MID_Y:
            quads[3] += 1
    return reduce(operator.mul, quads)


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=14, year=2024))
    print(solve(inp))
