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
    return None


if __name__ == '__main__':
    # sample = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=13, year=2023))
    print(solve(inp))
