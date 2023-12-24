import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data
import z3


def solve(inp):
    hails = []
    for line in inp:
        pos, vel = line.split(' @ ')
        x, y, z = tuple(int(n) for n in pos.split(', '))
        dx, dy, dz = tuple(int(n) for n in vel.split(', '))
        hails.append(((x, y, z), (dx, dy, dz)))
    xi, yi, zi, dxi, dyi, dzi = z3.BitVecs( "xi yi zi dxi dyi dzi", 64)
    ts = [z3.BitVec(f't{i}', 64) for i, _ in enumerate(hails)]

    solver = z3.Solver()
    for i, ((x, y, z), (dx, dy, dz)) in enumerate(hails):
        solver.add(x + dx * ts[i] == xi + dxi * ts[i])
        solver.add(y + dy * ts[i] == yi + dyi * ts[i])
        solver.add(z + dz * ts[i] == zi + dzi * ts[i])
    solver.check()
    return solver.model().evaluate(xi + yi + zi)


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=24, year=2023))
    print(solve(inp))
