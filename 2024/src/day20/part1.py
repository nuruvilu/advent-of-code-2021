import math
import operator

import sys
sys.path.append('..')

from collections import deque, defaultdict
from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def find_path(start, end, walls, memo, h, w):
    q = [(start, [start])]
    visited = set()
    while q:
        curr, path = q.pop(0)
        #print(curr, path)
        if curr == end:
            return path
        if curr in visited:
            continue
        if curr in memo:
            return path + memo[curr]
        visited.add(curr)
        for adj in aoc.adjs(curr):
            if adj not in walls and aoc.inbounds2(adj[0], adj[1], h, w):
                q.append((adj, path + [adj]))
    return None


def populate_memo(memo, path):
    for i, p in enumerate(path):
        memo[p] = path[i:]


def solve(inp):
    walls = set()
    start, end = None, None
    h, w = len(inp), len(inp[0])
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                end = (i, j)
            elif c == '#':
                walls.add((i, j))
    cheatless_path = find_path(start, end, walls, {}, h, w)
    target = len(cheatless_path)
    #print(target)
    way_to_end, way_to_start = {}, {}
    populate_memo(way_to_end, cheatless_path)
    populate_memo(way_to_start, cheatless_path[::-1])
    considered = set()
    savings = defaultdict(list)
    for i_wall, wall in enumerate(walls):
        print(i_wall, '/', len(walls))
        for adj_i, adj in enumerate(aoc.adjs(wall)):
            if not aoc.inbounds2(adj[0], adj[1], h, w) or adj in walls:
                continue
            for adj_2 in aoc.adjs(wall)[adj_i+1:]:
                if not aoc.inbounds2(adj_2[0], adj_2[1], h, w) or adj_2 in walls:
                    continue
                to_start_1 = way_to_start[adj]
                to_end_1 = way_to_end[adj]
                to_start_2 = way_to_start[adj_2]
                to_end_2 = way_to_end[adj_2]
                saveds = [len(to_start_1) + len(to_end_2) + 1, len(to_start_2) + len(to_end_1) + 1]
                for i, saved in enumerate(saveds):
                    if saved < target:
                        savings[target - saved].append((wall, adj) if i else (wall, adj_2))
    #print(sorted((k, len(v)) for k, v in savings.items()))
    return sum(len(v) for k, v in savings.items() if k >= 100)


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=20, year=2024))
    print(solve(inp))
