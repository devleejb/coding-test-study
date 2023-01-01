info_list = [list(map(int, input().split())) for _ in range(10)]

max = 0
cnt = 0

for info in info_list:
    cnt = cnt - info[0] + info[1]
    max = max if max > cnt else cnt

print(max)
