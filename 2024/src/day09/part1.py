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
    files, free_spaces = [], []
    is_file = True
    for x in inp:
        if is_file:
            files.append(int(x))
        else:
            free_spaces.append(int(x))
        is_file = not is_file
    left_p, right_p, i = 0, len(files) - 1, 0
    checksum = 0
    free_p = 0
    while right_p > left_p:
        j = i
        while i < j + files[left_p]:
            print(left_p, end='')
            checksum += i * left_p
            i += 1
        left_p += 1
        j = i
        while i < j + free_spaces[free_p]:
            print(right_p, end='')
            checksum += i * right_p
            files[right_p] -= 1
            if files[right_p] <= 0:
                right_p -= 1
            i += 1
        free_p += 1
    while files[right_p]:
        checksum += i * right_p
        i += 1
        files[right_p] -= 1
    print()
    return checksum


if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=9, year=2024))
    print(solve(inp))
