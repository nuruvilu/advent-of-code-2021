from functools import reduce
import operator
import copy

cave_map = {}


def explore(cave, past):
    if cave not in past:
        past2 = copy.deepcopy(past)
        if cave.islower():
            past2.add(cave)
        total = 0
        for c2 in cave_map[cave]:
            if c2 == 'end':
                total += 1
            elif c2 != 'start':
                total += explore(c2, past2)
        return total
    return 0


def solve(input_list: list):
    for inp in input_list:
        p1, p2 = inp.split('-')
        if p1 in cave_map:
            cave_map[p1].append(p2)
        else:
            cave_map[p1] = [p2]
        if p2 in cave_map:
            cave_map[p2].append(p1)
        else:
            cave_map[p2] = [p1]
    return reduce(operator.add, [explore(c, set()) for c in cave_map['start']])


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
