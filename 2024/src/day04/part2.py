import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path
from collections import defaultdict

import common as aoc
from aocd import get_data


def solve(inp):
    count = 0
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            if c == 'A' and 0 < i < len(inp) - 1 and 0 < j < len(inp[0]) - 1:
                if inp[i - 1][j - 1] == 'M' and inp[i - 1][j + 1] == 'M' and inp[i + 1][j - 1] == 'S' and inp[i + 1][j + 1] == 'S':
                    count += 1
                elif inp[i - 1][j - 1] == 'M' and inp[i - 1][j + 1] == 'S' and inp[i + 1][j - 1] == 'M' and inp[i + 1][j + 1] == 'S':
                    count += 1
                elif inp[i - 1][j - 1] == 'S' and inp[i - 1][j + 1] == 'S' and inp[i + 1][j - 1] == 'M' and inp[i + 1][j + 1] == 'M':
                    count += 1
                elif inp[i - 1][j - 1] == 'S' and inp[i - 1][j + 1] == 'M' and inp[i + 1][j - 1] == 'S' and inp[i + 1][j + 1] == 'M':
                    count += 1
    return count


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=4, year=2024))
    print(solve(inp))
