
def solve(input_list: list):
    moves = [tuple(line.split(' ')) for line in input_list]
    depth = 0
    length = 0
    for direction, mag in moves:
        magn = int(mag)
        if direction == 'down':
            depth += magn
        elif direction == 'up':
            depth -= magn
        elif direction == 'forward':
            length += magn
    return depth * length


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    print(solve(input_list))
