import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    total = 0
    for line in inp:
        points = 0
        _, numbers = line.split(':')
        winners, drawn = numbers.split('|')
        winners = set(winners.strip().split())
        for x in drawn.strip().split():
            if x in winners:
                if points:
                    points *= 2
                else:
                    points = 1
        total += points
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=4, year=2023))
    print(solve(inp))
