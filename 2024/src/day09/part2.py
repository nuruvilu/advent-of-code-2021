import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


TFILE, TFREE = 0, 1


def solve(inp):
    disk = []
    is_file = True
    file_n = 0
    for x in inp:
        if is_file:
            disk.append((TFILE, int(x), file_n))
            file_n += 1
        else:
            disk.append((TFREE, int(x), 0))
        is_file = not is_file
    i = len(disk) - 1
    while i > 0:
        j = 0
        while j < i:
            t, size, _ = disk[j]
            if t == TFREE and size >= disk[i][1]:
                disk[j] = (TFREE, size - disk[i][1], 0)
                disk.insert(j, disk[i])
                disk[i + 1] = (TFREE, disk[i + 1][1], 0)
                break
            j += 1
        i -= 1
        while disk[i][0] == TFREE:
            i -= 1
    print(''.join((f'{id_}' if t == TFILE else '.') * size for t, size, id_ in disk))
    return sum(i * n for i, n in enumerate(aoc.flatten([id_] * size for _, size, id_ in disk)))


if __name__ == '__main__':
    #inp = aoc.read(Path('sample.txt'))
    inp = aoc.read(get_data(day=9, year=2024))
    print(solve(inp))
