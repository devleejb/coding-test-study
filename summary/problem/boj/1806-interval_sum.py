from sys import maxsize

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
interval_sum = 0
end = 0
result = maxsize

for start in range(len(num_list)):
    while (interval_sum < S and end < N):
        interval_sum += num_list[end]
        end += 1

    if (interval_sum >= S):
        result = min(result, end - start)

    interval_sum -= num_list[start]

if (result == maxsize):
    print(0)
else:
    print(result)
