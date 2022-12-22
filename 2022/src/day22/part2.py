import math
import operator
import re
import string

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict
from pathlib import Path

import common as aoc


NOPE = 0
WALL = 1
OPEN = 2


compass = 'RDLU'
INPUT_FP = 'input.txt'


def paired(facing1, facing2):
    return ((facing1 in 'RU' and facing2 in 'RU')
            or (facing1 in 'DL' and facing2 in 'DL'))


hit = set()


def traverse_edge(facing, pos):
    curr_x, curr_y = pos
    faces = {}
    if INPUT_FP == 'sample.txt':
        faces['top'] = (8, 11, 0, 3)
        faces['front'] = (8, 11, 4, 7)
        faces['left'] = (4, 7, 4, 7)
        faces['back'] = (0, 3, 4, 7)
        faces['bottom'] = (8, 11, 8, 11)
        faces['right'] = (12, 15, 8, 11)
        translations = {
            ('top', 'D'): ('front', 'D'),
            ('top', 'L'): ('left', 'D'),
            ('top', 'U'): ('back', 'D'),
            ('top', 'R'): ('right', 'L'),
            ('front', 'D'): ('bottom', 'D'),
            ('front', 'L'): ('left', 'L'),
            ('front', 'U'): ('top', 'U'),
            ('front', 'R'): ('right', 'D'),
            ('left', 'D'): ('bottom', 'R'),
            ('left', 'L'): ('back', 'L'),
            ('left', 'U'): ('top', 'R'),
            ('left', 'R'): ('front', 'R'),
            ('back', 'D'): ('bottom', 'U'),
            ('back', 'L'): ('right', 'U'),
            ('back', 'U'): ('top', 'D'),
            ('back', 'R'): ('left', 'R'),
            ('bottom', 'D'): ('back', 'U'),
            ('bottom', 'L'): ('left', 'U'),
            ('bottom', 'U'): ('front', 'U'),
            ('bottom', 'R'): ('right', 'R'),
            ('right', 'D'): ('back', 'L'),
            ('right', 'L'): ('bottom', 'L'),
            ('right', 'U'): ('front', 'L'),
            ('right', 'R'): ('top', 'L'),
        }
    else:
        faces['top'] = (50, 99, 0, 49)
        faces['right'] = (100, 149, 0, 49)
        faces['front'] = (50, 99, 50, 99)
        faces['bottom'] = (50, 99, 100, 149)
        faces['left'] = (0, 49, 100, 149)
        faces['back'] = (0, 49, 150, 199)
        translations = {
            ('top', 'D'): ('front', 'D'),
            ('top', 'L'): ('left', 'R'),
            ('top', 'U'): ('back', 'R'),
            ('top', 'R'): ('right', 'R'),
            ('front', 'D'): ('bottom', 'D'),
            ('front', 'L'): ('left', 'D'),
            ('front', 'U'): ('top', 'U'),
            ('front', 'R'): ('right', 'U'),
            ('left', 'D'): ('back', 'D'),
            ('left', 'L'): ('top', 'R'),
            ('left', 'U'): ('front', 'R'),
            ('left', 'R'): ('bottom', 'R'),
            ('back', 'D'): ('right', 'D'),
            ('back', 'L'): ('top', 'D'),
            ('back', 'U'): ('left', 'U'),
            ('back', 'R'): ('bottom', 'U'),
            ('bottom', 'D'): ('back', 'L'),
            ('bottom', 'L'): ('left', 'L'),
            ('bottom', 'U'): ('front', 'U'),
            ('bottom', 'R'): ('right', 'L'),
            ('right', 'D'): ('front', 'L'),
            ('right', 'L'): ('top', 'L'),
            ('right', 'U'): ('back', 'U'),
            ('right', 'R'): ('bottom', 'L'),
        }
    curr_face = None
    abs_pos = None
    for face, (min_x, max_x, min_y, max_y) in faces.items():
        if min_x <= curr_x <= max_x and min_y <= curr_y <= max_y:
            curr_face = face
            abs_pos = (curr_x - min_x, curr_y - min_y)
            break
    else:
        raise ValueError(f'No face found for {pos}!')
    new_face, new_facing = translations[(curr_face, facing)]
    if new_facing == facing:
        if new_facing == 'L':
            nxt = (faces[new_face][1], abs_pos[1] + faces[new_face][2])
        elif new_facing == 'R':
            nxt = (faces[new_face][0], abs_pos[1] + faces[new_face][2])
        elif new_facing == 'D':
            nxt = (abs_pos[0] + faces[new_face][0], faces[new_face][2])
        elif new_facing == 'U':
            nxt = (abs_pos[0] + faces[new_face][0], faces[new_face][3])
    elif abs(compass.index(new_facing) - compass.index(facing)) == 2:
        if new_facing == 'L':
            nxt = (faces[new_face][1], faces[new_face][3] - abs_pos[1])
        elif new_facing == 'R':
            nxt = (faces[new_face][0], faces[new_face][3] - abs_pos[1])
        elif new_facing == 'D':
            nxt = (faces[new_face][1] - abs_pos[0], faces[new_face][2])
        elif new_facing == 'U':
            nxt = (faces[new_face][1] - abs_pos[0], faces[new_face][3])
    elif True:
        if new_facing == 'L':
            nxt = (faces[new_face][1], faces[new_face][2] + abs_pos[0])
        elif new_facing == 'R':
            nxt = (faces[new_face][0], faces[new_face][2] + abs_pos[0])
        elif new_facing == 'D':
            nxt = (faces[new_face][0] + abs_pos[1], faces[new_face][2])
        elif new_facing == 'U':
            nxt = (faces[new_face][0] + abs_pos[1], faces[new_face][3])
    else:
        if new_facing == 'L':
            nxt = (faces[new_face][1], faces[new_face][3] - abs_pos[0])
        elif new_facing == 'R':
            nxt = (faces[new_face][0], faces[new_face][3] - abs_pos[0])
        elif new_facing == 'D':
            nxt = (faces[new_face][1] - abs_pos[1], faces[new_face][2])
        elif new_facing == 'U':
            nxt = (faces[new_face][1] - abs_pos[1], faces[new_face][3])
    if (curr_face, facing) not in hit:
        abs_new = None
        for face, (min_x, max_x, min_y, max_y) in faces.items():
            if min_x <= nxt[0] <= max_x and min_y <= nxt[1] <= max_y:
                abs_new = (nxt[0] - min_x, nxt[1] - min_y)
        print('CURRENT:', curr_face, facing, abs_pos)
        print('NEW:', new_face, new_facing, abs_new)
        hit.add((curr_face, facing))
    return nxt, new_facing


