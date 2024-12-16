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


def solve(inp):
    return sum(int(l) * int(r) for l, r in re.findall(r'mul\((\d+)\,(\d+)\)', inp))


if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=3, year=2024))
    print(solve(inp))
