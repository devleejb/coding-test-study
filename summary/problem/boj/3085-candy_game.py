from sys import stdin

input = stdin.readline

N = int(input())
candy_list = [list(input()) for _ in range(N)]
dx = [1, 0]
dy = [0, 1]
result = 0


def count_max_candy():
    result = 1
    row_dp = [1] * N
    col_dp = [1] * N

    for i in range(N):
        for j in range(N - 1):
            if (candy_list[i][j] == candy_list[i][j + 1]):
                row_dp[j + 1] = row_dp[j] + 1
                result = max(row_dp[j + 1], result)
            if (candy_list[j][i] == candy_list[j + 1][i]):
                col_dp[j + 1] = col_dp[j] + 1
                result = max(col_dp[j + 1], result)
        row_dp = [1] * N
        col_dp = [1] * N

    return result


for i in range(N):
    for j in range(N):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if (0 < nx and nx < N and 0 < ny and ny < N):
                candy_list[i][j], candy_list[nx][ny] = candy_list[nx][ny], candy_list[i][j]
                result = max(result, count_max_candy())
                candy_list[i][j], candy_list[nx][ny] = candy_list[nx][ny], candy_list[i][j]

print(result)
