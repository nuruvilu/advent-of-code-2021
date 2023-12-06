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
    times, distances = inp
    times = [int(x) for x in times.split(':')[1].strip().split()]
    distances = [int(x) for x in distances.split(':')[1].strip().split()]
    tally = 1
    for t, d in zip(times, distances):
        surpassed = False
        count = 0
        for i in range(1, t):
            dist = i * (t - i)
            if surpassed and dist <= d:
                break
            elif dist > d:
                count += 1
                surpassed = True
        tally *= count
    return tally


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=6, year=2023))
    print(solve(inp))
