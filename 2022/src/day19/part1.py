import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from multiprocessing import Pool

import common as aoc


ORE = 0
CLAY = 1
OBS = 2
GEO = 3
RESOURCES = [ORE, CLAY, OBS, GEO]


def parse_blueprint(string):
    groups = re.match(
        r'Blueprint \d+: Each ore robot costs (\d+) ore. '
        r'Each clay robot costs (\d+) ore. '
        r'Each obsidian robot costs (\d+) ore and (\d+) clay. '
        r'Each geode robot costs (\d+) ore and (\d+) obsidian.',
        string
    ).groups()
    groups = [int(g) for g in groups]
    return [
        (groups[0], 0, 0, 0),
        (groups[1], 0, 0, 0),
        (groups[2], groups[3], 0, 0),
        (groups[4], 0, groups[5], 0)
    ]


def harvest(bots, resources):
    return tuple(resources[r] + bots[r] for r in RESOURCES)


def can_afford(bot_cost, resources):
    for r in RESOURCES:
        if bot_cost[r] > resources[r]:
            return False
    return True


def h(state):
    bots, resources = state
    x = 0
    BOT, RES = False, False
    for r, mul in zip(RESOURCES[::-1], (10_000, 100, 6, 1)):
        if not RES and resources[r] > 0:
            x += resources[r] * mul
            RES = True
        if not BOT and bots[r] > 0:
            x += bots[r] * mul
            BOT = True
        if BOT and RES:
            return x
    return x


def calc_quality(blueprint):
    bpid, bot_costs = blueprint
    states = [((1, 0, 0, 0), (0, 0, 0, 0))]
    for i in range(24):
        # print(states[0])
        print(i)
        new_states = []
        for bots, resources in states:
            branches = [(bots, resources)]
            for i, bot_cost in enumerate(bot_costs):
                if can_afford(bot_cost, resources):
                    branches.append((
                        aoc.emplace(bots, bots[i] + 1, i),
                        tuple(resources[r] - bot_cost[r] for r in RESOURCES)
                    ))
            if can_afford(bot_costs[GEO], resources):
                branches = [(
                    aoc.emplace(bots, bots[GEO] + 1, i),
                    tuple(resources[r] - bot_costs[GEO][r] for r in RESOURCES)
                )]
            for br_bots, br_resources in branches:
                new_states.append((
                    br_bots,
                    harvest(bots, br_resources)
                ))
        states = sorted(new_states, key=h, reverse=True)[:50_000]
    best = sorted(states, key=lambda t: t[-1][-1])[-1]
    print(best)
    if best[-1][-1] == 0:
        print('ENCOUNTERED 0 :<<<<<\n\n')
    return bpid * best[-1][-1]


def solve(inp):
    blueprints = list(enumerate(map(parse_blueprint, inp), start=1))
    with Pool(len(blueprints)) as p:
        return sum(p.map(calc_quality, blueprints))


if __name__ == '__main__':
    inp = aoc.readlines('input.txt')
    print(solve(inp))
