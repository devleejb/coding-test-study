start, end = map(int, input().split())
arr = []

num = 0

while (len(arr) < 1000):
    num += 1
    for _ in range(num):
        arr.append(num)

sum = 0

for i in range(start - 1, end):
    sum += arr[i]

print(sum)
