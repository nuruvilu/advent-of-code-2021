import threading


def val(vars_, token):
    if token in vars_:
        return vars_[token]
    return int(token)


# dont use this, solve on paper instead


def do_stuff(prog, i):
    mn = 0
    while True:
        if i < 11111111111111:
            print('NO')
            return 'NO'
        i -= 1
        numstr = str(i)
        if str(i).count('0') > 0:
            continue
        z = 16 + int(numstr[0])
        z = 26*z + int(numstr[1]) + 3
        z = 26*z + int(numstr[2]) + 2
        z = 26*z + int(numstr[3]) + 7
        z = (25 * int(numstr[4] == z % 26 - 10) + 1) * (z // 26)
        z = 26*z + int(numstr[5]) + 6
        z = (25 * int(numstr[6] == z % 26 - 14) + 1) * (z // 26)
        z = 26*z + int(numstr[7]) + 11
        z = (25 * int(numstr[8] == z % 26 - 4) + 1) * (z // 26)
        z = (25 * int(numstr[9] == z % 26 - 3) + 1) * (z // 26)
        z = 26*z + int(numstr[10]) + 11
        z = (25 * int(numstr[11] == z % 26 - 3) + 1) * (z // 26)
        z = (25 * int(numstr[12] == z % 26 - 9) + 1) * (z // 26)
        z = (25 * int(numstr[13] == z % 26 - 12) + 1) * (z // 26)
        if z < mn:
            mn = z
            print(mn)
        if z == 0:
            print('DONE', i)
            return


def solve(input_list: list):
    prog = [line.split(' ') for line in input_list]
    threads = []
    for x in [(1_000_000_000_00000 // 10) * i for i in range(10)]:
        #if x < 1000000000000:
            #print(x)
        t = threading.Thread(target=do_stuff, args=(prog, x))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
