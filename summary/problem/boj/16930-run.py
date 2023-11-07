from collections import deque
from sys import stdin, maxsize

input = stdin.readline

N, M, K = map(int, input().split())
board = [[]] + [[''] + list(input()) for _ in range(N)]
visited = [[maxsize] * (M + 1) for _ in range(N + 1)]
start_row, start_col, end_row, end_col = map(int, input().split())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


q = deque()

q.append((start_row, start_col))
visited[start_row][start_col] = 0

while (q):
    row, col = q.popleft()

    for i in range(len(dr)):
        nr = row + dr[i]
        nc = col + dc[i]
        count = 1

        while (0 < nr and nr <= N and 0 < nc and nc <= M and board[nr][nc] != '#' and count <= K and visited[nr][nc] >= visited[row][col]):
            visited[nr][nc] = visited[row][col] + 1
            q.append((nr, nc))
            count += 1
            nr += dr[i]
            nc += dc[i]


print(-1 if visited[end_row][end_col] ==
      maxsize else visited[end_row][end_col])
print(visited)
