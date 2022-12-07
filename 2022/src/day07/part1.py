import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc

s = 0
def sum_sizes(tree):
    if isinstance(tree, int):
        return tree
    else:
        global s
        s2 = 0
        for t in tree.values():
            s2 += sum_sizes(t)
        if s2 <= 100_000:
            #print('yes', tree, s, s2)
            s += s2
        else:
            #print('no', tree)
            pass
        return s2


def solve(inp):
    dir_tree = {}
    curr = dir_tree
    parents = []
    for line in inp[1:]:
        head, tail = line.split(' ', maxsplit=1)
        if head == '$':
            if ' ' in tail:
                _cmd, dst = tail.split()
                if dst == '..':
                    curr = dir_tree
                    parents.pop()
                    for parent in parents:
                        curr = curr[parent]
                else:
                    parents.append(dst)
                    curr[dst] = {}
                    curr = curr[dst]
        elif head == 'dir':
            pass
        else:
            curr[tail] = int(head)
    print(dir_tree)
    sum_sizes(dir_tree)
    return s


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
