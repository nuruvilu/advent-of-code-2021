from collections import defaultdict, Counter


def solve(input_list: list):
    template = input_list[0]
    rules = [r.split(' -> ') for r in input_list[1].split('\n')]
    rules = {r[0]: r[1] for r in rules}
    pairs = Counter(template[i - 1: i + 1] for i in range(1, len(template)))
    for _ in range(40):
        neo = defaultdict(int)
        for p, c in pairs.items():
            inject = rules[p]
            neo[p[0] + inject] += c
            neo[inject + p[1]] += c
        pairs = neo
    counts = defaultdict(int)
    for p, c in pairs.items():
        counts[p[0]] += c
    counts[template[-1]] += 1
    return max(counts.values()) - min(counts.values())


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n\n')]
    print(solve(input_list))
