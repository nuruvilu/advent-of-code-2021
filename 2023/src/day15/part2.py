import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    seq = ''.join(inp)
    steps = seq.split(',')
    boxes = [[] for _ in range(256)]
    for step in steps:
        curr = 0
        curr_label, curr_lens = re.split(r'[-=]', step)
        for ch in curr_label:
            curr += ord(ch)
            curr *= 17
            curr %= 256
        box = curr
        if '-' in step:
            boxes[box] = [(label, lens) for label, lens in boxes[box] if label != curr_label]
        else:
            curr_lens = int(curr_lens)
            for i, (label, lens) in enumerate(boxes[box]):
                if label == curr_label:
                    boxes[box][i] = (curr_label, curr_lens)
                    break
            else:
                boxes[box].append((curr_label, curr_lens))
    total = 0
    for i, box in enumerate(boxes, start=1):
        for j, (_, lens) in enumerate(box, start=1):
            total += i * j * lens
    return total


if __name__ == '__main__':
    #inp = aoc.readlines(Path('sample.txt'))
    inp = aoc.readlines(get_data(day=15, year=2023))
    print(solve(inp))
