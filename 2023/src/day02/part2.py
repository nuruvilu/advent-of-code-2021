import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import re
import common as aoc
from aocd import get_data, submit


def solve(inp):
    idsum = 0
    for game in inp:
        gid, g = game.split(':')
        red, blue, green = 0, 0, 0
        for sett in g.split(';'):
            for roll in sett.split(','):
                num, color = roll.strip().split()
                print(num, color)
                if color == 'red':
                    red = max(red, int(num))
                if color == 'blue':
                    blue = max(blue, int(num))
                if color == 'green':
                    green = max(green, int(num))
        idsum += red * blue * green
    return idsum


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=2, year=2023))
    answer = solve(inp)
    print(answer)
    #submit(answer)
