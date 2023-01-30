from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
in_degree_list = [0] * (N + 1)
q = deque()

for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
    in_degree_list[B] += 1

for i in range(N):
    if (in_degree_list[i + 1] == 0):
        q.append(i + 1)

for _ in range(N):
    if (not q):
        # 위상 정렬 불가능
        break
    start = q.popleft()
    print(start, end=' ')

    for end in edges[start]:
        in_degree_list[end] -= 1
        if (in_degree_list[end] == 0):
            q.append(end)
