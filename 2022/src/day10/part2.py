import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def pixelate(pixels, x, i):
    xp = x + 40 * (i // 40)
    if i in (xp - 1, xp, xp + 1):
        pixels[i] = '█'


def render(pixels):
    window = aoc.partition(pixels, 40)
    return '\n'.join(''.join(row) for row in window)


def solve(inp):
    cycle = -1
    x = 1
    pixels = [' '] * 240
    for op in inp:
        if op == 'noop':
            cycle += 1
            pixelate(pixels, x, cycle)
        else:
            _, num = op.split()
            cycle += 1
            pixelate(pixels, x, cycle)
            cycle += 1
            pixelate(pixels, x, cycle)
            x += int(num)
    return render(pixels)


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
