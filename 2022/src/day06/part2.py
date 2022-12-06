import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    slider = []
    for i, c in enumerate(inp, start=1):
        if len(slider) < 13:
            slider.append(c)
        elif c not in slider and len(set(slider)) == 13:
            return i
        else:
            slider = slider[1:]
            slider.append(c)


if __name__ == '__main__':
    inp = aoc.read('input.txt')
    print(solve(inp))
