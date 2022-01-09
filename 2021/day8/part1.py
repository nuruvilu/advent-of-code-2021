
def solve(input_list: list):
    s = 0
    for inp in input_list:
        output = inp.split('|')[1].split()
        for o in output:
            if len(o) in {2, 3, 4, 7}:
                s += 1
    return s


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
