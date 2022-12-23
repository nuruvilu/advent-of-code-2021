import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict
from pathlib import Path

import common as aoc


def vis(elves, min_x, max_x, min_y, max_y):
    out = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            out += '#' if (x, y) in elves else '.'
        out += '\n'
    Path('vis.txt').write_text(out)


def solve(inp):
    elves = set()
    min_x = 999999
    min_y = 999999
    max_x = 0
    max_y = 0
    for y, row in enumerate(inp):
        for x, spot in enumerate(row):
            if spot == '#':
                elves.add((x, y))
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)
    for i in range(10):
        print(i)
        propositions = defaultdict(list)
        for elf in elves:
            for adj in aoc.adjsdiags2(elf):
                if adj in elves:
                    break
            else:
                continue
            W, SW, S, SE, E, NE, N, NW = aoc.adjsdiags2(elf)
            choices = [
                ((N, NE, NW), N),
                ((S, SE, SW), S),
                ((W, NW, SW), W),
                ((E, NE, SE), E)
            ]
            for j in range(len(choices)):
                checks, dest = choices[(i + j) % len(choices)]
                for check in checks:
                    if check in elves:
                        break
                else:
                    propositions[dest].append(elf)
                    break
        # print(propositions)
        for dest, sources in propositions.items():
            if len(sources) == 1:
                elves.add(dest)
                elves.remove(sources[0])
                x, y = dest
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)
    empty_count = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in elves:
                empty_count += 1
    vis(elves, min_x, max_x, min_y, max_y)
    return empty_count


if __name__ == '__main__':
    inp = aoc.readgrid('input.txt')
    # print(aoc.adjsdiags2((0, 0)))
    print(solve(inp))
