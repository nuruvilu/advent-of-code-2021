import math
from functools import lru_cache
from collections import defaultdict
from itertools import product


def ahh(n):
    x = n % 10
    return x if x else 10


def solve(input_list: list):
    p = defaultdict(int)
    p[(7, 2, 0, 0)] = 1
    turn = 0
    p1w, p2w = 0, 0
    while p:
        #print(len(p))
        newp = defaultdict(int)
        for (p1p, p2p, p1s, p2s), c in p.items():
            newu = product([1, 2, 3], [1, 2, 3], [1, 2, 3])
            for uni in newu:
                if not turn:
                    p1p2 = ahh(p1p + sum(uni))
                    if p1s + p1p2 >= 21:
                        p1w += c
                    else:
                        newp[(p1p2, p2p, p1s + p1p2, p2s)] += c
                else:
                    p2p2 = ahh(p2p + sum(uni))
                    if p2s + p2p2 >= 21:
                        p2w += c
                    else:
                        newp[(p1p, p2p2, p1s, p2s + p2p2)] += c
        turn = 0 if turn else 1
        p = newp
    return max(p1w, p2w)


with open('input.txt', 'r') as f:
    #input_list = [s for s in f.read().strip().split('\n')]
    print(solve(None))
