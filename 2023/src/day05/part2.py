import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from multiprocessing import Pool  # :^)
from pathlib import Path

import common as aoc
from aocd import get_data


almanac = []


def handle_seeds(seed_pair):
    loc = 9e10
    start, rrr = seed_pair
    for seed in range(start, start + rrr):
        if seed % 100_000 == 0:
            print(((seed - start) / rrr) * 100)
        x = seed
        for step in almanac:
            done = False
            for dest, src, rng in step:
                if not done and x >= src and x <= src + rng:
                    x = dest + (x - src)
                    done = True
        loc = min(x, loc)
    return loc


def solve(inp):
    _, seeds = inp[0][0].split(':')
    seeds = aoc.partition([int(s) for s in seeds.strip().split()], 2)
    for mapping in inp[1:]:
        almanac.append([])
        for row in mapping[1:]:
            almanac[-1].append(tuple(map(int, row.split())))
    with Pool(len(seeds)) as p:
        results = p.map(handle_seeds, seeds)
        return min(results)


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=5, year=2023))
    print(solve(inp))
