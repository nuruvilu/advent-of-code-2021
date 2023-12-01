import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data, submit

nums = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

def solve(inp):
    n = 0
    for line in inp:
        zz = {}
        for num in nums:
            x = line.find(num)
            if x != -1:
                zz[x] = num
            x = line.rfind(num)
            if x != -1:
                zz[x] = num
        z = ''
        for i, ch in enumerate(line):
            if i in zz:
                d = nums.index(zz[i]) + 1
                print(d, zz[i], i)
                if not z:
                    z = str(d) + str(d)
                else:
                    z = z[0] + str(d)
            if ch.isdigit():
                if not z:
                    z = ch + ch
                else:
                    z = z[0] + ch
        print(zz, z, line)
        n += int(z)
    return n


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=1, year=2023))
    answer = solve(inp)
    print(answer)
    #submit(answer)
