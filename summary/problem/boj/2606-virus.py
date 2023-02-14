N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = -1

for _ in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)


def dfs(node):
    global result
    result += 1
    visited[node] = True

    for end in edges[node]:
        if (visited[end] == False):
            dfs(end)


dfs(1)

print(result)
