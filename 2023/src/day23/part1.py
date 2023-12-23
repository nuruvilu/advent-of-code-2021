import math
import operator

import sys
sys.path.append('..')

from collections import deque
from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    start = None
    stop = None
    for j, item in enumerate(inp[0]):
        if item == '.':
            start = (0, j)
    for j, item in enumerate(inp[-1]):
        if item == '.':
            stop = (len(inp) - 1, j)
    #print(start, stop)
    def step(curr):
        nexts = []
        for (i, j) in aoc.adjs(curr):
            if aoc.inbounds2(i, j, len(inp), len(inp[0])) and inp[i][j] != '#':
                #if inp[curr[0]][curr[1]] == 'v':
                    #print(curr, i, j)
                if inp[curr[0]][curr[1]] == '.':
                    nexts.append((i, j))
                elif inp[curr[0]][curr[1]] == '>' and j == curr[1] + 1:
                    nexts.append((i, j))
                elif inp[curr[0]][curr[1]] == '<' and j == curr[1] - 1:
                    nexts.append((i, j))
                elif inp[curr[0]][curr[1]] == '^' and i == curr[0] - 1:
                    nexts.append((i, j))
                elif inp[curr[0]][curr[1]] == 'v' and i == curr[0] + 1:
                    nexts.append((i, j))
        #print(nexts)
        return nexts
    def is_target(p_item):
        return p_item == stop
    q = deque([(start, set())])
    longest = 0
    while q:
        pos, visited = q.popleft()
        #print(pos)
        if is_target(pos):
            longest = max(longest, len(visited))
        else:
            for p in step(pos):
                if p not in visited:
                    q.append((p, visited | {pos}))
    #print(start, stop)
    return longest


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=23, year=2023))
    print(solve(inp))
