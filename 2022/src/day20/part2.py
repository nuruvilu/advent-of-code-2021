import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    key = 811589153
    inp = [key * n for n in inp]
    for k in range(len(inp)):
        i = 0
        while isinstance(inp[i], tuple):
            i += 1
        val = inp.pop(i)
        j = (i + val) % len(inp)
        if j == 0 and val != 0:
            inp.append((val, k))
        else:
            inp.insert(j, (val, k))
    for time in range(2, 11):
        print(time)
        for curr in range(len(inp)):
            i = 0
            while inp[i][-1] != curr:
                i += 1
            val, k = inp.pop(i)
            j = (i + val) % len(inp)
            if j == 0 and val != 0:
                inp.append((val, k))
            else:
                inp.insert(j, (val, k))
    s = 0
    zero = [i for i, (val, _) in enumerate(inp) if val == 0][0]
    for n in (1000, 2000, 3000):
        s += inp[(zero + n) % len(inp)][0]
        print(inp[(zero + n) % len(inp)])
    return s


if __name__ == '__main__':
    inp = aoc.readnums('input.txt')
    print(solve(inp))
