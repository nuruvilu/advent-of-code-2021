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
    n = 0
    for line in inp:
        z = ''
        for ch in line:
            if ch.isdigit():
                if not z:
                    z = ch + ch
                else:
                    z = z[0] + ch
        n += int(z)
    return n


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=1, year=2023))
    answer = solve(inp)
    print(answer)
    submit(answer)
