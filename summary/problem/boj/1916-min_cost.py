from sys import maxsize, stdin
import heapq

input = stdin.readline

N = int(input())
M = int(input())
dis_list = [maxsize] * (N + 1)
edge_list = [[] for _ in range(N + 1)]
heap = []

for _ in range(M):
    start, end, cost = map(int, input().split())
    edge_list[start].append((end, cost))

start, end = map(int, input().split())


def dijkstra():
    dis_list[start] = 0
    heapq.heappush(heap, (0, start))

    while (heap):
        cost, now = heapq.heappop(heap)

        if (dis_list[now] < cost):
            continue

        for edge in edge_list[now]:
            next_cost = cost + edge[1]
            if (dis_list[edge[0]] > next_cost):
                dis_list[edge[0]] = next_cost
                heapq.heappush(heap, (next_cost, edge[0]))


dijkstra()

print(dis_list[end])
