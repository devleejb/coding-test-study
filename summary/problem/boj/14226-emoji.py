from collections import deque

S = int(input())

visited = [[False] * 2_001 for _ in range(2_001)]


def bfs():
    q = deque()

    q.append((1, 0, 0))

    while (q):
        node, copy, cost = q.popleft()

        if (visited[node][copy]):
            continue

        if (node == S):
            print(cost)
            return

        visited[node][copy] = cost

        if (visited[node][node] == False):
            q.append((node, node, cost + 1))

        if (copy > 0 and node + copy <= 2000 and visited[node + copy][copy] == False):
            q.append((node + copy, copy, cost + 1))

        if (node - 1 >= 0 and visited[node - 1][copy] == False):
            q.append((node - 1, copy, cost + 1))


bfs()
