import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc


rocks = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],  # _
    [(2, 1), (3, 2), (3, 1), (3, 0), (4, 1)],  # +
    [(2, 0), (3, 0), (4, 2), (4, 1), (4, 0)],  # J
    [(2, 3), (2, 2), (2, 1), (2, 0)],  # |
    [(2, 1), (2, 0), (3, 1), (3, 0)]  # ■
]


def collides(rock, blocked):
    for x, y in rock:
        if (x, y) in blocked or not (0 <= x <= 6) or y < 0:
            return True
    return False


def emit_drops(blocked, max_height):
    s = ''
    for y in range(max_height, -1, -1):
        s += '|' + ''.join(['#' if (x, y) in blocked else ' ' for x in range(0, 7)]) + '|\n'
    s += '|-------|\n'
    Path('./out.txt').write_text(s)


def solve(inp):
    rocks_dropped = 0
    max_height = 0
    rock_idx = 0
    flow_idx = 0
    blocked = set()
    while rocks_dropped < 2022:
        print(rocks_dropped)
        rock = [(x, y + max_height + 3) for x, y in rocks[rock_idx]]
        while True:
            flow = inp[flow_idx]
            flow_idx = (flow_idx + 1) % len(inp)
            new_rock = [(x + (1 if flow == '>' else -1), y) for x, y in rock]
            if not collides(new_rock, blocked):
                # print(flow, new_rock)
                rock = new_rock
            new_rock = [(x, y - 1) for x, y in rock]
            if collides(new_rock, blocked):
                rocks_dropped += 1
                for block in rock:
                    blocked.add(block)
                    if block[1] + 1 > max_height:
                        max_height = block[1] + 1
                break
            rock = new_rock
        rock_idx = (rock_idx + 1) % len(rocks)
    return max_height


if __name__ == '__main__':
    inp = aoc.read('input.txt')
    print(solve(inp))
