N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        jump = board[row][col]

        if (jump == 0 or ((row, col) != (0, 0) and dp[row][col] == 0)):
            continue

        if (col + jump < N):
            dp[row][col + jump] += 1 if (row, col) == (0, 0) else dp[row][col]

        if (row + jump < N):
            dp[row + jump][col] += 1 if (row, col) == (0, 0) else dp[row][col]

print(dp[N - 1][N - 1])
