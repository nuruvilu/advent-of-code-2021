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


SIZE_X, SIZE_Y = 101, 103
ATTEMPT_SIZE = 10_000


def solve(inp):
    bots = []
    for line in inp:
        start_x, start_y, dx, dy = [int(n) for n in re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line).groups()]
        bots.append(((start_x, start_y), (dx, dy)))
    i = 0
    while i < ATTEMPT_SIZE:
        i += 1
        new_bots = []
        occupied = set()
        for (start_x, start_y), (dx, dy) in bots:
            end_x = (start_x + dx) % SIZE_X
            end_y = (start_y + dy) % SIZE_Y
            new_bots.append(((end_x, end_y), (dx, dy)))
            occupied.add((end_x, end_y))
        bots = new_bots
        if i % 200 == 0:
            print(i)
        if len(occupied) == len(bots):
            add_muh = f'\n{i}\n'
            for j in range(SIZE_Y):
                for k in range(SIZE_X):
                    add_muh += '#' if (k, j) in occupied else '.'
                add_muh += '\n'
            print(add_muh)
            return i


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=14, year=2024))
    print(solve(inp))
