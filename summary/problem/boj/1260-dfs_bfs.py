from collections import deque

N, M, V = map(int, input().split())
edges = [[] for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

for i in range(1, N + 1):
    edges[i].sort()


def dfs(node):
    visited_dfs[node] = True
    print(node, end=' ')

    for end in edges[node]:
        if (visited_dfs[end] == False):
            dfs(end)


def bfs():
    q = deque()
    q.append(V)
    visited_bfs[V] = True

    while (q):
        node = q.popleft()

        print(node, end=' ')

        for end in edges[node]:
            if (visited_bfs[end] == False):
                visited_bfs[end] = True
                q.append(end)


dfs(V)
print()
bfs()
