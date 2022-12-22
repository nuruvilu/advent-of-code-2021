import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict

import common as aoc


NOPE = 0
WALL = 1
OPEN = 2


compass = 'RDLU'


def udlr(facing, pos):
    if facing == 'U':
        facing = 'D'
    elif facing == 'D':
        facing = 'U'
    return aoc.udlr_xy(facing, pos)


def solve(inp):
    board_raw, path = inp
    row_bounds = defaultdict(lambda: (999999, 0))
    col_bounds = defaultdict(lambda: (999999, 0))
    board = defaultdict(int)
    for y, row in enumerate(board_raw):
        for x, val in enumerate(row):
            if val == ' ':
                continue
            x, y = int(x), int(y)
            board[(x, y)] = WALL if val == '#' else OPEN
            min_x = min(x, row_bounds[y][0])
            max_x = max(x, row_bounds[y][1])
            min_y = min(y, col_bounds[x][0])
            max_y = max(y, col_bounds[x][1])
            row_bounds[y] = (min_x, max_x)
            col_bounds[x] = (min_y, max_y)
    facing = 'R'
    pos = (row_bounds[0][0], 0)
    path = re.split(r'([LR])', path[0])
    for step in path:
        if step.isdecimal():
            steps = int(step)
            for _ in range(steps):
                print(pos)
                nxt = udlr(facing, pos)
                if board[nxt] == WALL:
                    break
                elif board[nxt] == NOPE:
                    # print('NOPE', pos, nxt)
                    if facing == 'L':
                        nxt = (row_bounds[pos[1]][1], pos[1])
                    elif facing == 'R':
                        nxt = (row_bounds[pos[1]][0], pos[1])
                    elif facing == 'D':
                        nxt = (pos[0], col_bounds[pos[0]][0])
                    elif facing == 'U':
                        nxt = (pos[0], col_bounds[pos[0]][1])
                    if board[nxt] == WALL:
                        break
                pos = nxt
        else:
            mod = 1 if step == 'R' else -1
            curr = compass.index(facing)
            facing = compass[(curr + mod) % 4]
            # print(facing)
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + compass.index(facing)


if __name__ == '__main__':
    inp = aoc.readstanzas('input.txt')
    print(solve(inp))
