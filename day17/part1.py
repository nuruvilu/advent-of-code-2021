
def solve(input_list: list):
    front, back = input_list.split(', ')
    ystr = back.split('=')[1]
    miny, maxy = [int(x) for x in ystr.split('..')]
    xstr = front.split('=')[1]
    minx, maxx = [int(x) for x in xstr.split('..')]

    def in_target(x, y):
        return minx <= x <= maxx and miny <= y <= maxy

    def missed(x, y):
        x > maxx or y < miny

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
            if missed(x, y):
                return -1
        return -1 if i == 256 else topy

    dx, dy = 1, 0
    while shoot(0, 0, dx, dy) == -1:
        dx += 1
    dxs = [dx]
    dx += 1
    while shoot(0, 0, dx, dy) != -1:
        dxs.append(dx)
        dx += 1
    topy = -999999
    for dxp in dxs:
        dy = 0
        countdown = False
        i = 128
        while i:
            newt = shoot(0, 0, dxp, dy)
            if newt == -1:
                countdown = True
            if countdown:
                i -= 1
            topy = max(topy, newt)
            dy += 1

    return topy


with open('input.txt', 'r') as f:
    input_list = f.read().strip()
    print(solve(input_list))
