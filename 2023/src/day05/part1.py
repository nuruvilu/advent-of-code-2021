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
    _, seeds = inp[0][0].split(':')
    seeds = [int(s) for s in seeds.strip().split()]
    almanac = []
    loc = 9e10
    for mapping in inp[1:]:
        almanac.append([])
        for row in mapping[1:]:
            almanac[-1].append(tuple(map(int, row.split())))
    for seed in seeds:
        x = seed
        for step in almanac:
            done = False
            for dest, src, rng in step:
                if not done and x >= src and x <= src + rng:
                    x = dest + (x - src)
                    done = True
        loc = min(x, loc)
    return loc


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=5, year=2023))
    print(solve(inp))
