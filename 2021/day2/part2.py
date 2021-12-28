
def solve(input_list: list):
    moves = [tuple(line.split(' ')) for line in input_list]
    aim = 0
    depth = 0
    length = 0
    for direction, mag in moves:
        magn = int(mag)
        if direction == 'down':
            aim += magn
        elif direction == 'up':
            aim -= magn
        elif direction == 'forward':
            length += magn
            depth += aim * magn
    return depth * length


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    print(solve(input_list))
