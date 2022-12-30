# 3
# 1 2 3
# 4 5 6
# 7 8 9
arr = [list(map(int, input().split())) for _ in range(int(input()))]

print(arr)

# 4 10 20 30 40
N, *arr2 = map(int, input().split())

print(N, arr2)

# 3
# AAAA
# BBBB
# CCCC
arr3 = [list(input()) for _ in range(int(input()))]

print(arr3)
