from collections import deque

A, B = map(int, input().split())
visited = {}


def bfs():
    q = deque()

    q.append((A, 1))

    while (q):
        num, cost = q.pop()

        if (num == B):
            print(cost)
            return

        if (str(num) in visited):
            continue

        visited[str(num)] = True

        if (not str(num * 2) in visited and num * 2 <= B):
            q.append((num * 2, cost + 1))

        addedNum = int(str(num) + '1')
        if (not str(addedNum) in visited and addedNum <= B):
            q.append((addedNum, cost + 1))

    print(-1)


bfs()
