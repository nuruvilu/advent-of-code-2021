import math
import operator
import json

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce

import common as aoc


dirs = []
def sum_sizes(tree):
    if isinstance(tree, int):
        return tree
    else:
        s2 = 0
        for t in tree.values():
            s2 += sum_sizes(t)
        dirs.append(s2)
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
    #print(json.dumps(dir_tree, indent=2))
    print(sum_sizes(dir_tree))
    total = max(dirs)
    space_free = 70_000_000 - total
    target = 30_000_000 - space_free
    print(total, target)
    #print(sorted(dirs))
    return min([d for d in dirs if d >= target])


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
