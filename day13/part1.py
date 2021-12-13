
def print_dots(dots):
    size = 20
    for i in range(size):
        for j in range(size):
            if (j, i) in dots:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()


def solve(input_list: list):
    dots = input_list[0].split('\n')
    dots = [d.split(',') for d in dots]
    dots = {(int(d[0]), int(d[1])) for d in dots}
    moves = input_list[1].split('\n')
    moves = [x.split('=') for x in moves]
    moves = [(x[0][-1], int(x[1])) for x in moves]
    for axis, val in moves:
        newdots = set()
        for x, y in dots:
            if axis == 'x':
                newx = val - (x - val) if x > val else x 
                newdots.add((newx, y))
            else:
                newy = val - (y - val) if y > val else y
                newdots.add((x, newy))
        dots = newdots
        break
    return len(dots)


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n\n')]
    print(solve(input_list))
