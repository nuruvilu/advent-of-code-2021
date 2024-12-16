import math
import operator

from dataclasses import dataclass, field
from functools import reduce
from heapq import heappush, heappop
from pathlib import Path
from typing import Any
from collections import defaultdict


def lcm(x: int, y: int) -> int:
    return abs(x * y) // math.gcd(x, y)


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


def rotate_counterclock( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


def rotate_clock(m):
    return [list(reversed(col)) for col in zip(*m)]


def emplace(lst: list | tuple, val, i: int) -> list:
    new_list = list(lst)
    new_list[i] = val
    return tuple(new_list) if isinstance(lst, tuple) else new_list


def flatten(lst: [list]) -> list:
    result = []
    for l in lst:
        for item in l:
            result.append(item)
    return result


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


def udlr_xy(direction: str, point: (int, int), dist: int=1) -> (int, int):
    if direction == 'U':
        return (point[0], point[1] - dist)
    elif direction == 'D':
        return (point[0], point[1] + dist)
    elif direction == 'R':
        return (point[0] + dist, point[1])
    elif direction == 'L':
        return (point[0] - dist, point[1])
    raise ValueError(f'Invalid direction={direction}, should be U,D,R,L')


def udlr_ij(direction: str, index: (int, int)) -> (int, int):
    i, j = index
    jprime, iprime = udlr_xy(direction, (j, i))
    return iprime, jprime


def do_arithmetic(operation: str,
                  left: float | int,
                  right: float | int) -> float | int:
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '//':
        return left // right
    else:
        raise ValueError(f'Invalid operation={operation}')


def readnums(to_read: str | Path) -> [int]:
    return [int(line) for line in readlines(to_read)]


def readlines(to_read: str | Path) -> [str]:
    return read(to_read).split('\n')


def read(to_read: str | Path) -> str:
    if isinstance(to_read, Path):
        return Path(to_read).read_text()
    else:
        return to_read


def readstanzas(to_read: str | Path) -> [[str]]:
    return [s.split('\n') for s in read(to_read).split('\n\n')]


def readstanzanums(to_read: str | Path) -> [[int]]:
    return [[int(e) for e in s] for s in readstanzas(to_read)]


def readgrid(to_read: str | Path) -> [[str]]:
    return [list(line) for line in readlines(to_read)]


def readgridnums(to_read: str | Path) -> [[int]]:
    return [[int(c) for c in line] for line in readgrid(to_read)]


def readrows(to_read: str | Path) -> [[str]]:
    return [s.split() for s in readlines(to_read)]


def readrownums(to_read: str | Path) -> [[int]]:
    return [[int(n) for n in row] for row in readrows(to_read)]


def findall(s: str, sub: str) -> [int]:
    result = []
    for i, ss in enumerate(window(s, len(sub))):
        if ''.join(ss) == sub:
            result.append(i)
    return result


@dataclass(order=True)
class PriorityItem:
    priority: int
    item: Any = field(compare=False)
    path: list = field(compare=False)
    total_weight: int = field(compare=False)


def astar(start, step, h, is_target):
    '''returns the priority queue item that matches is_target'''
    pqueue = []
    visited = {}
    heappush(pqueue, PriorityItem(h(start), start, [], 0))
    while pqueue:
        curr = heappop(pqueue)
        if curr.item in visited and visited[curr.item] < curr.total_weight:
            continue
        if is_target(curr):
            return curr
        visited[curr.item] = curr.total_weight
        for weight, item in step(curr):
            total_weight = weight + curr.total_weight
            if item not in visited or visited[item] >= total_weight:
                to_add = PriorityItem(
                    h(item) + total_weight,
                    item,
                    curr.path + [curr.item],
                    total_weight
                )
                heappush(pqueue, to_add)
    raise RuntimeError('Exhausted data set without finding target!')


def dijkstra(start, step, is_target):
    '''returns the priority queue item that matches is_target'''
    return astar(start, step, lambda _: 0, is_target)


def bfs(start, step, is_target):
    '''returns the priority queue item that matches is_target'''
    return dijkstra(start, lambda x: ((1, y) for y in step(x)), is_target)
