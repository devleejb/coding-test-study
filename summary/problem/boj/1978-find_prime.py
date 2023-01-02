import math

input()
arr = list(map(int, input().split()))

prime_list = [True] * 1001
prime_list[1] = False

for i in range(int(math.sqrt(1000))):
    if (not prime_list[i + 2]):
        continue
    j = 2

    while (i + 2) * j <= 1000:
        prime_list[(i + 2) * j] = False
        j = j + 1

cnt = 0

for num in arr:
    if (prime_list[num]):
        cnt += 1

print(cnt)
