from functools import reduce
from operator import mul


ON = 1
OFF = -1


def intersect(c1, c2):
    intersection = []
    for i in range(3):
        if c1[2 * i] > c2[2 * i + 1] or c1[2 * i + 1] < c2[2 * i]:
            return False
        intersection.append(max(c1[2 * i], c2[2 * i]))
        intersection.append(min(c1[2 * i + 1], c2[2 * i + 1]))
    return intersection


def volume(c):
    return reduce(mul, (c[2 * i + 1] - c[2 * i] + 1 for i in range(3)), 1)


def solve(input_list: list):
    steps = []
    for line in input_list:
        groups = line.split(' ')[1].split(',')
        t = ON if line[1] == 'n' else OFF
        groups = [group.split('=')[1].split('..') for group in groups]
        steps.append((t, [[int(n) for n in g] for g in groups]))
    cubes = []
    for (t, ((minx, maxx), (miny, maxy), (minz, maxz))) in steps:
        curr = [minx, maxx, miny, maxy, minz, maxz]
        cubes.extend([(intersect(cube, curr), -state)
                      for cube, state in cubes if intersect(cube, curr)])
        if t == ON:
            cubes.append((curr, t))
    return sum(volume(cube) * state for cube, state in cubes)


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
