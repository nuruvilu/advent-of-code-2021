import math
import operator
import json

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def in_order(left, right):
    if isinstance(left, list) and isinstance(right, list):
        if not left and not right:
            return 2
        elif not right:
            return False
        for leftp, rightp in zip(left, right):
            if not leftp and not rightp:
                continue
            last_seen = in_order(leftp, rightp)
            if not last_seen:
                return False
            elif last_seen == 2:
                continue
            else:
                return True
        if len(right) < len(left):
            return False
        return 2 if len(right) == len(left) else True
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left == right:
            return 2
        else:
            return False
    elif isinstance(left, int):
        return in_order([left], right)
    else:
        return in_order(left, [right])


def solve(inp):
    s = 0
    for i, (leftstr, rightstr) in enumerate(inp, start=1):
        left, right = json.loads(leftstr), json.loads(rightstr)
        if in_order(left, right):
            print(left, '\n', right, '\n')
            s += i
    #print(sum(i for i, _ in enumerate(inp)))
    return s


if __name__ == '__main__':
    inp = aoc.readstanzas('input.txt')
    print(solve(inp))
