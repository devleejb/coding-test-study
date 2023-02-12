from collections import deque

N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs():
    q = deque()

    # (row, col, cost)
    q.append((0, 0, 1))
    visited[0][0] = True

    while (q):
        row, col, cost = q.popleft()

        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if (nr < N and nr >= 0 and nc < M and nc >= 0 and board[nr][nc] == 1 and visited[nr][nc] == False):
                visited[nr][nc] = True
                q.append((nr, nc, cost + 1))

                if ((nr, nc) == (N - 1, M - 1)):
                    print(cost + 1)
                    return


bfs()
