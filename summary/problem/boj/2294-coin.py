from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
dp = [0] + [10001] * k

for coin in coin_list:
    for target in range(coin, k + 1):
        dp[target] = min(dp[target], dp[target - coin] + 1)

if (dp[k] == 10001):
    print(-1)
else:
    print(dp[k])
