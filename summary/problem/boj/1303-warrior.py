N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
BLUE_TEAM = 'B'
WHITE_TEAM = 'W'
blue_team_power = 0
white_team_power = 0


def dfs(row, col, team):
    visited[row][col] = True
    count = 1

    for i in range(len(dr)):
        nr = row + dr[i]
        nc = col + dc[i]

        if (nr < M and nr >= 0 and nc < N and nc >= 0 and board[nr][nc] == team and visited[nr][nc] == False):
            count += dfs(nr, nc, team)

    return count


for i in range(M):
    for j in range(N):
        if (visited[i][j] == False):
            result = dfs(i, j, board[i][j])

            if (board[i][j] == BLUE_TEAM):
                blue_team_power += result ** 2
            else:
                white_team_power += result ** 2

print(white_team_power, blue_team_power)
