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
    heads = []
    for line in inp[-1]:
        head, tail = line.split(' = ')
        left, right = tail.strip().split(', ')
        left, right = left[1:], right[:-1]
        graph[head] = (left, right)
        if head.endswith('A'):
            heads.append(head)
    x = None
    for h in heads:
        i = 0
        curr = h
        while True:
            #print(i, curr)
            if curr.endswith('Z'):
                if x == None:
                    x = i
                else:
                    x = aoc.lcm(x, i)
                break
            step = pattern[i % len(pattern)]
            if step == 'L':
                curr = graph[curr][0]
            else:
                curr = graph[curr][1]
            i += 1
    return x


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=8, year=2023))
    print(solve(inp))
