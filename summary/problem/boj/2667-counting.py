from sys import stdin

input = stdin.readline

N = int(input())
home_list = [list(input()) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
result = []


def count_home(row, col):
    home_list[row][col] = '0'
    count = 0

    for direction_idx in range(len(dr)):
        nr = row + dr[direction_idx]
        nc = col + dc[direction_idx]

        if (nr >= 0 and nr < N and nc >= 0 and nc < N and home_list[nr][nc] == '1'):
            count += count_home(nr, nc) + 1

    return count


for row in range(N):
    for col in range(N):
        if (home_list[row][col] == '1'):
            result.append(count_home(row, col) + 1)

result.sort()

print(len(result))

for count in result:
    print(count)
