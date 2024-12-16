import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce, cmp_to_key, cache
from pathlib import Path
from collections import defaultdict
from multiprocessing import Pool

import common as aoc
from aocd import get_data


@cache
def check_2(target, curr, nums):
    if not nums:
        return curr == target
    return check_2(target, curr + nums[0], nums[1:]) or check_2(target, curr * nums[0], nums[1:])


def do_thing(t):
    i, target, nums = t
    print(i)
    result = check_2(target, 0, nums)
    print(i, 'done', result)
    return target if result else 0


def solve(inp):
    lines = []
    for i, line in enumerate(inp):
        target, nums = line.split(':')
        target = int(target)
        nums = tuple([int(n) for n in nums.strip().split()])
        lines.append((i, target, nums))
    with Pool(850 // 50) as p:
        return sum(p.map(do_thing, lines))


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=7, year=2024))
    print(solve(inp))
