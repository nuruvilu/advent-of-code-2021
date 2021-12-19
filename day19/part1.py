from collections import defaultdict


def subperm(x, y, z):
    return [
        (x, y, z),
        (x, y, -z),
        (x, -y, z),
        (x, -y, -z),
        (-x, y, z),
        (-x, y, -z),
        (-x, -y, z),
        (-x, -y, -z)
    ]


def permute(x, y, z):
    return subperm(x, y, z) + subperm(z, y, x) \
         + subperm(y, x, z) + subperm(y, z, x) \
         + subperm(x, z, y) + subperm(z, x, y)


def vec_sub(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])


def vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])


def triangulate(left_beacons, right_beacons):
    perms = list(zip(*[permute(x, y, z) for x, y, z in right_beacons]))
    #print(perms)
    for i, p in enumerate(perms):
        #print(i)
        #if (-686, 422, -578) in p:
            #print(p)
        counts = defaultdict(int)
        for l in left_beacons:
            for r in p:
                counts[vec_sub(l, r)] += 1
        for pos, count in counts.items():
            #if pos == (68, -1246, -43):
                #print(count)
            if count >= 12:
                return pos, p
    return False, None


def solve(input_list: list):
    scanners = []
    for scanner_str in input_list:
        rbeacons = [[int(n) for n in line.split(',')] for line in scanner_str.split('\n') if not line.startswith('---')]
        scanners.append(rbeacons)
    detected = {}
    detected[0] = (0, 0, 0)
    dc = 1
    beacons = scanners[0]
    while dc < len(scanners):
        for si, b in enumerate(scanners):
            if si in detected:
                continue
            pos, perms = triangulate(beacons, b)
            if pos:
                dc += 1
                detected[si] = pos
                for beacon in perms:
                    beacons.append(vec_add(pos, beacon))
    print(detected)
    return len({tuple(b) for b in beacons})


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n\n')]
    print(solve(input_list))
    #print(dist(-447, -329, 318, -537, -823, -458))
