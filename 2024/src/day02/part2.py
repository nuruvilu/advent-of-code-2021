import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import re
import common as aoc
from aocd import get_data, submit


def solve(inp):
    s = 0
    for report in inp:
        for i, _ in enumerate(report):
            rp = report[0:i] + report[i+1:]
            inc = None
            for l, r in aoc.window(rp, 2):
                if inc is None:
                    if l == r:
                        print(rp, l, r, 'eq')
                        break
                    elif l > r:
                        inc = False
                    else:
                        inc = True
                elif (inc and l >= r) or ((not inc) and l <= r):
                    print(rp, l, r, inc)
                    break
                if abs(l - r) > 3:
                    print(rp, l, r)
                    break
            else:
                print(report)
                s += 1
                break
    return s


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readrownums(get_data(day=2, year=2024))
    answer = solve(inp)
    print(answer)
    #submit(answer)
