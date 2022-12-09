import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    grid = [[int(n) for n in row] for row in inp]

    tops = 0
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            curr = 1
            #print(i, j, n)
            for k in range(i - 1, -1, -1):
                if grid[k][j] >= n:
                    #print(i, k)
                    curr *= i - k
                    break
            else:
                curr *= i
           #print(curr)
            for k in range(i + 1, len(grid)):
                if grid[k][j] >= n:
                    #print(i, k)
                    curr *= k - i
                    break
            else:
                curr *= len(grid) - i - 1
            #print(curr)
            for k in range(j - 1, -1, -1):
                if grid[i][k] >= n:
                    #print(i, k)
                    curr *= j - k
                    break
            else:
                curr *= j
            #print(curr)
            for k in range(j + 1, len(row)):
                if grid[i][k] >= n:
                    #print(i, k)
                    curr *= k - j
                    break
            else:
                curr *= len(row) - j - 1
            if curr > tops:
                tops = curr
            #print(curr)
            #print()
    #vis(grid, visible)
    return tops


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
