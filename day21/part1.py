
def ahh(n):
    x = n % 10
    return x if x else 10


def next_die(n):
    x = n
    while True:
        if x < 100:
            x += 1
        else:
            x = 1
        yield x


def solve(input_list: list):
    ps = [7, 2]
    p = [0, 0]
    dice = next_die(0)
    turn = 0
    rolls = 0
    while p[0] < 1000 and p[1] < 1000:
        roll = sum(next(dice) for _ in range(3))
        newspot = ps[turn] + roll
        ps[turn] = ahh(newspot)
        p[turn] += ps[turn]
        turn = 0 if turn else 1
        rolls += 3
    return min(p) * rolls


with open('input.txt', 'r') as f:
    print(solve(None))
