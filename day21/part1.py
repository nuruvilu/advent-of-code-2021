import math
from functools import lru_cache


@lru_cache()
def ahh(n):
    while n > 10:
        n -= 10
    return n


def next_die(n):
    x = n
    while True:
        if x < 100:
            x += 1
        else:
            x = 1
        print(x)
        yield x


def solve(input_list: list):
    ps = [7, 2]
    p = [0, 0]
    dice = next_die(0)
    turn = 0
    rolls = 0
    while p[0] < 1000 and p[1] < 1000:
        roll = sum(next(dice) for _ in range(3))
        print(roll)
        newspot = ps[turn] + roll
        ps[turn] = ahh(newspot)
        print(ps)
        p[turn] += ps[turn]
        print(p)
        turn = 0 if turn else 1
        rolls += 3
    print(p)
    return min(p) * rolls


with open('input.txt', 'r') as f:
    #input_list = [s for s in f.read().strip().split('\n')]
    print(solve(None))
