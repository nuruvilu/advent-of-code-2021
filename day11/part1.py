
def get_adjacents(i, j):
    return [(i + 1, j),
            (i - 1, j),
            (i + 1, j + 1),
            (i + 1, j - 1),
            (i - 1, j + 1),
            (i - 1, j - 1),
            (i, j - 1),
            (i, j + 1)]


def not_oob(i, j, height, width):
    return i >= 0 and i < height and j >= 0 and j < width


def solve(input_list: list):
    octos = [[int(c) for c in s] for s in input_list]
    flashes = 0
    height = len(octos)
    width = len(octos[0])
    for _ in range(100):
        must = set()
        has = set()
        for i, row in enumerate(octos):
            for j, octo in enumerate(row):
                if octo >= 9:
                    must.add((i, j))
                else:
                    octos[i][j] += 1
        while must:
            i, j = must.pop()
            adjs = get_adjacents(i, j)
            for ip, jp in adjs:
                if not_oob(ip, jp, height, width):
                    if (ip, jp) not in must and (ip, jp) not in has:
                        if octos[ip][jp] >= 9:
                            must.add((ip, jp))
                        else:
                            octos[ip][jp] += 1
            
            has.add((i, j))
            flashes += 1
        for i, j in has:
            octos[i][j] = 0
    return flashes


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n')]
    print(solve(input_list))
