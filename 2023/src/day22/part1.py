import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


X, Y, Z, CUBE = 0, 1, 2, 3


def solve(inp):
    bricks = []
    for line in inp:
        ends = line.split('~')
        l, r = [tuple(map(int, n)) for n in (e.split(',') for e in ends)]
        axis = 0
        while axis < 3 and l[axis] == r[axis]:
            axis += 1
        bricks.append((axis, min(l[2], r[2]), (l, r)))
    z_arranged = sorted(bricks, key=lambda b: b[1])
    sol = {}
    uniquely_supporting = set()
    for brick in z_arranged:
        axis, z_pos, (l, r) = brick
        supporters = set()
        height = 1
        if axis != CUBE:
            ll, rr = min(l[axis], r[axis]), max(l[axis], r[axis])
        points = []
        if axis == X:
            points = [(x, l[1]) for x in range(ll, rr + 1)]
        elif axis == Y:
            points = [(l[0], y) for y in range(ll, rr + 1)]
        else:
            if axis == Z:
                height = rr - ll + 1
            points = [(l[0], l[1])]
        min_bottom = 1
        for point in points:
            if point in sol:
                bot, support = sol[point]
                if bot == min_bottom:
                    supporters.add(support)
                elif bot > min_bottom:
                    supporters = {support}
                    min_bottom = bot
        if len(supporters) == 1:
            for support in supporters:
                uniquely_supporting.add(support)
        for point in points:
            sol[point] = (min_bottom + height, brick)
    return len(bricks) - len(uniquely_supporting)


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=22, year=2023))
    print(solve(inp))
