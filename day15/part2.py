from queue import PriorityQueue
from math import sqrt


def dist(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def get_adjacents(i, j):
    return [(i + 1, j),
            (i - 1, j),
            (i, j - 1),
            (i, j + 1)]


def not_oob(i, j, height, width):
    return i >= 0 and i < height and j >= 0 and j < width


def dup_map(mapu):
    og = len(mapu[0])
    for i in range(0, 4):
        for ind in range(len(mapu)):
            mapu[ind] += [(x + i) % 9 + 1 for x in mapu[ind][:og]]
    og = len(mapu)
    for i in range(0, 4):
        for row in mapu[:og]:
            mapu.append([(x + i) % 9 + 1 for x in row])
    return mapu


def solve(input_list: list):
    mapu = dup_map([[int(c) for c in l] for l in input_list])
    height = len(mapu)
    width = len(mapu[0])
    targ = (height - 1, width - 1)
    q = PriorityQueue()
    q.put((dist((0, 0), targ), (0, 0, 0)))
    passed = set()
    while q:
        _, (i, j, n) = q.get()
        if (i, j) in passed:
            continue
        if (i, j) == targ:
            return n + mapu[i][j] - mapu[0][0]
        passed.add((i, j))
        for i2, j2 in get_adjacents(i, j):
            if (i2, j2) not in passed and not_oob(i2, j2, height, width):
                n2 = mapu[i][j] + n
                q.put((dist((i2, j2), targ) + n2, (i2, j2, n2)))


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
