N, S, M = map(int, input().split())
range_list = [0] + list(map(int, input().split()))
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
    for j in range(0, M + 1):
        if (j - range_list[i] >= 0 and dp[i - 1][j - range_list[i]]):
            dp[i][j] = True
        elif (j + range_list[i] <= M and dp[i - 1][j + range_list[i]]):
            dp[i][j] = True

max_idx = -1

for i in range(0, M + 1):
    if (dp[N][i]):
        max_idx = i

print(max_idx)
