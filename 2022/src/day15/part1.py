import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict

import common as aoc


EMPTY = 0
BEACON = 1
NO_BEACON = 2


def solve(inp):
    marked = defaultdict(int)
    line_num = 2000000
    def_not_beacons = 0
    for line in inp:
        groups = re.match(
            r'Sensor at x=(-{0,1}\d+), y=(-{0,1}\d+): closest beacon'
            r' is at x=(-{0,1}\d+), y=(-{0,1}\d+)',
            line
        ).groups()
        groups = [int(x) for x in groups]
        sensor, beacon = [tuple(x) for x in aoc.partition(groups, 2)]
        target = aoc.mandist(sensor, beacon)
        marked[beacon] = BEACON
        i = 0
        while aoc.mandist((sensor[0] + i, line_num), sensor) <= target:
            for p in [(sensor[0] + i, line_num), (sensor[0] - i, line_num)]:
                if marked[p] == EMPTY:
                    marked[p] = NO_BEACON
                    def_not_beacons += 1
            i += 1
    return def_not_beacons


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
