import math

M = int(input())
N = int(input())

is_prime = [False, False] + [True] * (N - 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if (is_prime[i]):
        for j in range(i * 2, N + 1, i):
            is_prime[j] = False

min = -1
sum = 0

for i in range(M, N + 1):
    if (is_prime[i]):
        sum += i
        if (min == -1):
            min = i

if (min == -1):
    print(-1)
else:
    print(sum)
    print(min)
