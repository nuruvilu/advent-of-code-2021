
def solve(input_list: list):
    map_ = [[int(n) for n in line] for line in input_list]
    s = 0
    for i, row in enumerate(map_):
        for j, n in enumerate(row):
            could = True
            if i != 0 and map_[i - 1][j] <= n:
                could = False
            if i != len(map_) - 1 and map_[i + 1][j] <= n:
                could = False
            if j != 0 and map_[i][j - 1] <= n:
                could = False
            if j != (len(row)) - 1 and map_[i][j + 1] <= n:
                could = False
            if could:
                s += n + 1
    return s


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
