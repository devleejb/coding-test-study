N, n = map(int, input().split())

result_list = []

while N // n:
    result_list.append(N % n)
    N = N // n

result_list.append(N)
result_list.reverse()

print(*result_list)
