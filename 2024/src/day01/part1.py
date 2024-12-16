import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data, submit


def solve(inp):
    left, right = [], []
    for line in inp:
        print(line)
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    s = 0
    for l, r in zip(left, right):
        s += abs(l - r)
    return s


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=1, year=2024))
    answer = solve(inp)
    print(answer)
    #submit(answer)
