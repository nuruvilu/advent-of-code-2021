import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    cycle = 0
    x = 1
    points = 0
    nextp = 20
    for op in inp:
        hold = 0
        if op == 'noop':
            cycle += 1
        else:
            _, num = op.split()
            hold = int(num)
            cycle += 2
        if nextp <= 220 and cycle >= nextp:
            tcycle = (cycle // 10) * 10
            points += tcycle * x
            nextp += 40
        x += hold
    return points


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
