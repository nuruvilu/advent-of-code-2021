
def hex2(n):
    return f'{n:x}'


def drop(s, n):
    mask = 0
    for _ in enumerate(s):
        mask = (mask << 4) + 0xF
    #print(hex2(mask))
    s2 = hex2((int(s, 16) << n) & mask)
    #print(n, s, s2)
    return '0' * (len(s) - len(s2)) + s2


def parse_sub(sub: str):
    version = int(sub[0], 16) >> 1
    rest = drop(sub, 3)
    #print(rest)
    typeid = int(rest[0], 16) >> 1
    rest = drop(rest, 3)
    #print(version, typeid, rest)
    #print(rest)
    if typeid == 4:
        keepgoing = True
        num = 0
        skipped = 6
        while keepgoing:
            skipped += 5
            firstbit = int(rest[0], 16) >> 3
            #print(firstbit)
            rest = drop(rest, 1)
            #print(rest)
            num = (num << 4) + int(rest[0], 16)
            if firstbit == 0:
                keepgoing = False
            rest = drop(rest, 4)
            #print(rest)
        #print(num)
        return {'v': version,
                't': typeid,
                'body': num}, rest, skipped
    else:
        ltypeid = int(rest[0], 16) >> 3
        rest = drop(rest, 1)
        body = []
        skipped = 0
        if ltypeid == 0:
            #print(rest)
            sublen = int(rest[0:4], 16) >> 1
            #print(sublen)
            rest = drop(rest, 15)
            #print(rest)
            while skipped < sublen and int(rest, 16):
                #print(rest)
                st, rest, sk = parse_sub(rest)
                skipped += sk
                body.append(st)
                print(skipped, sublen)
                #break
        else:
            subnum = int(rest[0:3], 16) >> 1
            rest = drop(rest, 11)
            for _ in range(subnum):
                if not int(rest, 16):
                    break
                st, rest, sk = parse_sub(rest)
                skipped += sk
                body.append(st)
        return {'v': version,
                't': typeid,
                'body': body}, rest, skipped


def sum_ver(ast: dict):
    if isinstance(ast['body'], list):
        return ast['v'] + sum(sum_ver(x) for x in ast['body'])
    else:
        return ast['v']


def solve(input_num: str):
    ast, _, _ = parse_sub(input_num)
    return sum_ver(ast)


with open('input.txt', 'r') as f:
    input_num = f.read().strip()
    print(solve(input_num))
