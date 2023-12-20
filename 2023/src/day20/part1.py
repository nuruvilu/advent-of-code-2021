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
BUTTON_PRESSES = 1000


def solve(inp):
    modules = {}
    for line in inp:
        name, dests = line.split(' -> ')
        dests = dests.split(', ')
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
    lows, highs = [], []
    cycles = 0
    while cycles < BUTTON_PRESSES:
        print(cycles)
        cycles += 1
        curr_highs, curr_lows = 0, 0
        pulses = deque([('broadcaster', LOW, 'button')])
        while pulses:
            target, level, source = pulses.popleft()
            #print(source, f'-{level}->', target)
            if level == LOW:
                curr_lows += 1
            else:
                curr_highs += 1
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
        lows.append(curr_lows)
        highs.append(curr_highs)
        for kind, state, dests in modules.values():
            if state == ON:
                break
            elif isinstance(state, dict):
                if reduce(operator.or_, state.values()):
                    break
        else:
            break
        #print()
        #break
    print(lows, highs)
    print(sum(lows) * sum(highs))
    total = (BUTTON_PRESSES // cycles)**2 * sum(lows) * sum(highs)
    remaining = BUTTON_PRESSES - cycles * (BUTTON_PRESSES // cycles)
    total += sum(lows[:remaining]) * sum(highs[:remaining])
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=20, year=2023))
    print(solve(inp))
