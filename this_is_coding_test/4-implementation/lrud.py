dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
op = ['L', 'R', 'U', 'D']
x, y = 1, 1

N = int(input())
planList = input().split()

for plan in planList:
    for i in range(len(op)):
        if (op[i] == plan):
            nr = x + dr[i]
            nc = y + dc[i]

    if (nr > N or nc > N or nr < 1 or nc < 1):
        continue

    x, y = nr, nc

print(x, y)
