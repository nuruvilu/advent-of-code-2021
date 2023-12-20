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
    xmin, xmax, ymin, ymax = 0, 0, 0, 0
    pos = (0, 0)
    trench = {pos}
    for line in inp:
        direction, num, _color = line.split()
        num = int(num)
        for _ in range(num):
            pos = aoc.udlr_xy(direction, pos)
            x, y = pos
            xmin = min(x, xmin)
            xmax = max(x, xmax)
            ymin = min(y, ymin)
            ymax = max(y, ymax)
            trench.add(pos)
    seen = set()
    for x in range(xmin + 1, xmax):
        for y in range(ymin + 1, ymax):
            #print(x, y)
            if (x, y) in trench:
                continue
            curr_seen = set()
            def step(p_item):
                return [p for p in aoc.adjs(p_item.item) if p not in trench]
            def is_target(p_item):
                loc = p_item.item
                if loc in seen:
                    return True
                #print(loc)
                curr_seen.add(loc)
                cx, cy = loc
                return cx <= xmin or cx >= xmax or cy <= ymin or cy >= ymax
            try:
                aoc.bfs((x, y), step, is_target)
            except:
                trench |= curr_seen
            seen |= curr_seen
    return len(trench)


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=18, year=2023))
    print(solve(inp))
