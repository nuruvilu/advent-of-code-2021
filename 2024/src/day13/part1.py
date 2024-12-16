import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


MAX_PRESSES = 100


def v_add(p1, p2):
    return tuple(i1 + i2 for i1, i2 in zip(p1, p2))


def solve(inp):
    prize_cost = 0
    for button_a, button_b, prize in inp:
        button_a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', button_a)
        button_b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', button_b)
        prize = re.match(r'Prize: X=(\d+), Y=(\d+)', prize)
        button_a = tuple(int(n) for n in button_a.groups())
        button_b = tuple(int(n) for n in button_b.groups())
        prize = tuple(int(n) for n in prize.groups())
        #print(button_a, button_b, prize)
        def step(curr_item):
            curr, (a_presses, b_presses) = curr_item.item
            nexts = []
            new_item = v_add(curr, button_a)
            if new_item[0] <= prize[0] and new_item[1] <= prize[1] and a_presses < 100:
                nexts.append((3, (new_item, (a_presses + 1, b_presses))))
            new_item = v_add(curr, button_b)
            if new_item[0] <= prize[0] and new_item[1] <= prize[1] and b_presses < 100:
                nexts.append((1, (new_item, (a_presses, b_presses + 1))))
            return nexts
        def is_target(curr_item):
            return curr_item.item[0] == prize
        def h(curr):
            return aoc.mandist(curr[0], prize)
        try:
            prize_cost += aoc.astar(((0, 0), (0, 0)), step, h, is_target).total_weight
        except RuntimeError as e:
            print(e)
    return prize_cost


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=13, year=2024))
    print(solve(inp))
