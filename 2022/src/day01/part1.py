import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    elves = inp.split('\n\n')
    mx = -9
    for elf in elves:
        cals = sum([int(e) for e in elf.split('\n')])
        if cals > mx:
            mx = cals
    return mx


if __name__ == '__main__':
    inp = aoc.read('input.txt')
    print(solve(inp))
