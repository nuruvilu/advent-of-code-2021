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


PRUNE = 16777216


def mix_and_prune(n, secret):
    return (n ^ secret) % PRUNE


def solve(inp):
    occs = defaultdict(list)
    seen = set()
    for i, secret in enumerate(inp):
        last4 = []
        print(i, '/', len(inp))
        curr = secret
        price = None
        for j in range(2000):
            curr = mix_and_prune(curr << 6, curr)
            curr = mix_and_prune(curr >> 5, curr)
            curr = mix_and_prune(curr << 11, curr)
            new_price = int(str(curr)[-1])
            if price is not None:
                last4.append(new_price - price)
            price = new_price
            if len(last4) == 4:
                l4t = tuple(last4)
                if (l4t, i) not in seen:
                    occs[l4t].append(price)
                    seen.add((l4t, i))
                last4.pop(0)
    return max(map(sum, occs.values()))


if __name__ == '__main__':
    #inp = aoc.readnums(Path('sample.txt'))
    inp = aoc.readnums(get_data(day=22, year=2024))
    print(solve(inp))
