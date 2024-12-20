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


def find_path(start, end, accept, memo, max_depth = None):
    q = []
    heappush(q, aoc.PriorityItem(aoc.mandist(start, end), start, [start], 0))
    visited = set()
    while q:
        p_item = heappop(q)
        curr = p_item.item
        #print(curr, path)
        if curr == end:
            return p_item.path
        if curr != start and (curr, end) in memo:
            return p_item.path + memo[(curr, end)][1:]
        if curr in visited:
            continue
        visited.add(curr)
        for adj in aoc.adjs(curr):
            if accept(adj) and adj not in p_item.path:
                to_add = aoc.PriorityItem(
                    aoc.mandist(adj, end) + p_item.total_weight,
                    adj,
                    p_item.path + [adj],
                    p_item.total_weight + 1
                )
                if max_depth is None or to_add.priority <= max_depth:
                    heappush(q, to_add)
    return None


TARGET_SAVINGS = 100
MAX_CHEAT = 20


def populate_memo(target, path, memo):
    for i, p in enumerate(path):
        memo[(p, target)] = path[i:]


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
    cheatless_path = find_path(start, end, lambda a: a not in walls and aoc.inbounds2(a[0], a[1], h, w), {})
    cheatless_dist = len(cheatless_path) - 1
    counts = defaultdict(int)
    memo = {}
    for start_dist, left_p in enumerate(cheatless_path):
        if cheatless_dist - start_dist < TARGET_SAVINGS:
            break
        print(start_dist, '/', len(cheatless_path))
        for end_dist, right_p in enumerate(cheatless_path[::-1]):
            potential = cheatless_dist - start_dist - end_dist
            if potential < TARGET_SAVINGS:
                break
            cheat_path = find_path(left_p, right_p, lambda a: a == right_p or aoc.inbounds2(a[0], a[1], h, w), memo, MAX_CHEAT)
            if cheat_path is not None:
                populate_memo(right_p, cheat_path, memo)
                savings = potential - len(cheat_path) + 1
                if len(cheat_path) - 1 <= MAX_CHEAT and savings >= TARGET_SAVINGS:
                    counts[savings] += 1
                    # if savings == 50:
                    #     print()
                    #     print(len(cheat_path), start_dist, end_dist, left_p, right_p)
                    #     for i, row in enumerate(inp):
                    #         for j, c in enumerate(row):
                    #             if (i, j) in cheatless_path[:start_dist + 1] + cheatless_path[::-1][:end_dist + 1]:
                    #                 print('O', end='')
                    #             elif (i, j) in cheat_path:
                    #                 print(8, end='')
                    #             else:
                    #                 print(c, end='')
                    #         print()
    #print(sorted(counts.items()))
    return sum(counts.values())


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=20, year=2024))
    print(solve(inp))
