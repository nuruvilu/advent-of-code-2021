import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict

import common as aoc


def solve(inp):  # go and grab yourself a drink :^)
    cap = 4_000_000
    possible = set()
    sensors = []
    for sensor_num, line in enumerate(inp):
        groups = re.match(
            r'Sensor at x=(-{0,1}\d+), y=(-{0,1}\d+): closest beacon'
            r' is at x=(-{0,1}\d+), y=(-{0,1}\d+)',
            line
        ).groups()
        groups = [int(x) for x in groups]
        sensor, beacon = [tuple(x) for x in aoc.partition(groups, 2)]
        target = aoc.mandist(sensor, beacon)
        sensors.append((sensor, target))
        for i in range(target):
            for p in [(sensor[0] + i, sensor[1] - target + i + 1),
                      (sensor[0] + target - i + 1, sensor[1] - i),
                      (sensor[0] - i, sensor[1] + target - i + 1),
                      (sensor[0] - target + i + 1, sensor[1] + i)]:
                if 0 <= p[0] <= cap and 0 <= p[1] <= cap:
                    possible.add(p)
        print(sensor_num)
    for sensor, target in sensors:
        print(sensor)
        possible = set(p for p in possible if aoc.mandist(p, sensor) > target)
    x, y = list(possible)[0]
    return x * 4_000_000 + y


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
