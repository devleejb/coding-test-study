from collections import deque

N, M = map(int, input().split())
board = []
visited = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(board, visited):
    queue = deque()

    queue.appendleft((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and ny >= 0 and nx < N and ny < M and board[nx][ny] == 1 and visited[nx][ny] == -1):
                queue.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


for i in range(N):
    board.append(list(map(int, list(input()))))
    visited.append([-1] * M)

bfs(board, visited)

print(visited[N - 1][M - 1])
