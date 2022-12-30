N = int(input())
count = 0

for i in range(0, N + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            if (i % 10 == 3 or j % 10 == 3 or k % 10 == 3 or i // 10 == 3 or j // 10 == 3 or k // 10 == 3):
                count += 1

print(count)
