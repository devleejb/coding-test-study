from collections import deque

N, K = map(int, input().split())
min_time = -1
count = 0
visited = [-1] * 200_001


def bfs():
    global min_time, count

    q = deque()

    q.append((N, 0))

    while (q):
        node, time = q.popleft()

        if (visited[node] != -1 and time != visited[node]):
            continue

        visited[node] = time

        if (node == K and (min_time == -1 or min_time == time)):
            min_time = time
            count += 1

        if (min_time != -1 and time > min_time):
            return

        if (node < K and node + 1 <= 200_000 and visited[node + 1] == -1):
            q.append((node + 1, time + 1))

        if (node - 1 >= 0 and visited[node - 1] == -1):
            q.append((node - 1, time + 1))

        if (node < K and node * 2 <= 200_000 and visited[node * 2] == -1):
            q.append((node * 2, time + 1))


bfs()

print(min_time)
print(count)
