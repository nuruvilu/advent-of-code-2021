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


def put_page(new_pages, page, hold, hold_flipped, encountered):
    new_pages.append(page)
    encountered.add(page)
    for held in hold[page]:
        hold_flipped[held].remove(page)
        if not hold_flipped[held]:
            put_page(new_pages, held, hold, hold_flipped, encountered)


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
        new_pages = []
        hold = defaultdict(set)
        hold_flipped = defaultdict(set)
        was_borked = False
        for page in pages:
            x = rules_dict[page].intersection(pages)
            if page in rules_dict and x and not encountered.issuperset(x):
                #print(page, update, rules_dict[page], x, encountered)
                was_borked = True
                for xp in x.difference(encountered):
                    hold[xp].add(page)
                    hold_flipped[page].add(xp)
                #print(hold, hold_flipped)
            else:
                put_page(new_pages, page, hold, hold_flipped, encountered)
        if was_borked:
            s += int(new_pages[len(new_pages) // 2])
            #print(s, new_pages)
    return s


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=5, year=2024))
    print(solve(inp))
