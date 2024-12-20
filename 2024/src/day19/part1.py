import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def is_towel_possible(patterns, towel):
    if not towel:
        return True
    for pattern in patterns:
        if towel.startswith(pattern) and is_towel_possible(patterns, towel[len(pattern):]):
            return True
    return False


def solve(inp):
    patterns, towels = inp
    patterns = patterns[0].split(', ')
    count = 0
    for towel in towels:
        if is_towel_possible(patterns, towel):
            count += 1
    return count


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=19, year=2024))
    print(solve(inp))
