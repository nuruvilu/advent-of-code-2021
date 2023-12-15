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
    seq = ''.join(inp)
    steps = seq.split(',')
    total = 0
    for step in steps:
        curr = 0
        for ch in step:
            curr += ord(ch)
            curr *= 17
            curr %= 256
        total += curr
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=15, year=2023))
    print(solve(inp))
