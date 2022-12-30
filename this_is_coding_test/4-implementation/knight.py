col, row = list(input())

# char를 int로 변환
row = int(row)
col = ord(col) - 96

count = 8

# row 변화량 배열
dr = [-1, 1, 2, 2, 1, -1, -2, -2]
# col 변화량 배열
dc = [2, 2, 1, -1, -2, - 2, - 1, 1]

for i in range(0, len(dr)):
    nr = row + dr[i]
    nc = col + dc[i]

    if (nr > 8 or nc > 8 or nr < 1 or nc < 1):
        count -= 1

print(count)
