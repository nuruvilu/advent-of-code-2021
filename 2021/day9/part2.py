from functools import reduce
import operator


def is_low_point(i, j, row, n, map_):
    could = True if n < 9 else False
    if i != 0 and map_[i - 1][j] <= n:
        could = False
    if i != len(map_) - 1 and map_[i + 1][j] <= n:
        could = False
    if j != 0 and map_[i][j - 1] <= n:
        could = False
    if j != (len(row)) - 1 and map_[i][j + 1] <= n:
        could = False
    return could


def oob(i, j, row, map_):
    return i < 0 or j < 0 or i >= len(map_) or j >= len(row)


def get_basin(i1, j1, row, n, map_):
    good = {(i1, j1)}
    passed = {(i1, j1)}
    waiting = [(i1, j1)]
    while waiting:
        (i, j), waiting = waiting[0], waiting[1:]
        if not oob(i, j, row, map_) and map_[i][j] != 9:
            for t in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if t not in passed:
                    waiting.append(t)
            good.add((i, j))
        passed.add((i, j))
    return len(good)


def solve(input_list: list):
    map_ = [[int(n) for n in line] for line in input_list]
    s = []
    for i, row in enumerate(map_):
        for j, n in enumerate(row):
            if is_low_point(i, j, row, n, map_):
                x = get_basin(i, j, row, n, map_)
                if len(s) < 3:
                    s.append(x)
                elif min(s) < x:
                    s[s.index(min(s))] = x
    return reduce(operator.mul, s)


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
