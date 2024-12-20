import math
import operator
import re

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path
from multiprocessing import Pool

import common as aoc
from aocd import get_data


'''
sample:::
while A != 0:
    A //= 8
    out A % 8

actual:::
while A != 0:
    B = A % 8
    B ^= 1
    C = A // 2^B
    B = C
    A //= 8
    out B % 8
'''
ADV, BXL, BST, JNZ, BXC, OUT, BDV, CDV = tuple(range(8))
A, B, C = (0, 1, 2)


def resolve_combo(registers, operand):
    if 4 <= operand <= 6:
        return registers[operand - 4]
    return operand


def run(program, a_start):
    registers = [a_start, 0, 0]
    out = []
    i_ptr = 0
    while i_ptr < len(program) - 1:
        opcode, operand = program[i_ptr:i_ptr+2]
        if opcode == ADV:
            registers[A] //= 2 ** resolve_combo(registers, operand)
        elif opcode == BXL:
            registers[B] ^= operand
        elif opcode == BST:
            registers[B] = resolve_combo(registers, operand) % 8
        elif opcode == JNZ:
            if registers[A] != 0:
                i_ptr = operand
                continue
        elif opcode == BXC:
            registers[B] ^= registers[C]
        elif opcode == OUT:
            out.append(resolve_combo(registers, operand) % 8)
        elif opcode == BDV:
            registers[B] = registers[A] // (2 ** resolve_combo(registers, operand))
        elif opcode == CDV:
            registers[C] = registers[A] // (2 ** resolve_combo(registers, operand))
        i_ptr += 2
    return out


def solve(inp):
    _, program = inp
    program = [int(n) for n in program[0].split(': ')[1].split(',')]
    q = [(len(program) - 1, 0)]
    while q:
        d, n = q.pop(0)
        for a in range(8 * n, 8 * (n + 1)):
            if run(program, a) == program[d:]:
                if d == 0:
                    return a
                q.append((d - 1, a))


if __name__ == '__main__':
    #inp = aoc.readstanzas(Path('sample.txt'))
    inp = aoc.readstanzas(get_data(day=17, year=2024))
    print(solve(inp))
