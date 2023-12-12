import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce, lru_cache
from pathlib import Path

import common as aoc
from aocd import get_data


@lru_cache
def test(springs, groups):
    if not springs and not groups:
        return 1
    elif not springs:
        return 0
    elif springs[0] == ".":
        return test(springs[1:], groups)
    elif springs[0] == "#":
        if not groups or len(springs) < groups[0]:
            return 0
        elif "." in springs[:groups[0]]:
            return 0
        elif groups[0] < len(springs) and springs[groups[0]] == "#":
            return 0
        elif groups[0] < len(springs) and springs[groups[0]] == "?":
            return test(springs[groups[0] + 1:], groups[1:])
        else:
            return test(springs[groups[0]:], groups[1:])
    elif springs[0] == "?":
        return test("#" + springs[1:], groups) + test("." + springs[1:], groups)


def solve(inp):
    total = 0
    for line in inp:
        springs, groups = line.split()
        total += test("?".join([springs] * 5), tuple([int(x) for x in groups.split(',')] * 5))
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=12, year=2023))
    print(solve(inp))
