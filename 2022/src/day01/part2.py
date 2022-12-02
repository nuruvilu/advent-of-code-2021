import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    elves = inp.split('\n\n')
    t3 = []
    for elf in elves:
        cals = sum([int(e) for e in elf.split('\n')])
        if len(t3) == 3 and cals > t3[0]:
            heappop(t3)
            heappush(t3, cals)
        elif len(t3) < 3:
            heappush(t3, cals)
    return sum(t3)


if __name__ == '__main__':
    inp = aoc.read('input.txt')
    print(solve(inp))
