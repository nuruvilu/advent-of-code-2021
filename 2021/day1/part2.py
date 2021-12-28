
import operator
from functools import reduce


def compare_increasing(nums: list) -> int:
    pairs = [(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]
    print(pairs)
    increases = map(lambda p: 1 if p[0] < p[1] else 0, pairs)
    return reduce(operator.add, increases)


with open('input.txt', 'r') as f:
    inp = f.readlines()
    nums = [int(s.strip('\n')) for s in inp]
    nums = [nums[i] + nums[i + 1] + nums[i + 2] for i in range(len(nums) - 2)]
    increase_count = compare_increasing(nums)
    print(increase_count)
