from collections import defaultdict


ON = 0
OFF = 1


def solve(input_list: list):
    steps = []
    for line in input_list:
        groups = line.split(' ')[1].split(',')
        t = ON if line[1] == 'n' else OFF
        #print(groups)
        groups = [group.split('=')[1].split('..') for group in groups]
        #print(groups)
        steps.append((t, [[int(n) for n in g] for g in groups]))
    cubes = defaultdict(int)
    for (t, ((minx, maxx), (miny, maxy), (minz, maxz))) in steps:
        minx = max(-50, minx)
        miny = max(-50, miny)
        minz = max(-50, minz)
        maxx = min(50, maxx)
        maxy = min(50, maxy)
        maxz = min(50, maxz)
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                for z in range(minz, maxz + 1):
                    if t == ON:
                        cubes[(x, y, z)] = 1
                    else:
                        cubes[(x, y, z)] = 0
    return sum(cubes.values())


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
