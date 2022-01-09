
steps = {}


def step_size(n):
    if n in steps:
        return steps[n]
    s = 0
    for i in range(1, n+1):
        s += i
        steps[i] = s
    return s


def solve(input_list: list):
    maxi, mini = 0, 2_000_000
    for n in input_list:
        if n > maxi:
            maxi = n
        elif n < mini:
            mini = n
    d = 2_000_000_000_000_000
    for m in range(mini, maxi + 1):
        total = 0
        for j in input_list:
            total += step_size(abs(m - j))
        if total < d:
            d = total
    return d


with open('input.txt', 'r') as f:
    input_list = [int(s) for s in f.read().strip().split(',')]
    print(solve(input_list))
