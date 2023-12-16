import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    entrypoints = [((0, i), 'R') for i in range(len(inp))]
    entrypoints += [((len(inp[0]) - 1, i), 'L') for i in range(len(inp))]
    entrypoints += [((i, len(inp) - 1), 'D') for i in range(len(inp[0]))]
    entrypoints += [((i, 0), 'U') for i in range(len(inp[0]))]
    maxeng = 0
    for i, entrypoint in enumerate(entrypoints):
        print(i / len(entrypoints))
        beams = [entrypoint]
        energized = set()
        visited = set()
        while beams:
            (curr_x, curr_y), curr_dir = beams.pop(0)
            while aoc.inbounds2(curr_y, curr_x, len(inp), len(inp[0])):
                if ((curr_x, curr_y), curr_dir) in visited:
                    break
                visited.add(((curr_x, curr_y), curr_dir))
                energized.add((curr_x, curr_y))
                if inp[curr_y][curr_x] == '/':
                    if curr_dir == 'U': curr_dir = 'L'
                    elif curr_dir == 'L': curr_dir = 'U'
                    elif curr_dir == 'D': curr_dir = 'R'
                    elif curr_dir == 'R': curr_dir = 'D'
                elif inp[curr_y][curr_x] == '\\':
                    if curr_dir == 'U': curr_dir = 'R'
                    elif curr_dir == 'R': curr_dir = 'U'
                    elif curr_dir == 'D': curr_dir = 'L'
                    elif curr_dir == 'L': curr_dir = 'D'
                elif inp[curr_y][curr_x] == '-':
                    if curr_dir in ('U', 'D'):
                        curr_dir = 'L'
                        other = 'R'
                        other_pos = aoc.udlr_xy(other, (curr_x, curr_y))
                        beams.append((other_pos, other))
                elif inp[curr_y][curr_x] == '|':
                    if curr_dir in ('L', 'R'):
                        curr_dir = 'U'
                        other = 'D'
                        other_pos = aoc.udlr_xy(other, (curr_x, curr_y))
                        beams.append((other_pos, other))
                curr_x, curr_y = aoc.udlr_xy(curr_dir, (curr_x, curr_y))
        maxeng = max(maxeng, len(energized))
    return maxeng


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=16, year=2023))
    print(solve(inp))
