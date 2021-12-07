
def solve(input_list: list):
    gamma = ''
    eps = ''
    for index in range(len(input_list[0])):
        ones = 0
        zeros = 0
        for j, _ in enumerate(input_list):
            if input_list[j][index] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += '1'
            eps += '0'
        else:
            gamma += '0'
            eps += '1'
    gamma = int(gamma, 2)
    eps = int(eps, 2)
    return gamma * eps


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    print(solve(input_list))
