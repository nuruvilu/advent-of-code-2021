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
    visited = set()
    cost = 0
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if (i, j) in visited:
                continue
            q = [(i, j)]
            area = 0
            perimiter = 0
            while q:
                ip, jp = q.pop(0)
                if (ip, jp) in visited:
                    continue
                visited.add((ip, jp))
                area += 1
                perimiter_temp = 4
                for ipp, jpp in aoc.adjs((ip, jp)):
                    if aoc.inbounds2(ipp, jpp, len(inp), len(inp[0])) and inp[ipp][jpp] == c:
                        perimiter_temp -= 1
                        q.append((ipp, jpp))
                perimiter += perimiter_temp
            cost += area * perimiter
    return cost


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=12, year=2024))
    print(solve(inp))
