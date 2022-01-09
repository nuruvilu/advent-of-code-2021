
from functools import reduce


def flatMap(array):
    return reduce(list.__add__, array)


def parse_line(line):
    ends = line.split('->')
    ends = [[int(n) for n in e.strip().split(',')] for e in ends]
    if ends[0][0] == ends[1][0]:
        lower = min(ends[0][1], ends[1][1])
        upper = max(ends[0][1], ends[1][1])
        return [(ends[0][0], i) for i in range(lower, upper + 1)]
    elif ends[0][1] == ends[1][1]:
        lower = min(ends[0][0], ends[1][0])
        upper = max(ends[0][0], ends[1][0])
        return [(i, ends[0][1]) for i in range(lower, upper + 1)]


def solve(input_list: list):
    lines = [parse_line(line) for line in input_list]
    s = 0
    flatlines = flatMap(l for l in lines if l is not None)
    sofar = set()
    sofar2 = set()
    for point in flatlines:
        if point in sofar2:
            continue
        if point in sofar:
            sofar2.add(point)
            s += 1
        else:
            sofar.add(point)
    return s


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    # input_list = f.read().split('\n\n')  # for line broken input
    print(solve(input_list))
