import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    s = 0
    for line in inp:
        left, right = line[:len(line) // 2], line[len(line) // 2:]
        #print(left, right)
        l = set(left)
        for c in right:
            if c in l:
                if c.islower():
                    s += ord(c) - ord('a') + 1
                else:
                    s += ord(c) - ord('A') + 27
                #print(c, s)
                break
    return s


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
