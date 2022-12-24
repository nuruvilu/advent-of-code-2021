import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict
from pathlib import Path
from functools import lru_cache

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


def vis(bs, pos, width, height):
    out = ''
    dx = {v: k for k, v in DIRECTIONS.items()}
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

    @lru_cache
    def gen_blizzards(elapsed):
        bzrds = defaultdict(list)
        for bpos, bdir in blizzards:
            (x, y) = bpos
            if bdir == 'U':
                y = (y - elapsed) % height
            elif bdir == 'D':
                y = (y + elapsed) % height
            elif bdir == 'L':
                x = (x - elapsed) % width
            else:
                x = (x + elapsed) % width
            bzrds[(x, y)].append(bdir)
        return bzrds

    start = (0, -1)
    target = (width - 1, height)
    visited_weights = set()
    current_phase = [0]

    def is_target(prio_item):
        pos, phase, _ = prio_item
        if phase > current_phase[0]:
            current_phase[0] = phase
        return pos == target and phase == 2

    def step(prio_item):
        pos, phase, steps = prio_item.item
        if phase < current_phase[0]:
            return []
        # blocs_old = gen_blizzards(prio_item.total_weight)
        blocs = gen_blizzards(prio_item.total_weight + 1)

        if prio_item.total_weight not in visited_weights:
            print(prio_item.total_weight)
            # vis(blocs_old, pos, width, height)
            visited_weights.add(prio_item.total_weight)
        # if prio_item.total_weight > 10:
        #     return []
        # print(prio_item)
        ret = []
        for x, y in list(aoc.adjs(pos)) + [pos]:
            if aoc.inbounds2(y, x, height, width) or (x, y) in ((0, -1), target):
                if not blocs[(x, y)]:
                    # print((x, y))
                    new_phase = phase
                    if phase == 0 and (x, y) == target:
                        new_phase = 1
                    elif phase == 1 and (x, y) == start:
                        new_phase = 2
                    # print(x, y, prio_item.path)
                    ret.append((1, ((x, y), new_phase, (steps + 1) % (width * height))))
        return ret

    def h(state):
        pos, phase, _ = state
        if phase in (0, 2):
            return aoc.mandist(pos, target)
        else:
            return aoc.mandist(pos, start)

    return aoc.astar((start, 0, 0), step, h, is_target).total_weight


if __name__ == '__main__':
    inp = aoc.readgrid('input.txt')
    print(solve(inp))
