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
    tot = 0
    curr = 0
    start = -1
    for i, row in enumerate(inp):
        for j, item in enumerate(row):
            if item.isdigit():
                curr = 10*curr + int(item)
                if start == -1:
                    start = j
            elif curr:
                counted = False
                for k in range(start, j):
                    for ip, kp in aoc.adjsdiags2((i, k)):
                        if aoc.inbounds2(ip, kp, len(inp), len(row)) and inp[ip][kp] != '.' and not inp[ip][kp].isalnum():
                            counted = True
                if counted:
                    print(curr)
                    tot += curr
                curr = 0
                start = -1
        if curr:
            counted = False
            for k in range(start, len(row)):
                for ip, kp in aoc.adjsdiags2((i, k)):
                    if aoc.inbounds2(ip, kp, len(inp), len(row)) and inp[ip][kp] != '.' and not inp[ip][kp].isalnum():
                        counted = True
            if counted:
                print(curr)
                tot += curr
            curr = 0
            start = -1
    return tot


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=3, year=2023))
    print(solve(inp))
