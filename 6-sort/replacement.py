N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

A.sort(reverse=True)
B.sort(reverse=True)

for i in range(K):
    sum += B[i]

for i in range(N - K):
    sum += A[i]

print(sum)
