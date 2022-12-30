N, M = map(int, input().split())
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0


def dfs(board, x, y):
    board[x][y] = 1

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx >= 0 and ny >= 0 and nx < N and ny < M and board[nx][ny] == 0):
            dfs(board, nx, ny)


for i in range(N):
    board.append(list(map(int, list(input()))))

for i in range(N):
    for j in range(M):
        if (board[i][j] == 0):
            count += 1
            dfs(board, i, j)

print(count)
