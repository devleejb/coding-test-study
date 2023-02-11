from sys import stdin

input = stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
count = 0

VERTICAL = 0
HORIZONTAL = 1
DIAGONAL = 2


def dfs(row, col, type):
    global count

    if ((row, col) == (N - 1, N - 1)):
        count += 1
        return

    if ((type == DIAGONAL or type == HORIZONTAL) and col + 1 < N):
        if (board[row][col + 1] == 0):
            dfs(row, col + 1, HORIZONTAL)

    if ((type == VERTICAL or type == DIAGONAL) and row + 1 < N):
        if (board[row + 1][col] == 0):
            dfs(row + 1, col, VERTICAL)

    if (row + 1 < N and col + 1 < N):
        if (board[row + 1][col + 1] == 0 and board[row + 1][col] == 0 and board[row][col + 1] == 0):
            dfs(row + 1, col + 1, DIAGONAL)


dfs(0, 1, HORIZONTAL)

print(count)
