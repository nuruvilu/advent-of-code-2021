import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    monkeys = {}
    for line in inp:
        name, op = line.split(': ')
        if op.isdecimal():
            monkeys[name] = int(op)
        else:
            left, op, right = op.split()
            monkeys[name] = (op, left, right)
    not_yet_evaled = set(name for name, val in monkeys.items() if isinstance(val, tuple))
    while not_yet_evaled:
        marked = set()
        for monkey in not_yet_evaled:
            op, left, right = monkeys[monkey]
            if left not in not_yet_evaled and right not in not_yet_evaled:
                if op == '+':
                    val = monkeys[left] + monkeys[right]
                if op == '-':
                    val = monkeys[left] - monkeys[right]
                if op == '*':
                    val = monkeys[left] * monkeys[right]
                if op == '/':
                    val = monkeys[left] / monkeys[right]
                if monkey == 'root':
                    return val
                monkeys[monkey] = val
                marked.add(monkey)
        not_yet_evaled -= marked


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
