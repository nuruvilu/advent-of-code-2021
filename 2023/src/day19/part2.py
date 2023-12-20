import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


COMPARE = 0
AUTO = 1

def calc(limits):
    total = 1
    for minv, maxv in limits:
        total *= max(maxv + 1 - minv, 0)
    return total


def recurse(workflow_dict, progress):
    curr, path, step_i, limits = progress
    if curr == 'A':
        return calc(limits)
    elif curr == 'R':
        return 0
    r, a = 0, 0
    step_type, dest, value, comp, num = workflow_dict[curr][step_i]
    next_limits = limits
    if step_type == AUTO:
        return recurse(workflow_dict, (dest, path + [dest], 0, limits))
    else:
        minv, maxv = limits[value]
        if comp == '>':
            total = 0
            if minv <= num:
                total += recurse(workflow_dict, (curr, path, step_i + 1, aoc.emplace(limits, (minv, num), value)))
            if maxv > num:
                total += recurse(workflow_dict, (dest, path + [dest], 0, aoc.emplace(limits, (max(num + 1, minv), maxv), value)))
            return total
        elif comp == '<':
            total = 0
            if maxv >= num:
                total += recurse(workflow_dict, (curr, path, step_i + 1, aoc.emplace(limits, (num, maxv), value)))
            if minv < num:
                total += recurse(workflow_dict, (dest, path + [dest], 0, aoc.emplace(limits, (minv, min(num - 1, maxv)), value)))
            return total


def solve(inp):
    workflows, _parts = inp
    workflow_dict = {}
    for workflow in workflows:
        name, steps = workflow[:-1].split('{')
        steps = steps.split(',')
        parsed_steps = []
        for step in steps:
            if ':' in step:
                c, dest = step.split(':')
                if '>' in c:
                    score, num = c.split('>')
                    parsed_steps.append((COMPARE, dest, 'xmas'.index(score), '>', int(num)))
                else:
                    score, num = c.split('<')
                    parsed_steps.append((COMPARE, dest, 'xmas'.index(score), '<', int(num)))
            else:
                parsed_steps.append((AUTO, step, None, None, None))
        workflow_dict[name] = parsed_steps
    progress = ('in', ['in'], 0, ((1, 4000), (1, 4000), (1, 4000), (1, 4000)))
    return recurse(workflow_dict, progress)


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=19, year=2023))
    print(solve(inp))
