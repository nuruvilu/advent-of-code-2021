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
    curr = 0
    start = -1
    maybe = {}
    gears = {}
    notgears = set()
    for i, row in enumerate(inp):
        for j, item in enumerate(row):
            if item.isdigit():
                curr = 10*curr + int(item)
                if start == -1:
                    start = j
            elif curr:
                checked = set()
                for k in range(start, j):
                    for ip, kp in aoc.adjsdiags2((i, k)):
                        if aoc.inbounds2(ip, kp, len(inp), len(row)) and inp[ip][kp] == '*':
                            if (ip, kp) in notgears or (ip, kp) in checked:
                                continue
                            checked.add((ip, kp))
                            if (ip, kp) in gears:
                                gears.pop((ip, kp))
                                notgears.add((ip, kp))
                            elif (ip, kp) in maybe:
                                num = maybe.pop((ip, kp))
                                gears[(ip, kp)] = num * curr
                            else:
                                maybe[(ip, kp)] = curr
                curr = 0
                start = -1
        if curr:
            checked = set()
            for k in range(start, j):
                for ip, kp in aoc.adjsdiags2((i, k)):
                    if aoc.inbounds2(ip, kp, len(inp), len(row)) and inp[ip][kp] == '*':
                        if (ip, kp) in notgears or (ip, kp) in checked:
                            continue
                        checked.add((ip, kp))
                        if (ip, kp) in gears:
                            gears.pop((ip, kp))
                            notgears.add((ip, kp))
                        elif (ip, kp) in maybe:
                            num = maybe.pop((ip, kp))
                            gears[(ip, kp)] = num * curr
                        else:
                            maybe[(ip, kp)] = curr
            curr = 0
            start = -1
    print(maybe, gears, notgears)
    return sum(gears.values())


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=3, year=2023))
    print(solve(inp))
