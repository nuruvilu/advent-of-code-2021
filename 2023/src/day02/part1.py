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
        print(gid, g)
        gid = int(gid.split()[-1])
        good = True
        for sett in g.split(';'):
            for roll in sett.split(','):
                #print(roll)
                num, color = roll.strip().split()
                print(num, color)
                if color == 'red' and int(num) > 12:
                    good = False
                if color == 'blue' and int(num) > 14:
                    good = False
                if color == 'green' and int(num) > 13:
                    good = False
        if not good:
            print('BAD')
        else:
            idsum += gid
            print('GOOD')
    return idsum


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=2, year=2023))
    answer = solve(inp)
    print(answer)
    #submit(answer)
