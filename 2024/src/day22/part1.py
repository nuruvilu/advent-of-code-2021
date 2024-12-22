import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


PRUNE = 16777216


def mix_and_prune(n, secret):
    return (n ^ secret) % PRUNE


def solve(inp):
    total = 0
    for i, secret in enumerate(inp):
        print(i, '/', len(inp))
        curr = secret
        for _ in range(2000):
            curr = mix_and_prune(curr << 6, curr)
            curr = mix_and_prune(curr >> 5, curr)
            curr = mix_and_prune(curr << 11, curr)
        total += curr
    return total


if __name__ == '__main__':
    #inp = aoc.readnums(Path('sample.txt'))
    inp = aoc.readnums(get_data(day=22, year=2024))
    print(solve(inp))