def udlr(facing, pos):
    if facing == 'U':
        facing = 'D'
    elif facing == 'D':
        facing = 'U'
    return aoc.udlr_xy(facing, pos)


def vis(board, chart, pivots):
    out = ''
    for y in range(250):
        for x in range(250):
            curr = board[(x, y)]
            if curr == NOPE:
                out += ' '
            elif curr == WALL:
                if (x, y) in chart or (x, y) in pivots:
                    raise RuntimeError('SOMETHING WRONG')
                out += '#'
            else:
                if (x, y) in pivots:
                    out += pivots[(x, y)]
                elif (x, y) in chart:
                    out += {
                        'R': '>',
                        'L': '<',
                        'D': 'v',
                        'U': '^'
                    }[chart[(x, y)]]
                else:
                    out += '.'
        out += '\n'
    Path('vis.txt').write_text(out)


def solve(inp):
    board_raw, path = inp
    start_x = 8 if INPUT_FP == 'sample.txt' else 50
    board = defaultdict(int)
    for y, row in enumerate(board_raw):
        for x, val in enumerate(row):
            if val == ' ':
                continue
            x, y = int(x), int(y)
            board[(x, y)] = WALL if val == '#' else OPEN
    chart = {}
    pivots = {}
    facing = 'R'
    pos = (start_x, 0)
    path = re.split(r'([LR])', path[0])
    pivot_idx = 0
    taken = 0
    for step in path:
        if step.isdecimal():
            steps = int(step)
            for _ in range(steps):
                taken += 1
                # if taken > 4000:
                #     vis(board, chart, pivots)
                #     return 0
                # print(pos)
                chart[pos] = facing
                nxt = udlr(facing, pos)
                if board[nxt] == WALL:
                    break
                elif board[nxt] == NOPE:
                    nxt, nxt_facing = traverse_edge(facing, pos)
                    if board[nxt] == WALL:
                        break
                    facing = nxt_facing
                    if pivot_idx < len(string.ascii_letters):
                        pivots[nxt] = string.ascii_letters[pivot_idx]
                        pivots[pos] = string.ascii_letters[pivot_idx]
                        pivot_idx += 1
                pos = nxt
        else:
            mod = 1 if step == 'R' else -1
            curr = compass.index(facing)
            facing = compass[(curr + mod) % 4]
            # print(facing)
    vis(board, chart, pivots)
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + compass.index(facing)


if __name__ == '__main__':
    inp = aoc.readstanzas(INPUT_FP)
    print(solve(inp))
