
openners = {
    '{': '}',
    '<': '>',
    '(': ')',
    '[': ']'
}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def solve(input_list: list):
    ss = []
    for line in input_list:
        stack = []
        nogood = False
        s = 0
        for c in line:
            if c in openners:
                stack.append(c)
            else:
                last = stack.pop()
                if openners[last] != c:
                    nogood = True
                    break
        if not nogood:
            while stack:
                cur = stack.pop()
                s *= 5
                s += points[openners[cur]]
            ss.append(s)
    sortedd = sorted(ss)
    if len(sortedd) % 2 == 1:
        return sortedd[(len(sortedd) - 1) // 2]
    else:
        return (sortedd[(len(sortedd) - 1) // 2]
                + sortedd[((len(sortedd) - 1) // 2) + 1]) / 2


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
