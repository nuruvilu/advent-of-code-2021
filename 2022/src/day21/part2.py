import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


def solve(inp):
    monkeys_static = {}
    for line in inp:
        name, op = line.split(': ')
        if op.isdecimal():
            monkeys_static[name] = int(op)
        else:
            left, op, right = op.split()
            monkeys_static[name] = (op, left, right)
    n_str = '1'
    curr = -1
    while True:
        n = int(n_str)
        print(n)
        monkeys = monkeys_static.copy()
        monkeys['humn'] = n
        not_yet_evaled = set(
            name for name, val in monkeys.items() if isinstance(val, tuple))
        while not_yet_evaled:
            marked = set()
            for monkey in not_yet_evaled:
                op, left, right = monkeys[monkey]
                if left not in not_yet_evaled and right not in not_yet_evaled:
                    if monkey == 'root' and int(monkeys[left]) == int(monkeys[right]):
                        return monkeys['humn']
                    elif monkey == 'root':
                        print(monkeys[left], monkeys[right])
                        if curr == -1 and monkeys[left] > monkeys[right]:
                            n_str += '0'
                        elif curr == -1:
                            n_str = n_str[:-1]
                            curr = 0
                        elif monkeys[left] > monkeys[right]:
                            chars = list(n_str)
                            if chars[curr] == '9':
                                curr += 1
                            else:
                                chars[curr] = str(int(chars[curr]) + 1)
                            n_str = ''.join(chars)
                        else:
                            chars = list(n_str)
                            chars[curr] = str(int(chars[curr]) - 1)
                            n_str = ''.join(chars)
                            curr += 1
                        not_yet_evaled = set()
                    if op == '+':
                        val = monkeys[left] + monkeys[right]
                    if op == '-':
                        val = monkeys[left] - monkeys[right]
                    if op == '*':
                        val = monkeys[left] * monkeys[right]
                    if op == '/':
                        val = monkeys[left] / monkeys[right]
                    monkeys[monkey] = val
                    marked.add(monkey)
            not_yet_evaled -= marked


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
