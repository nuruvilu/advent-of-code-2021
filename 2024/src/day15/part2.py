import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


MOVES = {
    '^': 'U',
    'v': 'D',
    '<': 'L',
    '>': 'R'
}


def get_other(grid, i, j):
    if grid[i][j] == ']':
        return i, j - 1
    return i, j + 1


def solve(inp):
    grid, moves = inp.split('\n\n')
    moves = ''.join(moves.split('\n'))
    grid = aoc.readgrid(grid)
    new_grid = []
    robo_pos = None
    for i, row in enumerate(grid):
        new_row = []
        for j, c in enumerate(row):
            if c == '@':
                new_row += ['@', '.']
                robo_pos = i, j * 2
            elif c == 'O':
                new_row += ['[', ']']
            else:
                new_row += [c, c]
        new_grid.append(new_row)
    grid = new_grid
    for move in moves:
        d = MOVES[move]
        if d in 'LR':
            ii, jj = ip, jp = aoc.udlr_ij(d, robo_pos)
            hit = []
            while grid[ip][jp] in '[]':
                hit.append((ip, jp, grid[ip][jp]))
                ip, jp = aoc.udlr_ij(d, (ip, jp))
            if grid[ip][jp] == '.':
                hit.append((ip, jp, '.'))
                for (_, _, c), (ih, jh, _) in aoc.window(hit, 2):
                    grid[ih][jh] = c
                grid[ii][jj] = '@'
                grid[robo_pos[0]][robo_pos[1]] = '.'
                robo_pos = ii, jj
        else:
            ip, jp = aoc.udlr_ij(d, robo_pos)
            if grid[ip][jp] == '.':
                grid[ip][jp] = '@'
                grid[robo_pos[0]][robo_pos[1]] = '.'
                robo_pos = ip, jp
            elif grid[ip][jp] in '[]':
                push = []
                q = [(ip, jp), get_other(grid, ip, jp)]
                visited = set()
                now_occupied = set()
                while q:
                    ii, jj = q.pop(0)
                    if (ii, jj) in visited:
                        continue
                    visited.add((ii, jj))
                    iii, jjj = aoc.udlr_ij(d, (ii, jj))
                    if grid[iii][jjj] in '[]':
                        o_i, o_j = get_other(grid, iii, jjj)
                        q.append((iii, jjj))
                        q.append((o_i, o_j))
                    elif grid[iii][jjj] == '#':
                        break
                    push.append((iii, jjj, grid[ii][jj], ii, jj))
                    now_occupied.add((iii, jjj))
                else:
                    for iii, jjj, c, ii, jj in push:
                        grid[iii][jjj] = c
                        if (ii, jj) not in now_occupied:
                            grid[ii][jj] = '.'
                    grid[ip][jp] = '@'
                    grid[robo_pos[0]][robo_pos[1]] = '.'
                    robo_pos = ip, jp
        # print(d)
        # print('\n'.join(''.join(row) for row in grid))
    s = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '[':
                s += 100*i + j
    return s


if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=15, year=2024))
    print(solve(inp))
