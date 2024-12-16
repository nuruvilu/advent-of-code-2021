import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


DIRECTIONS = 'UDLR'
SIDE_CORRELATIONS = ['LR', 'LR', 'DU', 'DU']


def solve(inp):
    # print(aoc.adjs((0, 0)))
    # print([aoc.udlr_ij(d, (0, 0)) for d in DIRECTIONS])
    visited = set()
    cost = 0
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            counted_sides = set()
            if (i, j) in visited:
                continue
            q = [(i, j)]
            area = 0
            side_count = 0
            while q:
                ip, jp = q.pop(0)
                if (ip, jp) in visited:
                    continue
                visited.add((ip, jp))
                area += 1
                sides = []
                for dir_i, (ipp, jpp) in enumerate(aoc.adjs((ip, jp))):
                    if aoc.inbounds2(ipp, jpp, len(inp), len(inp[0])) and inp[ipp][jpp] == c:
                        q.append((ipp, jpp))
                    else:
                        sides.append(dir_i)
                for dir_i in sides:
                    if (ip, jp, dir_i) in counted_sides:
                        continue
                    side_dir = DIRECTIONS[dir_i]
                    counted = False
                    for check_dir in SIDE_CORRELATIONS[dir_i]:
                        ipp, jpp = ip, jp
                        while aoc.inbounds2(ipp, jpp, len(inp), len(inp[0])) and inp[ipp][jpp] == c:
                            if (ipp, jpp) != (ip, jp) and (ipp, jpp, dir_i) in counted_sides:
                                counted = True
                                break
                            s_i, s_j = aoc.udlr_ij(side_dir, (ipp, jpp))
                            if aoc.inbounds2(s_i, s_j, len(inp), len(inp[0])) and inp[s_i][s_j] == c:
                                break
                            counted_sides.add((ipp, jpp, dir_i))
                            ipp, jpp = aoc.udlr_ij(check_dir, (ipp, jpp))
                        if counted:
                            break
                    if not counted:
                        #print(side_dir, (ip, jp))
                        side_count += 1
            cost += area * side_count
            print(c, area, side_count, area * side_count)
    return cost


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=12, year=2024))
    print(solve(inp))
