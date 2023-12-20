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


def parse_part(part_str) -> {}:
    x, m, a, s = [int(z.split('=')[-1]) for z in part_str[1:-1].split(',')]
    return {'x': x, 'm': m, 'a': a, 's': s}


def solve(inp):
    workflows, parts = inp
    parts = [parse_part(part) for part in parts]
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
                    parsed_steps.append((COMPARE, dest, score, '>', int(num)))
                else:
                    score, num = c.split('<')
                    parsed_steps.append((COMPARE, dest, score, '<', int(num)))
            else:
                parsed_steps.append((AUTO, step, None, None, None))
        workflow_dict[name] = parsed_steps
    total = 0
    #print(workflow_dict)
    for part in parts:
        curr = 'in'
        while curr not in 'AR':
            for step_type, dest, value, comp, num in workflow_dict[curr]:
                if step_type == AUTO:
                    curr = dest
                    break
                elif comp == '>' and part[value] > num:
                    curr = dest
                    break
                elif comp == '<' and part[value] < num:
                    curr = dest
                    break
        if curr == 'A':
            total += sum(part.values())
    return total


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=19, year=2023))
    print(solve(inp))
