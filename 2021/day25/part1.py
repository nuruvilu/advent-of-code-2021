
def solve(input_list: list):
    moved = True
    cucumbers = input_list
    steps = 0
    while moved:
        steps += 1
        print(steps)
        moved = False
        cucumbers2 = ['.' * len(cucumbers[0])] * len(cucumbers)
        for i, row in enumerate(cucumbers2):
            cucumbers2[i] = list(row)
        for i, row in enumerate(cucumbers):
            for j, cuc in enumerate(row):
                if cuc == '>':
                    if cucumbers[i][(j + 1) % len(row)] == '.':
                        moved = True
                        cucumbers2[i][(j + 1) % len(row)] = '>'
                    else:
                        cucumbers2[i][j] = '>'
                elif cuc != '.':
                    cucumbers2[i][j] = cuc
        cucumbers = cucumbers2
        #print(cucumbers)
        cucumbers2 = ['.' * len(cucumbers[0])] * len(cucumbers)
        for i, row in enumerate(cucumbers2):
            cucumbers2[i] = list(row)
        for i, row in enumerate(cucumbers):
            for j, cuc in enumerate(row):
                if cuc == 'v':
                    if cucumbers[(i + 1) % len(cucumbers)][j] == '.':
                        moved = True
                        cucumbers2[(i + 1) % len(cucumbers2)][j] = 'v'
                    else:
                        cucumbers2[i][j] = 'v'
                elif cuc != '.':
                    cucumbers2[i][j] = cuc
        cucumbers = cucumbers2
        #print(cucumbers)
    return steps


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    print(solve(input_list))
