import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce, cache
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    patterns, towels = inp
    patterns = patterns[0].split(', ')
    @cache
    def build_towel(towel):
        if not towel:
            return 1
        return sum(build_towel(towel[len(p):]) for p in patterns if towel.startswith(p))
    return sum(build_towel(towel) for towel in towels)


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=19, year=2024))
    print(solve(inp))
