import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc
import re


stacks = [
    ['L', 'C', 'G', 'M', 'Q'],
    ['G', 'H', 'F', 'T', 'C', 'L', 'D', 'R'],
    ['R', 'W', 'T', 'M', 'N', 'F', 'J', 'V'],
    ['P', 'Q', 'V', 'D', 'F', 'J'],
    ['T', 'B', 'L', 'S', 'M', 'F', 'N'],
    ['P', 'D', 'C', 'H', 'V', 'N', 'R'],
    ['T', 'C', 'H'],
    ['P', 'H', 'N', 'Z', 'V', 'J', 'S', 'G'],
    ['G', 'H', 'F', 'Z']
]

# stacks = [
#     ['N', 'Z'],
#     ['D', 'C', 'M'],
#     ['P']
# ]


def solve(inp):
    for stack in stacks:
        stack.reverse()
    for line in inp:
        line = line[5:]
        #print(re.split(r'(\sfrom\s|\sto\s)', line))
        cnt, _, src, _, dst = re.split(r'(\sfrom\s|\sto\s)', line)
        source = stacks[int(src) - 1]
        for e in source[len(source) - int(cnt):]:
            source.pop()
            stacks[int(dst) - 1].append(e)
    return ''.join([s[-1] for s in stacks])


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
