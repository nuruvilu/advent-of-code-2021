
openners = {
    '{': '}',
    '<': '>',
    '(': ')',
    '[': ']'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def solve(input_list: list):
    s = 0
    for line in input_list:
        stack = []
        for c in line:
            if c in openners:
                stack.append(c)
            else:
                last = stack.pop()
                if openners[last] != c:
                    print(last, c)
                    s += points[c]
                    break
    return s


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
