N, K = map(int, input().split())
bags = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i - 1][j]
        if (j - bags[i][0] >= 0):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - bags[i][0]] + bags[i][1])

print(max(dp[N]))
