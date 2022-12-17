import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from collections import defaultdict

import common as aoc


rocks = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],  # _
    [(2, 1), (3, 2), (3, 1), (3, 0), (4, 1)],  # +
    [(2, 0), (3, 0), (4, 2), (4, 1), (4, 0)],  # J
    [(2, 3), (2, 2), (2, 1), (2, 0)],  # |
    [(2, 1), (2, 0), (3, 1), (3, 0)]  # ■
]


def get_relative(rock):
    min_y = min(r[1] for r in rock)
    return tuple((x, y - min_y) for x, y in rock)


def collides(rock, blocked):
    for x, y in rock:
        if (x, y) in blocked or not (0 <= x <= 6) or y < 0:
            return True
    return False


def cycles(i, j, recording):
    if len(recording) - j < j - i:
        return False
    i_prime, j_prime = i, j
    while i_prime < j:
        if recording[i_prime] != recording[j_prime]:
            return False
        i_prime += 1
        j_prime += 1
    return True


def calc_gain(i, j, recording):
    return sum(r[1] for r in recording[i:j])


def solve(inp):
    rocks_dropped = 0
    max_height = 0
    rock_idx = 0
    flow_idx = 0
    blocked = set()
    recording = []
    relatives = defaultdict(list)
    cap = 1_000_000_000_000
    while rocks_dropped < cap:
        if rocks_dropped % 1000 == 0:
            print(rocks_dropped)
        rock = [(x, y + max_height + 3) for x, y in rocks[rock_idx]]
        while True:
            flow = inp[flow_idx]
            flow_idx = (flow_idx + 1) % len(inp)
            new_rock = [(x + (1 if flow == '>' else -1), y) for x, y in rock]
            if not collides(new_rock, blocked):
                # print(flow, new_rock)
                rock = new_rock
            new_rock = [(x, y - 1) for x, y in rock]
            if collides(new_rock, blocked):
                former_max_height = max_height
                for block in rock:
                    blocked.add(block)
                    if block[1] + 1 > max_height:
                        max_height = block[1] + 1
                height_diff = max_height - former_max_height
                relative = get_relative(rock)
                if len(relatives[relative]) >= 2:
                    for i in relatives[relative]:
                        for j in relatives[relative]:
                            if i < j and cycles(i, j, recording):
                                print('CYCLE DETECTED', i, j, rocks_dropped)
                                gain = calc_gain(i, j, recording)
                                rock_diff = j - i
                                x = (cap - rocks_dropped) // rock_diff
                                rocks_dropped += rock_diff * x
                                max_height += gain * x
                                idx = i
                                print(rocks_dropped - cap, max_height)
                                print(cap / rock_diff, x)
                                while rocks_dropped < cap:
                                    rocks_dropped += 1
                                    max_height += recording[idx][1]
                                    idx += 1
                                return max_height - height_diff
                relatives[relative].append(rocks_dropped)
                recording.append((relative, height_diff))
                rocks_dropped += 1
                break
            rock = new_rock
        rock_idx = (rock_idx + 1) % len(rocks)
    return max_height


if __name__ == '__main__':
    inp = aoc.read('input.txt')
    print(solve(inp))
