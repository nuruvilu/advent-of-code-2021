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


PRIZE_OFFSET = 10000000000000


def v_add(p1, p2):
    return tuple(i1 + i2 for i1, i2 in zip(p1, p2))


def v_mul(s, p):
    return tuple(s * n for n in p)


def solve(inp):
    prize_cost = 0
    for button_a, button_b, prize in inp:
        button_a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', button_a)
        button_b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', button_b)
        prize = re.match(r'Prize: X=(\d+), Y=(\d+)', prize)
        a = a_x, a_y = tuple(int(n) for n in button_a.groups())
        b = b_x, b_y = tuple(int(n) for n in button_b.groups())
        prize = prize_x, prize_y = tuple(int(n) + PRIZE_OFFSET for n in prize.groups())
        #print(button_a, button_b, prize)
        b_presses = (a_y*prize_x - a_x*prize_y) // (a_y*b_x - a_x*b_y)
        a_presses = (prize_x - b_presses*b_x) // a_x
        if prize == v_add(v_mul(a_presses, a), v_mul(b_presses, b)):
            prize_cost += 3*a_presses + b_presses
    return prize_cost


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=13, year=2024))
    print(solve(inp))
