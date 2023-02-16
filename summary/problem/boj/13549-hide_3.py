from collections import deque
from sys import maxsize

N, K = map(int, input().split())
result = maxsize
visited = [maxsize] * 200_001


def bfs():
    global result

    q = deque()

    q.append((N, 0))

    while (q):
        node, time = q.popleft()

        if (visited[node] < time):
            continue

        if (node == K):
            result = min(result, time)

        visited[node] = time

        if (node < K and node + 1 <= 200_000 and visited[node + 1] > time + 1):
            q.append((node + 1, time + 1))

        if (node - 1 >= 0 and visited[node - 1] > time + 1):
            q.append((node - 1, time + 1))

        if (node < K and node * 2 <= 200_000 and visited[node * 2] > time):
            q.append((node * 2, time))


bfs()

print(result)
