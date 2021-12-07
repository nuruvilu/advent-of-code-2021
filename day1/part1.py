import operator
from functools import reduce

with open('input.txt', 'r') as f:
    inp = f.readlines()
    nums = [int(s.strip('\n')) for s in inp]
    pairs = [(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]
    print(pairs)
    increases = map(lambda p: 1 if p[0] < p[1] else 0, pairs)
    increase_count = reduce(operator.add, increases)
    print(increase_count)
