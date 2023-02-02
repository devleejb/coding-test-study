from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
dp = [1] + ([0] * k)

for coin in coin_list:
    for j in range(k + 1):
        if (j >= coin):
            dp[j] += dp[j - coin]

print(dp[-1])
