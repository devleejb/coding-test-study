from sys import stdin

input = stdin.readline

input()

arr = list(map(int, input().split()))

arr.sort()

print(arr[0], arr[len(arr) - 1])
