from sys import maxsize

N = int(input())
board = list(input())
dp = [maxsize] * N

dp[0] = 0

for i in range(N):
    now_char = board[i]
    for j in range(i):
        prev_char = ''

        if (now_char == 'B'):
            prev_char = 'J'
        elif (now_char == 'O'):
            prev_char = 'B'
        else:
            prev_char = 'O'

        if (dp[j] != maxsize and board[j] == prev_char):
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

print(dp[N - 1] if dp[N - 1] != maxsize else -1)
