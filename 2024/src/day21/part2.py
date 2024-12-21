import math
import operator

import sys
sys.path.append('..')

from copy import deepcopy
from heapq import heappush, heappop
from functools import reduce, cache
from pathlib import Path
from itertools import permutations

import common as aoc
from aocd import get_data


NUMERIC_KEYPAD = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
                 '0': (1, 3), 'A': (2, 3),
}
NUMERIC_PIVOT = {v: k for k, v in NUMERIC_KEYPAD.items()}
DIRECTIONAL_KEYPAD = {
                 '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1),
}
DIRECTIONAL_PIVOT = {v: k for k, v in DIRECTIONAL_KEYPAD.items()}
ARROWS_TO_LETTERS = {'^': 'U', 'v': 'D', '>': 'R', '<': 'L'}
ITERATIONS = 25


def goes_over_blank(start, moves, keypad_pivot):
    pos = start
    for move in moves:
        pos = aoc.udlr_xy(ARROWS_TO_LETTERS[move], pos)
        if pos not in keypad_pivot:
            return True
    return False


@cache
def get_cost(code, depth):
    keypad = NUMERIC_KEYPAD if depth == 0 else DIRECTIONAL_KEYPAD
    cost = 0
    pos = keypad['A']
    for key in code:
        dx = pos[0] - keypad[key][0]
        dy = pos[1] - keypad[key][1]
        xc = ('<' if dx > 0 else '>') * abs(dx)
        yc = ('^' if dy > 0 else 'v') * abs(dy)
        paths = [xc + yc + 'A']
        if yc and xc:
            paths.append(yc + xc + 'A')
        paths = [p for p in paths if not goes_over_blank(pos, p[:-1], NUMERIC_PIVOT if depth == 0 else DIRECTIONAL_PIVOT)]
        lowest = sys.maxsize
        for path in paths:
            path_cost = get_cost(path, depth + 1) if depth < ITERATIONS else len(path)
            lowest = min(path_cost, lowest)
        pos = keypad[key]
        cost += lowest
    return cost


def solve(inp):
    score = 0
    for i, code in enumerate(inp):
        print('\n', i)
        numbers = int(code[:-1])
        cost = get_cost(code, 0)
        print(cost)
        score += numbers * cost
    return score


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=21, year=2024))
    print(solve(inp))
