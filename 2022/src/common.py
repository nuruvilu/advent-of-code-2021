import math
import operator

from functools import reduce
from pathlib import Path


def dist(p1, p2) -> float:
    sq_diffs = ((x1 - x2) * (x1 - x2) for x1, x2 in zip(p1, p2))
    return math.sqrt(reduce(operator.add, sq_diffs, 0))


def mandist(p1, p2) -> float:
    return reduce(operator.add, (abs(x1 - x2) for x1, x2 in zip(p1, p2)), 0)


def median(lst: [int | float]) -> int | float:
    middle_idx = (len(lst) - 1) // 2
    if len(lst) % 2 == 0:
        return (lst[middle_idx] + lst[middle_idx + 1]) / 2
    else:
        return lst[middle_idx]


def partition(lst: list, psize: int) -> [list]:
    return [lst[i:i + psize] for i in range(0, len(lst), psize)]


def window(lst: list, wsize: int) -> [tuple]:
    return list(zip(*[lst[i:] for i in range(wsize)]))


def inbounds2(i, j, h, w) -> bool:
    return 0 <= i < h and 0 <= j < w


def inbounds3(x, y, z, maxx, maxy, maxz) -> bool:
    return 0 <= x < maxx and 0 <= y < maxy and 0 <= z < maxz


def emplace(lst: list | tuple, val, i: int) -> list:
    new_list = list(lst)
    new_list[i] = val
    return tuple(new_list) if isinstance(lst, tuple) else new_list


def adjs(point) -> [tuple]:
    adjacents = []
    for i, n in enumerate(point):
        for o in (-1, 1):
            adjacents.append(emplace(point, n + o, i))
    return adjacents


def adjsdiags2(point) -> [tuple]:
    x, y = point
    return [
        (x - 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
        (x + 1, y),
        (x + 1, y - 1),
        (x, y - 1),
        (x - 1, y - 1)
    ]


def readnums(path: str) -> [int]:
    return [int(line) for line in readlines(path)]


def readlines(path: str) -> [str]:
    return read(path).split('\n')


def read(path: str) -> str:
    return Path(path).read_text()


def readstanzas(path: str) -> [[str]]:
    return [s.split('\n') for s in read(path).split('\n\n')]


def readstanzanums(path: str) -> [[int]]:
    return [[int(e) for e in s] for s in readstanzas(path)]
