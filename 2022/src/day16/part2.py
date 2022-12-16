import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def release_pressure(valves, turned):
    total = 0
    for t in turned:
        total += valves[t][0]
    return total


def solve(inp):
    valves = {}
    worthwhile_cnt = 0
    for line in inp:
        head = re.match(r'Valve ([a-zA-Z]{2}) has flow rate=(\d+);.+', line)
        name, rate = head.groups()
        rate = int(rate)
        if 'valves' in line:
            tunnels = line.split(' valves ')[1].split(', ')
        else:
            tunnels = line.split(' valve ')[1].split(', ')
        valves[name] = (rate, tunnels)
        if rate > 0:
            worthwhile_cnt += 1
    states = [(0, set(), 'AA', 'AA')]
    for i in range(26):
        print('mins:', i)
        new_states = []
        for pressure, turned, me, ele in states:
            if len(turned) // 2 >= worthwhile_cnt:
                new_states.append((
                    release_pressure(valves, turned) + pressure,
                    turned,
                    me,
                    ele
                ))
                continue
            mes = [(v, turned) for v in valves[me][1]]
            eles = [(v, turned) for v in valves[ele][1]]
            if me not in turned and valves[me][0] > 0:
                mes.append((me, turned | {me}))
            if ele not in turned and valves[ele][0] > 0:
                eles.append((ele, turned | {ele}))
            for me2, me_t in mes:
                for ele2, ele_t in eles:
                    new_states.append((
                        release_pressure(valves, turned) + pressure,
                        turned | me_t | ele_t,
                        me2,
                        ele2
                    ))
        states = sorted(new_states, key=lambda t: t[0], reverse=True)[:8_000]
    return states[0]


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
