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
    pattern = inp[0][0]
    graph = {}
    for line in inp[-1]:
        head, tail = line.split(' = ')
        left, right = tail.strip().split(', ')
        left, right = left[1:], right[:-1]
        graph[head] = (left, right)
    i = 0
    curr = 'AAA'
    while True:
        if curr == 'ZZZ':
            return i
        step = pattern[i % len(pattern)]
        if step == 'L':
            curr = graph[curr][0]
        else:
            curr = graph[curr][1]
        i += 1


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=8, year=2023))
    print(solve(inp))
