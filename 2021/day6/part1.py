
def solve(input_list: list):
    days = 80
    fish = [0] * 10
    for f in input_list:
        fish[f] += 1
    for _ in range(days):
        for i, c in enumerate(fish):
            if i:
                fish[i - 1] = c
            else:
                fish[9] += c
                fish[7] += c
        fish[9] = 0
    return sum(fish)


with open('input.txt', 'r') as f:
    input_list = [int(s) for s in f.read().strip('\n').split(',')]
    print(solve(input_list))
