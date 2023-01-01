from sys import stdin

input = stdin.readline

arr_list = [list(map(int, input().split())) for _ in range(int(input()))]

for arr in arr_list:
    arr.sort(reverse=True)
    print(arr[2])
