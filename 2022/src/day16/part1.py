import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):  # SLOW
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
    pressure = [-1]
    progress = [30]
    path = [None]

    def step(curr):
        mins_left, curr_pressure, turned, pos = curr.item
        if mins_left < progress[0]:
            print(mins_left)
            progress[0] = mins_left
        if mins_left == 0 or len(turned) // 2 >= worthwhile_cnt:
            if curr_pressure > pressure[0]:
                pressure[0] = curr_pressure
                path[0] = curr.path + [curr.item]
            return []
        elif pos not in turned and valves[pos][0] > 0:
            turned_p = turned + pos
            return [(
                mins_left - 1,
                curr_pressure + (mins_left - 1) * valves[pos][0],
                turned_p,
                pos
            )]
        else:
            res = []
            for tunnel in valves[pos][1]:
                res.append((
                    mins_left - 1,
                    curr_pressure,
                    turned,
                    tunnel
                ))
            return res
    
    try:
        aoc.bfs((30, 0, '', "AA"), step, lambda _: False)
    except RuntimeError:
        print('done!')
    
    return pressure[0]


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
