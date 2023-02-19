from collections import deque

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0


def bfs(start_row, start_col):
    q = deque()
    visited = [[False] * M for _ in range(N)]

    q.append((start_row, start_col, 0))

    while (q):
        row, col, cost = q.popleft()

        if (visited[row][col]):
            continue

        visited[row][col] = True

        if (board[row][col] == 1):
            return cost

        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if (0 <= nr and nr < N and 0 <= nc and nc < M and visited[nr][nc] == False):
                q.append((nr, nc, cost + 1))


for i in range(N):
    for j in range(M):
        result = max(result, bfs(i, j))

print(result)
