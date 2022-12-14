import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    max_y = -1
    blocked_vs = set()
    for row in inp:
        for left, right in aoc.window(row.split(' -> '), 2):
            leftx, lefty = [int(x) for x in left.split(',')]
            rightx, righty = [int(x) for x in right.split(',')]
            max_y = max(max_y, lefty, righty)
            if leftx == rightx:
                start = min(lefty, righty)
                end = max(lefty, righty)
                for y in range(start, end + 1):
                    blocked_vs.add((leftx, y))
            else:
                start = min(leftx, rightx)
                end = max(leftx, rightx)
                for x in range(start, end + 1):
                    blocked_vs.add((x, lefty))
    curr_x, curr_y = (500, 0)
    sand_added = 1
    floor = max_y + 2
    while (500, 0) not in blocked_vs:
        if curr_y + 1 >= floor:
            blocked_vs.add((curr_x, curr_y))
            curr_x, curr_y = (500, 0)
            sand_added += 1
        elif (curr_x, curr_y + 1) not in blocked_vs:
            curr_y += 1
        elif (curr_x - 1, curr_y + 1) not in blocked_vs:
            curr_x -= 1
            curr_y += 1
        elif (curr_x + 1, curr_y + 1) not in blocked_vs:
            curr_x += 1
            curr_y += 1
        else:
            blocked_vs.add((curr_x, curr_y))
            curr_x, curr_y = (500, 0)
            sand_added += 1
    return sand_added - 1


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
