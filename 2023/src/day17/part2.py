import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


dirs = {
    'L': 'UD',
    'R': 'UD',
    'U': 'LR',
    'D': 'LR'
}


# Returns wrong answer, I guessed the answer by luck. I have given up on fixing it.
def solve(inp):
    def step(p_item):
        nexts = []
        coords, drct, reps = p_item.item
        for ch in dirs[drct] + drct:
            if (ch == drct and reps < 10) or (ch != drct and reps > 3):
                nxt = aoc.udlr_ij(ch, coords)
                if aoc.inbounds2(nxt[0], nxt[1], len(inp), len(inp[0])):
                    nexts.append((inp[nxt[0]][nxt[1]], (nxt, ch, (reps + 1) if ch == drct else 1)))
        return nexts
    def is_target(p_item):
        loc, _, reps = p_item.item
        return reps > 3 and loc == (len(inp) - 1, len(inp[0]) - 1)
    result = aoc.dijkstra(((0, 0), 'R', 1), step, is_target)
    print(result.item)
    path = set(p for p, _, _ in result.path)
    for i, row in enumerate(inp):
        print(''.join('#' if (i, j) in path else str(num) for j, num in enumerate(row)))
    return result.total_weight


if __name__ == '__main__':
    #inp = aoc.readgridnums(Path('sample.txt'))
    inp = aoc.readgridnums(get_data(day=17, year=2023))
    print(solve(inp))
