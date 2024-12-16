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


def solve(inp):
    grid, moves = inp.split('\n\n')
    grid = aoc.readgrid(grid)
    moves = ''.join(moves.split('\n'))
    robo_pos = None
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '@':
                robo_pos = (i, j)
    for move in moves:
        d = MOVES[move]
        ii, jj = ip, jp = aoc.udlr_ij(d, robo_pos)
        hit = []
        while grid[ip][jp] == 'O':
            hit.append((ip, jp))
            ip, jp = aoc.udlr_ij(d, (ip, jp))
        if grid[ip][jp] == '.':
            grid[ip][jp] = 'O'
            for ih, jh in hit:
                grid[ih][jh] = 'O'
            grid[ii][jj] = '@'
            grid[robo_pos[0]][robo_pos[1]] = '.'
            robo_pos = ii, jj
        #print(d)
        #print('\n'.join(''.join(row) for row in grid))
    s = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 'O':
                s += 100*i + j
    return s
            

if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=15, year=2024))
    print(solve(inp))
