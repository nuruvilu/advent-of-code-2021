import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def apply_op(op, old):
    left, oprtr, right = op
    if left == 'old':
        left = old
    if right == 'old':
        right = old
    if oprtr == '*':
        return left * right
    elif oprtr == '+':
        return left + right
    else:
        raise ValueError(f'Bad operator! {oprtr}')


def solve(inp):
    monkeys = []
    monkey_throws = []
    for raw_monkey in inp:
        worrys = [int(n) for n in raw_monkey[1].split(': ')[1].split(', ')]
        op = raw_monkey[2].split('= ')[1].split()
        op = tuple(int(x) if x.isdecimal() else x for x in op)
        test = int(raw_monkey[3].split()[-1])
        if_true = int(raw_monkey[4].split()[-1])
        if_false = int(raw_monkey[5].split()[-1])
        monkeys.append((worrys, op, test, if_true, if_false))
        monkey_throws.append(0)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            while monkey[0]:
                item = monkey[0].pop(0)
                new_worry = apply_op(monkey[1], item)
                new_worry //= 3
                if new_worry % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(new_worry)
                else:
                    monkeys[monkey[4]][0].append(new_worry)
                monkey_throws[i] += 1
    print(monkey_throws)
    return reduce(operator.mul, sorted(monkey_throws, reverse=True)[:2])


if __name__ == '__main__':
    inp = aoc.readstanzas('input.txt')
    print(solve(inp))
