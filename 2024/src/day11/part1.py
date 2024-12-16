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
    stones = []
    for stone in inp.split():
        stones.append(int(stone))
    for i in range(25):
        print(i)
        new_stones = []
        for stone in stones:
            stone_str = str(stone)
            if stone == 0:
                new_stones.append(1)
            elif len(stone_str) % 2 == 0:
                middle = len(stone_str) // 2
                new_stones.append(int(stone_str[:middle]))
                new_stones.append(int(stone_str[middle:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=11, year=2024))
    print(solve(inp))
