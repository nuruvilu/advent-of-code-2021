import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce, cache
from pathlib import Path

import common as aoc
from aocd import get_data


@cache
def blink_better(stone, reps):
    if reps == 0:
        return 1
    if stone == 0:
        return blink_better(1, reps - 1)
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        middle = len(stone_str) // 2
        return blink_better(int(stone_str[:middle]), reps - 1) + blink_better(int(stone_str[middle:]), reps - 1)
    return blink_better(stone * 2024, reps - 1)


def solve(inp):
    c = 0
    for stone in inp.split():
        c += blink_better(int(stone), 75)
    return c


if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=11, year=2024))
    print(solve(inp))
