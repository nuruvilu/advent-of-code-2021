
def solve(input_list: list):
    front, back = input_list.split(', ')
    ystr = back.split('=')[1]
    miny, maxy = [int(x) for x in ystr.split('..')]
    xstr = front.split('=')[1]
    minx, maxx = [int(x) for x in xstr.split('..')]

    def in_target(x, y):
        return minx <= x <= maxx and miny <= y <= maxy

    def shoot(x, y, dx, dy):
        topy = -999999
        i = 0
        while not in_target(x, y) and i < 256:
            x += dx
            y += dy
            if y > topy:
                topy = y
            if dx:
                dx += 1 if dx < 0 else -1
            dy -= 1
            i += 1
        return -999999 if i == 256 else topy

    count = 0
    for dx in range(1, maxx + 100):
        for dy in range(miny - 100, 1000):
            if shoot(0, 0, dx, dy) != -999999:
                count += 1

    return count


with open('input.txt', 'r') as f:
    input_list = f.read().strip()
    print(solve(input_list))
