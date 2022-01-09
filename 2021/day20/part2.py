from functools import reduce
import operator


def flatmap(lst):
    return reduce(operator.add, lst)


def not_oob(i, j, h, w):
    return 0 <= i and i < h and 0 <= j and j < w


def considerations(i, j):
    return [(i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1)]


edges = '0'


def determine(i, j, image, h, w):
    n = ''
    for ip, jp in considerations(i, j):
        #print(ip, jp)
        if not_oob(ip, jp, h, w):
            n += str(image[ip][jp])
            #print(n)
        else:
            n += edges
    #print(i, j, n)
    return int(n, 2)


def print_image(image):
    for row in image:
        for num in row:
            print('#' if num else '.', end='')
        print()
    print()


def enhance(image, algo):
    oldh = len(image)
    newh = oldh + 2
    oldw = len(image[0])
    neww = oldw + 2
    newimage = []
    for i in range(newh):
        row = []
        for j in range(neww):
            row.append(algo[determine(i - 1, j - 1, image, oldh, oldw)])
        newimage.append(row)
    return newimage


def solve(input_list: list):
    algo, image = input_list
    algo = [1 if c == '#' else 0 for c in algo]
    image = [[1 if c == '#' else 0 for c in line]
             for line in image.split('\n')]
    #print_image(image)
    #return determine(2, 2, image, 5, 5)
    for i in range(50):
        global edges
        image = enhance(image, algo)
        if edges == '0':
            edges = '1' if algo[0] else '0'
        else:
            edges = '1' if algo[511] else '0'
    #print_image(image)
    return sum(flatmap(image))


with open('input.txt', 'r') as f:
    input_list = [s for s in f.read().strip().split('\n\n')]
    print(solve(input_list))
