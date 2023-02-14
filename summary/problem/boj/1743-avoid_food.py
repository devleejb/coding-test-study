from collections import deque

N, M, K = map(int, input().split())
board = [[False] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
result = -1

for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = True


def dfs(row, col):
    q = deque()
    count = 0
    q.append((row, col))

    while q:
        row, col = q.pop()

        if (visited[row][col] == True):
            continue

        visited[row][col] = True
        count += 1

        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if (0 <= nr and nr < N and 0 <= nc and nc < M):
                if (visited[nr][nc] == False and board[nr][nc] == True):
                    q.append((nr, nc))

    return count


for i in range(N):
    for j in range(M):
        if (visited[i][j] == False and board[i][j] == True):
            result = max(result, dfs(i, j))

print(result)
