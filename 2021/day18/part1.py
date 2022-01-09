from copy import deepcopy
import math


CARRYING = 1
CARRIED = 0
NOT_CARRYING = -1


def walk_explode(num, depth, pos, lastregpos, carry=None):
    if pos:
        one_up = num
        for p in pos[:-1]:
            one_up = one_up[p]
        cur = one_up[pos[-1]]
    else:
        cur = num
    if carry is not None and not isinstance(cur, list):
        one_up[pos[-1]] += carry
        return CARRIED, None, pos
    elif carry is None and not isinstance(cur, list):
        return NOT_CARRYING, None, pos
    if carry is None and depth >= 4:
        #print('DEEP', pos, one_up, cur)
        left, right = cur
        if lastregpos:
            x = num
            #print('HI', lastregpos, x)
            for p in lastregpos[:-1]:
                x = x[p]
            x[lastregpos[-1]] += left
        one_up[pos[-1]] = 0
        return CARRYING, right, pos
    else:  # list
        #print('LIST', pos, num)
        c = NOT_CARRYING if carry is None else CARRYING
        newlastreg = deepcopy(lastregpos)
        to_c = carry
        for i, _ in enumerate(cur):
            #print(c)
            if c == CARRIED:
                #print('DONE')
                return CARRIED, None, lastregpos
            newpos = deepcopy(pos)
            newpos.append(i)
            c, to_c, newlastreg = walk_explode(num, depth + 1, newpos, newlastreg, to_c)
        return c, to_c, newlastreg


def walk_split(num, pos):
    if pos:
        one_up = num
        for p in pos[:-1]:
            one_up = one_up[p]
        cur = one_up[pos[-1]]
    else:
        cur = num
    if not isinstance(cur, list):
        if cur >= 10:
            one_up[pos[-1]] = [math.floor(cur / 2), math.ceil(cur / 2)]
            return True
        else:
            return False
    else:
        split = False
        for i, _ in enumerate(cur):
            newpos = deepcopy(pos)
            newpos.append(i)
            split = walk_split(num, newpos)
            if split:
                break
        return split


def reduce(num):
    reduction = deepcopy(num)
    while True:
        carried, _, _ = walk_explode(reduction, 0, [], [])
        if carried == NOT_CARRYING:
            if not walk_split(reduction, []):
                break
    return reduction


def magn(num):
    left, right = num
    if isinstance(left, list):
        lp = magn(left)
    else:
        lp = left
    if isinstance(right, list):
        rp = magn(right)
    else:
        rp = right
    return 3 * lp + 2 * rp


def solve(input_list: list):
    cur = input_list[0]
    for num in input_list[1:]:
        #print(cur)
        unreduced = [cur, num]
        cur = reduce(unreduced)
    return magn(cur)


with open('input.txt', 'r') as f:
    input_list = [eval(s) for s in f.read().strip().split('\n')]
    print(solve(input_list))
    #print(magn([[9, 1], [1, 9]]))
