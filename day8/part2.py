
def flip(t):
    return {v: k for k, v in t.items()}


normal = {
    'abcdeg': 0,
    'ab': 1,
    'acdfg': 2,
    'abcdf': 3,
    'abef': 4,
    'bcdef': 5,
    'bcdefg': 6,
    'abd': 7,
    'abcdefg': 8,
    'abcdef': 9
}


def final_t(t):
    newt = {}
    for s in normal.keys():
        newv = ''
        for c in s:
            newv += t[c]
        newt[''.join(sorted(newv))] = s
    return newt


def solve(input_list: list):
    s = 0
    for inp in input_list:
        reads = inp.split('|')[0].split()
        table = {}
        assigned = set()
        for read in sorted(reads, key=lambda x: len(x)):
            r = ''.join(sorted(read))
            if r in table:
                continue
            elif len(r) == 2:
                table['a'] = r[0]
                table['b'] = r[1]
                assigned.add(r[0])
                assigned.add(r[1])
            elif len(r) == 3:
                mm = [s for s in r if s not in assigned][0]
                table['d'] = mm
                assigned.add(mm)
                break
        fivews = [r for r in reads if len(r) == 5]
        x = [r for r in reads if len(r) == 4][0]
        for f in fivews:
            x = ''.join(n for n in x if n in f)
        table['f'] = x
        for f in [r for r in reads if len(r) == 4][0]:
            if f not in flip(table):
                table['e'] = f
        for f in fivews:
            c = ''.join(n for n in f if n not in flip(table))
            if len(c) == 1:
                table['c'] = c
                break
        for f in fivews:
            c = ''.join(n for n in f if n not in flip(table))
            if len(c) == 1:
                if table['b'] in f:
                    table['a'], table['b'] = table['b'], table['a']
        for c in 'abcdefg':
            if c not in flip(table):
                table['g'] = c
                break

        bettertab = final_t(table)

        output = inp.split('|')[1].split()
        x = 0
        for i, o in enumerate(output):
            val = normal[bettertab[''.join(sorted(o))]]
            x += val * 10**(3-i)
        s += x
    return s


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
