
def solve(input_list: list):
    se = ''
    l = input_list
    i = 0
    while len(l) != 1:
        ones = 0
        zeros = 0
        for x in l:
            if x[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            se += '1'
        elif ones == zeros:
            se += '1'
        else:
            se += '0'
        l = [x for x in input_list if x.startswith(se)]
        i += 1
    o = l[0]
    se = ''
    l = input_list
    i = 0
    while len(l) != 1:
        ones = 0
        zeros = 0
        for x in l:
            if x[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones < zeros:
            se += '1'
        elif ones == zeros:
            se += '0'
        else:
            se += '0'
        l = [x for x in input_list if x.startswith(se)]
        i += 1
    c = l[0]
    return int(c, 2) * int(o, 2)


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    print(solve(input_list))
