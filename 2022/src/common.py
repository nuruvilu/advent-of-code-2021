import math
import operator

from dataclasses import dataclass, field
from functools import reduce
from heapq import heappush, heappop
from pathlib import Path
from typing import Any


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


def udlr_xy(direction: str, point: (int, int)) -> (int, int):
    if direction == 'U':
        return (point[0], point[1] + 1)
    elif direction == 'D':
        return (point[0], point[1] - 1)
    elif direction == 'R':
        return (point[0] + 1, point[1])
    elif direction == 'L':
        return (point[0] - 1, point[1])
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


def readgrid(path: str) -> [[str]]:
    return [list(line) for line in readlines(path)]


def readgridnums(path: str) -> [[int]]:
    return [[int(c) for c in line] for line in readgrid(path)]


@dataclass(order=True)
class PriorityItem:
    priority: int
    item: Any = field(compare=False)
    path: list = field(compare=False)
    total_weight: int = field(compare=False)


def astar(start, step, h, is_target):
    '''returns the priority queue item that matches is_target'''
    pqueue = []
    visited = set()
    heappush(pqueue, PriorityItem(h(start), start, [], 0))
    while pqueue:
        curr = heappop(pqueue)
        if curr.item in visited:
            continue
        if is_target(curr.item):
            return curr
        visited.add(curr.item)
        for weight, item in step(curr):
            if item not in visited:
                total_weight = weight + curr.total_weight
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
