from collections import deque

N, K = map(int, input().split())
visited = [-1] * 200_001


def bfs():
    global result

    q = deque()

    q.append((N, 0, N))

    while (q):
        node, time, prev_node = q.popleft()

        if (visited[node] != -1):
            continue

        visited[node] = prev_node

        if (node == K):
            print(time)
            return

        if (node < K and node + 1 <= 200_000 and visited[node + 1] == -1):
            q.append((node + 1, time + 1, node))

        if (node - 1 >= 0 and visited[node - 1] == -1):
            q.append((node - 1, time + 1, node))

        if (node < K and node * 2 <= 200_000 and visited[node * 2] == -1):
            q.append((node * 2, time + 1, node))


bfs()

idx = K
result = [K]

while (idx != N):
    result.append(visited[idx])
    idx = visited[idx]

result.reverse()

print(*result)
