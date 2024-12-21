import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
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


def goes_over_blank(start, moves, keypad_pivot):
    pos = start
    for move in moves:
        pos = aoc.udlr_xy(ARROWS_TO_LETTERS[move], pos)
        if pos not in keypad_pivot:
            return True
    return False


def find_possible_moves(code, keypad, keypad_pivot):
    options = ['']
    pos = keypad['A']
    for button in code:
        dx = pos[0] - keypad[button][0]
        dy = pos[1] - keypad[button][1]
        xc = ('<' if dx > 0 else '>') * abs(dx)
        yc = ('^' if dy > 0 else 'v') * abs(dy)
        new_options = []
        for permutation in set(permutations(xc + yc)):
            if not goes_over_blank(pos, permutation, keypad_pivot):
                for option in options:
                    new_options.append(option + ''.join(permutation) + 'A')
        options = new_options
        pos = keypad[button]
        #print(options, dx, dy, xc, yc, button)
    return options


def solve(inp):
    score = 0
    for i, code in enumerate(inp):
        print('\n', i)
        numbers = int(code[:-1])
        options = find_possible_moves(code, NUMERIC_KEYPAD, NUMERIC_PIVOT)
        for _ in range(2):
            possibles = [find_possible_moves(option, DIRECTIONAL_KEYPAD, DIRECTIONAL_PIVOT) for option in options]
            lowest = min(len(p[0]) for p in possibles)
            new_options = []
            for j, possible in enumerate(possibles):
                if len(possible[0]) <= lowest:
                    new_options += possible
            options = new_options
        print(lowest)
        score += numbers * lowest
    return score


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=21, year=2024))
    print(solve(inp))
