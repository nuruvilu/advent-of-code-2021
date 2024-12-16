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
    rules, updates = inp
    rules_dict = defaultdict(set)
    for rule in rules:
        l, r = rule.split('|')
        rules_dict[r].add(l)
    s = 0
    for update in updates:
        pages = update.split(',')
        encountered = set()
        for page in pages:
            x = rules_dict[page].intersection(pages)
            if page in rules_dict and x and not encountered.issuperset(x):
                # print(page, update, rules_dict[page], x, encountered)
                break
            encountered.add(page)
        else:
            s += int(pages[len(pages) // 2])
            # print(s)
    return s


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=5, year=2024))
    print(solve(inp))
