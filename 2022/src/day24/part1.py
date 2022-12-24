import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict
from pathlib import Path

import common as aoc


DIRECTIONS = {
    '^': 'U',
    'v': 'D',
    '<': 'L',
    '>': 'R'
}


def udlr(facing, pos, width, height):
    if facing == 'U':
        facing = 'D'
    elif facing == 'D':
        facing = 'U'
    x, y = aoc.udlr_xy(facing, pos)
    if x < 0:
        x = width - 1
    if x >= width:
        x = 0
    if y < 0:
        y = height - 1
    if y >= height:
        y = 0
    return x, y


def vis(blizzards, pos, width, height):
    out = ''
    bs = defaultdict(list)
    dx = {v: k for k, v in DIRECTIONS.items()}
    for bpos, bdir in blizzards:
        bs[bpos].append(bdir)
    for y in range(height):
        for x in range(width):
            if (x, y) == pos:
                out += 'E'
            elif bs[(x, y)]:
                if len(bs[(x, y)]) == 1:
                    out += dx[bs[(x, y)][0]]
                else:
                    out += str(len(bs[(x, y)]))
            else:
                out += '.'
        out += '\n'
    print(out)


def solve(inp):
    width = len(inp[0]) - 2
    height = len(inp) - 2
    print(width, height)
    blizzards = []
    for y, line in enumerate(inp[1:-1]):
        for x, spot in enumerate(line[1:-1]):
            if spot in DIRECTIONS:
                blizzards.append(((x, y), DIRECTIONS[spot]))
    blizzards = tuple(blizzards)
    start = (0, -1)
    target = (width - 1, height)
    visited_weights = set()

    def is_target(prio_item):
        pos, _ = prio_item
        return pos == target
    
    def step(prio_item):
        pos, blizzards = prio_item.item
        if prio_item.total_weight not in visited_weights:
            print(prio_item.total_weight)
            # vis(blizzards, pos, width, height)
            visited_weights.add(prio_item.total_weight)
        # print(prio_item)
        new_blizzards = []
        for bpos, bdir in blizzards:
            new_blizzards.append((udlr(bdir, bpos, width, height), bdir))
        blocs = set(bbpos for bbpos, _ in new_blizzards)
        new_blizzards = tuple(new_blizzards)
        ret = []
        for x, y in list(aoc.adjs(pos)) + [pos]:
            if aoc.inbounds2(y, x, height, width) or (x, y) in ((0, -1), target):
                if (x, y) not in blocs:
                    # print(x, y, prio_item.path)
                    ret.append((1, ((x, y), new_blizzards)))
        return ret

    def h(state):
        pos, _ = state
        return aoc.mandist(pos, target)

    return aoc.astar((start, blizzards), step, h, is_target).total_weight


if __name__ == '__main__':
    inp = aoc.readgrid('input.txt')
    print(solve(inp))
