import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    s = 0
    for group in aoc.partition(inp, 3):
        top, mid = set(group[0]), set(group[1])
        for c in group[2]:
            if c in top and c in mid:
                if c.islower():
                    s += ord(c) - ord('a') + 1
                else:
                    s += ord(c) - ord('A') + 27
                break
    return s


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
