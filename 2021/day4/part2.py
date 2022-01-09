
from functools import reduce
import operator

def check_win(board, nums_so_far):
    for row in board:
        if reduce(operator.and_, row, True):
            return True
    for j, _ in enumerate(board):
        allTrue = True
        for i, _ in enumerate(board[0]):
            allTrue = allTrue and board[i][j]
        if allTrue:
            return True


def do(board, nums):
    nums_so_far = []
    board_state = [[False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False]]
    for i, num in enumerate(nums):
        for j, row in enumerate(board):
            if num in row:
                nums_so_far.append(int(num))
                board_state[j][row.index(num)] = True
                break
        if check_win(board_state, nums_so_far):
            s = 0
            for k, row in enumerate(board):
                for l, num in enumerate(row):
                    if not board_state[k][l]:
                        s += int(num)
            return i, s * nums_so_far[-1]


def solve(input_list: list):
    nums = input_list[0].split(',')
    bs = input_list[2:]
    bs = [x for x in bs if x not in {'', ' ', '\n'}]
    boards = [bs[i:i + 5] for i in range(0, len(bs), 5)]
    boards = [[row.split() for row in b] for b in boards]
    boards = [do(b, nums) for b in boards]
    return sorted(boards, key=lambda p: p[0])[-1]


with open('input.txt', 'r') as f:
    input_list = [s.strip('\n') for s in f.readlines()]
    print(solve(input_list))
