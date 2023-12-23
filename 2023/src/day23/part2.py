import math
import operator

import sys
sys.path.append('..')

from collections import deque
from dataclasses import dataclass, field
from heapq import heappush, heappushpop
from functools import reduce, lru_cache
from pathlib import Path

import common as aoc
from aocd import get_data


@dataclass(order=True)
class Fork:
    steps: int
    pos: (int, int)=field(compare=False)
    seen: {(int, int)}=field(compare=False)


def solve(inp):
    start = None
    stop = None
    for j, item in enumerate(inp[0]):
        if item == '.':
            start = (0, j)
    for j, item in enumerate(inp[-1]):
        if item == '.':
            stop = (len(inp) - 1, j)

    forks = [Fork(0, start, set())]
    #passed_over = []
    cache = {}
    pots = []
    MAX_FORKS = 5000
    while forks:
        print(forks[-1].steps)
        #print([len(s) for p, s in forks])
        new_forks = []
        for fork in forks:
            #print(len(seen))
            if fork.pos == stop:
                #print([x for x, _ in forks])
                pots.append(len(seen))
            nexts = [fork]
            while len(nexts) == 1:
                cfork = nexts.pop()
                for (i, j) in aoc.adjs(cfork.pos):
                    if (i, j) == stop:
                        pots.append(len(cfork.seen) + 1)
                    if aoc.inbounds2(i, j, len(inp), len(inp[0])) and inp[i][j] != '#' and (i, j) not in cfork.seen:
                        nexts.append(Fork(cfork.steps + 1, (i, j), cfork.seen | {cfork.pos}))
            for nfork in nexts:
                if len(new_forks) < MAX_FORKS:
                    heappush(new_forks, nfork)
                else:
                    heappushpop(new_forks, nfork)
        forks = new_forks
    print(pots)
    return max(pots)


if __name__ == '__main__':
    #inp = aoc.readgrid(Path('sample.txt'))
    inp = aoc.readgrid(get_data(day=23, year=2023))
    print(solve(inp))
