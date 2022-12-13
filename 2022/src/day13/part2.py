import math
import operator
import json

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce, cmp_to_key

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


def cmp(left, right):
    x = in_order(left, right)
    if x == 2:
        return 0
    elif x:
        return -1
    else:
        return 1


def solve(inp):
    s = 1
    stuff = [json.loads(x) for x in inp if x]
    stuff.append([[2]])
    stuff.append([[6]])
    new_stuff = sorted(stuff, key=cmp_to_key(cmp))
    for i, thing in enumerate(new_stuff, start=1):
        if json.dumps(thing) in ('[[2]]', '[[6]]'):
            s *= i
    #print('\n'.join(str(x) for x in new_stuff))
    return s


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
