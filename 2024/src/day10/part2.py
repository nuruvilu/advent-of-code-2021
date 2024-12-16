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
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == 0:
                q = [(i, j)]
                while q:
                    curr_i, curr_j = q.pop(0)
                    for next_i, next_j in aoc.adjs((curr_i, curr_j)):
                        if aoc.inbounds2(next_i, next_j, len(inp), len(inp[0])) \
                                and inp[next_i][next_j] - 1 == inp[curr_i][curr_j]:
                            if inp[next_i][next_j] == 9 and (next_i, next_j):
                                total += 1
                            else:
                                q.append((next_i, next_j))
    return total

if __name__ == '__main__':
    #inp = aoc.readgridnums(Path('sample.txt'))
    inp = aoc.readgridnums(get_data(day=10, year=2024))
    print(solve(inp))
