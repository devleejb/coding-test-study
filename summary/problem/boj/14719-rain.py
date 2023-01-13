H, W = map(int, input().split())
height_list = list(map(int, input().split()))

result = 0

for i in range(H):
    for j in range(W):
        if (height_list[j] <= i):
            left = False
            right = False
            for k in range (j):
                if (height_list[k] > i):
                    left = True
                    break
            for k in range (j + 1, W):
                if (height_list[k] > i):
                    right = True
                    break
            if (left and right):
                result += 1

print(result)                

