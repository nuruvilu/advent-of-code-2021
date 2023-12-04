import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path
from collections import defaultdict

import common as aoc
from aocd import get_data


def solve(inp):
    instances = defaultdict(int)
    for i, line in enumerate(inp, start=1):
        _, numbers = line.split(':')
        winners, drawn = numbers.split('|')
        winners = set(winners.strip().split())
        count = len([x for x in drawn.strip().split() if x in winners])
        for j in range(i + 1, min(len(inp), i + count) + 1):
            instances[j] += instances[i] + 1
    return len(inp) + sum(instances.values())


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=4, year=2023))
    print(solve(inp))
