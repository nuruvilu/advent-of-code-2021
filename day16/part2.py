from functools import reduce
import operator


def hex2(n):
    return f'{n:x}'


def drop(s, n):
    mask = 0
    for _ in enumerate(s):
        mask = (mask << 4) + 0xF
    s2 = hex2((int(s, 16) << n) & mask)
    return '0' * (len(s) - len(s2)) + s2


def parse_sub(sub: str):
    version = int(sub[0], 16) >> 1
    rest = drop(sub, 3)
    typeid = int(rest[0], 16) >> 1
    rest = drop(rest, 3)
    if typeid == 4:
        keepgoing = True
        num = 0
        skipped = 6
        while keepgoing:
            skipped += 5
            firstbit = int(rest[0], 16) >> 3
            rest = drop(rest, 1)
            num = (num << 4) + int(rest[0], 16)
            if firstbit == 0:
                keepgoing = False
            rest = drop(rest, 4)
        return {'v': version,
                't': typeid,
                'body': num}, rest, skipped
    else:
        ltypeid = int(rest[0], 16) >> 3
        rest = drop(rest, 1)
        body = []
        skipped = 7
        if ltypeid == 0:
            sublen = int(rest[0:4], 16) >> 1
            rest = drop(rest, 15)
            skipped += 15
            subskipped = 0
            while subskipped < sublen:
                st, rest, sk = parse_sub(rest)
                subskipped += sk
                body.append(st)
            skipped += subskipped
        else:
            subnum = int(rest[0:3], 16) >> 1
            rest = drop(rest, 11)
            skipped += 11
            for _ in range(subnum):
                st, rest, sk = parse_sub(rest)
                skipped += sk
                body.append(st)
        return {'v': version,
                't': typeid,
                'body': body}, rest, skipped


def evalu(ast: dict):
    if ast['t'] == 4:
        return ast['body']
    evalbody = [evalu(b) for b in ast['body']]
    if ast['t'] == 0:
        return sum(evalbody)
    elif ast['t'] == 1:
        return reduce(operator.mul, evalbody)
    elif ast['t'] == 2:
        return min(evalbody)
    elif ast['t'] == 3:
        return max(evalbody)
    elif ast['t'] == 5:
        return 1 if evalbody[0] > evalbody[1] else 0
    elif ast['t'] == 6:
        return 1 if evalbody[0] < evalbody[1] else 0
    elif ast['t'] == 7:
        return 1 if evalbody[0] == evalbody[1] else 0


def solve(input_num: str):
    ast, _, _ = parse_sub(input_num)
    return evalu(ast)


with open('input.txt', 'r') as f:
    input_num = f.read().strip()
    print(solve(input_num))
