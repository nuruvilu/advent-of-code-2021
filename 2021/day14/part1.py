from collections import Counter


def solve(input_list: list):
    template = input_list[0]
    rules = [r.split(' -> ') for r in input_list[1].split('\n')]
    rules = {r[0]: r[1] for r in rules}
    for _ in range(10):
        neo = template[0]
        for i in range(1, len(template)):
            inject = rules[template[i - 1: i + 1]]
            neo += inject + template[i]
        template = neo
    counts = Counter(template)
    return max(counts.values()) - min(counts.values())


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n\n')]
    print(solve(input_list))
