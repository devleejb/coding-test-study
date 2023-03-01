n = int(input())
num_list = [int(input()) for _ in range(n)]
max_num = max(num_list)
dp = [[0] * 4 for _ in range(max_num + 1)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, max_num + 1):
    for j in range(1, 4):
        count = 0
        for k in range(1, j + 1):
            count += dp[i - j][k]
        dp[i][j] = count

for num in num_list:
    print(sum(dp[num]))
