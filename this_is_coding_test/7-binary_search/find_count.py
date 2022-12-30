from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
integer_list = list(map(int, input().split()))

left = bisect_left(integer_list, x)
right = bisect_right(integer_list, x)

if (left < right):
    print(right - left)
else:
    print(-1)
