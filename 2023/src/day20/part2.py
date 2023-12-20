import math
import operator

import sys
sys.path.append('..')

from collections import deque
from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


BROADCASTER = 0
FLIP_FLOP = 1
CONJUNCTION = 2
OFF, ON = False, True
LOW, HIGH = False, True


def solve(inp):
    modules = {}
    pre_point = None
    for line in inp:
        name, dests = line.split(' -> ')
        dests = dests.split(', ')
        if 'rx' in dests:
            pre_point = name[1:]
        if name.startswith('%'):
            modules[name[1:]] = (FLIP_FLOP, OFF, dests)
        elif name.startswith('&'):
            modules[name[1:]] = (CONJUNCTION, {}, dests)
        else:
            modules[name] = (BROADCASTER, None, dests)
    for name, (_, _, dests) in modules.items():
        for dest in dests:
            if dest in modules and modules[dest][0] == CONJUNCTION:
                modules[dest][1][name] = LOW
    cycles = 0
    pre_cycles = {}
    while True:
        cycles += 1
        curr_highs, curr_lows = 0, 0
        pulses = deque([('broadcaster', LOW, 'button')])
        while pulses:
            target, level, source = pulses.popleft()
            if target == 'rx' and level == LOW:
                return cycles
            elif target == pre_point and level == HIGH and source not in pre_cycles:
                pre_cycles[source] = cycles
                if len(pre_cycles) == len(modules[pre_point][1]):
                    return reduce(aoc.lcm, pre_cycles.values())
            if target in modules:
                kind, state, dests = modules[target]
                if kind == BROADCASTER:
                    for dest in dests:
                        pulses.append((dest, level, target))
                elif kind == FLIP_FLOP and level == LOW:
                    modules[target] = aoc.emplace(modules[target], not state, 1)
                    for dest in dests:
                        pulses.append((dest, HIGH if state == OFF else LOW, target))
                elif kind == CONJUNCTION:
                    modules[target][1][source] = level
                    all_high = reduce(operator.and_, modules[target][1].values())
                    for dest in dests:
                        pulses.append((dest, LOW if all_high else HIGH, target))


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=20, year=2023))
    print(solve(inp))
