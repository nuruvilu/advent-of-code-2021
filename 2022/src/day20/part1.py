import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    for _ in range(len(inp)):
        i = 0
        while isinstance(inp[i], tuple):
            i += 1
        val = inp.pop(i)
        j = (i + val) % len(inp)
        if j == 0:
            inp.append((val, True))
        else:
            inp.insert(j, (val, True))
        # print(inp)
    s = 0
    # print(inp)
    zero = inp.index((0, True))
    for n in (1000, 2000, 3000):
        s += inp[(zero + n) % len(inp)][0]
        print(inp[(zero + n) % len(inp)])
    return s


if __name__ == '__main__':
    inp = aoc.readnums('input.txt')
    print(solve(inp))
